#!/usr/bin/env python

from distutils.core import setup
from glob import glob

setup(name='envpickle',
      version='0.0.1',
      description='Pickle your environment for later use',
      author='Noel Dawe',
      author_email='noel.dawe@cern.ch',
      url='http://github.com/ndawe/envpickle',
      packages=['envpickle'],
      scripts=glob('scripts/*')
     )
