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

import random

__matcher__ = '(?P<num>[0-9]{1,3})d(?P<type>[0-9]{1,4})'

def respond(brain, user, message, groups):
    num = int(groups['num'])
    type = int(groups['type'])
    result = sum(random.randint(1, type) for i in xrange(num))
    return '%s rolled %s.' % (user, result)
