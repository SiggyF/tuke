#!/usr/bin/python2.5
# vim: tabstop=4 expandtab shiftwidth=4 fileencoding=utf8
# ### BOILERPLATE ###
# Tuke - Electrical Design Automation toolset
# Copyright (C) 2008 Peter Todd <pete@petertodd.org>
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# ### BOILERPLATE ###

import sys, os, getopt
from setuptools import setup, find_packages, Extension

if sys.version_info[:2] < (2,5):
    print "Sorry, Tuke requires version 2.5 or later of python"
    sys.exit(1)

setup(
    name="tuke",
    version='0.1',
    packages = find_packages(),
    ext_modules = [
        Extension('Tuke.context._context',
                  sources = ['Tuke/context/_context/cfunction.c',
                             'Tuke/context/_context/source.c',
                             'Tuke/context/_context/weakset.c',
                             'Tuke/context/_context/wrap_dict.c',
                             'Tuke/context/_context/wrap_list.c',
                             'Tuke/context/_context/wrap_tuple.c',
                             'Tuke/context/_context/wrapper.c',
                             'Tuke/context/_context/__init__.c']),
        ],
    description="Tuke EDA toolkit.",
    author="Peter Todd",
    author_email="pete@petertodd.org",
    url="http://petertodd.org/tech/example-projects",
    )
