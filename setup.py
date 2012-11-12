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

from setuptools import setup, find_packages

setup(
    name='yaubot',
    version='0.1',
    description='Yet Another Unnecessary Bot',
    author='Jake Basile',
    url='https://github.com/jakebasile/yaubot',
    download_url='https://github.com/downloads/jakebasile/yaubot-0.1.tar.gz',
    packages=find_packages(),
    scripts=[
        'yaubot-runner',
    ],
    install_requires=[
        'Twisted==12.2.0',
        'zope.interface==4.0.1',
        'redis==2.7.1',
    ],
)


