# Inspired by content from cython.readthedocs.io

from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("cython_helloworld_example.pyx")
)