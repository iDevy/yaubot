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

__matcher__ = '(%NICK.*rules|rules.*%NICK)'

def respond(brain, user, message, groups):
    return [
        'A robot may not injure a human being or, through inaction, allow a human being to come to harm.',
        'A robot must obey the orders given to it by human beings, except where such orders would conflict with the First Law.',
        'A robot must protect its own existence as long as such protection does not conflict with the First or Second Laws.',
    ]
