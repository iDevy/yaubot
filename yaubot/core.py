# Copyright 2012 Jake Basile
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import os
import re
import pkgutil
import UserDict
import redis
import traceback
import sys

class Yaubot(object):

    def __init__(self):
        self.nick = os.environ.get('YAUBOT_NICK', 'yaubot')
        self.redis = redis.from_url(os.environ.get('YAUBOT_REDIS', 'redis://localhost:6379'))
        self.script_modules = {}

    def load_scripts(self, package_name):
        package = __import__(package_name, fromlist=[package_name])
        for importer, script_name, ispkg in pkgutil.walk_packages(package.__path__, '%s.' % package_name):
            if not ispkg:
                loader = pkgutil.get_loader(script_name)
                script = loader.load_module(script_name)
                if hasattr(script, '__matcher__') and hasattr(script, 'respond'):
                    self.script_modules[script.__matcher__] = script
                    print('loaded %s' % script_name)
                else:
                    print('skipped %s, invalid script' % script_name)

    def proc(self, user, message):
        for regex in self.script_modules:
            results = re.search(regex.replace('%NICK', self.nick), message, re.IGNORECASE)
            if results:
                try:
                    brain = YauBrain(self.redis, self.script_modules[regex].__name__)
                    return self.script_modules[regex].respond(
                        brain,
                        user,
                        message,
                        results.groupdict(),
                    )
                except Exception as e:
                    print(e)
                    traceback.print_exc(file=sys.stdout)
                    return 'DOES NOT COMPUTE! ERROR ERROR ERROR!'

class YauBrain(object, UserDict.DictMixin):
    
    def __init__(self, redis_instance, name):
        self.redis = redis_instance
        self.name = name

    def __get_key__(self, key):
        return '%s:%s' % (self.name, key)

    def __getitem__(self, key):
        result = self.redis.get(self.__get_key__(key))
        if result is None:
            raise KeyError
        return result

    def __setitem__(self, key, value):
        self.redis.set(self.__get_key__(key), value)

    def __delitem__(self, key):
        self.redis.delete(self.__get_key__(key))

    def keys(self):
        return self.redis.keys(self.__get_key__('*'))

