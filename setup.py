#!/usr/bin/python
# -*- coding: utf-8 -*-


__author__ = "Carlos Mão de Ferro"
__copyright__ = ""
__credits__ = "Carlos Mão de Ferro"
__license__ = "MIT"
__version__ = "0.0"
__maintainer__ = ["Ricardo Ribeiro", "Carlos Mão de Ferro"]
__email__ = ["ricardojvr at gmail.com", "cajomferro at gmail.com"]
__status__ = "Development"
__updated__ = "2015-12-10"

from setuptools import setup, find_packages

setup(

    name='Reagents DB',
    version='1.1.0',
    description="""Database to manage reagents stock.""",
    author='Ricardo Ribeiro and Carlos Mao de Ferro',
    author_email='carlos.maodeferro@neuro.fchampalimaud.org',
    license='MIT',

    url='http://gitlab/swp/Reagents-db.git',

    packages=['reagents'],

)
