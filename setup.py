# -*- coding: utf-8 -*-
#
# Copyright 2010, Pradeep Gowda
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
"""Setup script."""

import os
import setuptools


def read(*rnames):
    return open(os.path.join(os.getcwd(), *rnames)).read()


setuptools.setup(
    name='pyremlog',
    version=read('version.txt').strip(),
    author="Pradeep Gowda",
    author_email="pradeep at btbytes dot com",
    description="Python Remote Logger.",
    long_description=(
        read('README.md')
        + '\n\n' +
        read('CHANGES.md')
        ),
    license="Apache License 2.0",
    keywords=["logging"],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Server',
        ],
    url='http://github.com/btbytes/pyremlog',
    packages=setuptools.find_packages('src'),
    include_package_data=True,
    package_dir={'': 'src'},
    install_requires=[
        'setuptools',
        ],
    extras_require=dict(
        ),
    zip_safe=False,
    )
