#!/usr/bin/env python

#     <ChaThon: A CLI Chat Application>
#     Copyright (C) <2022>  <Cromega>

#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU Affero General Public License as published
#     by the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.

#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU Affero General Public License for more details.

#     You should have received a copy of the GNU Affero General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.

from importlib_metadata import entry_points
from setuptools import setup

setup(
        name="ChaThon",
        version="1.0.0",
        description="A CLI chat implementation",
        author="Cromega",
        author_email="cr.jrg08@gmail.com",
        py_modules=["server", "app"],
        entry_points = {
            "console_scripts" : ["chathon=app:run"]
        })
