#!/usr/bin/env python

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