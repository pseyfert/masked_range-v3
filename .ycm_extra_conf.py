##########################################################################
# Simple ycm_extra_conf.py example                                       #
# Copyright (C) <2013>  Onur Aslan  <onur@onur.im>                       #
#                                                                        #
# This file is loaded by default. Place your own .ycm_extra_conf.py to   #
# project root to override this.                                         #
#                                                                        #
# This program is free software: you can redistribute it and/or modify   #
# it under the terms of the GNU General Public License as published by   #
# the Free Software Foundation, either version 3 of the License, or      #
# (at your option) any later version.                                    #
#                                                                        #
# This program is distributed in the hope that it will be useful,        #
# but WITHOUT ANY WARRANTY; without even the implied warranty of         #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          #
# GNU General Public License for more details.                           #
#                                                                        #
# You should have received a copy of the GNU General Public License      #
# along with this program.  If not, see <http://www.gnu.org/licenses/>.  #
##########################################################################
# modifications to integrate into BsToKMuNu                              #
# by Paul Seyfert <Paul.Seyfert@cern.ch>                                 #
##########################################################################

import os

localheaders = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "include")

# some default flags
# for more information install clang-3.2-doc package and
# check UsersManual.html
flags = [
    '-Wall',
    '-Werror',
    '-std=c++17',
    '-x',
    'c++',
]

flags += ['-isystem'+'/home/pseyfert/.local/include', ]
flags += ['-I'+localheaders, ]

# youcompleteme is calling this function to get flags
# You can also set database for flags. Check: JSONCompilationDatabase.html in
# clang-3.2-doc package


def FlagsForFile(filename):
    return {
        'flags': flags,
        'do_cache': True
    }
