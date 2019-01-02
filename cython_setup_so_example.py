# Inspired by content from cython.readthedocs.io

from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

ext_modules = [
    Extension("cython_so_example",
              sources=["cython_so_example.pyx"],
              libraries=["candpy"]
              )
]

setup(name="CythonSoExample",
      ext_modules=cythonize(ext_modules))