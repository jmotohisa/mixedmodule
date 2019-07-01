#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from numpy.distutils.core import setup, Extension
# # from numpy.distutils.misc_util import Configuration

from distutils.core import setup, Extension

hello_sources = [
    'hello.i',
    'hello_f.f',
    'hello_c.c',
    # 'hello.pyf',
]

ext_hello = Extension(
    '_hello',
    sources=hello_sources,
    # libraries=['gsl', 'gslcblas'],
    # library_dirs=['/opt/local/lib'],
)

if __name__ == '__main__':
    setup(
        name="hello",
        version="0.0.0",
        description="hello test by jm",
        ext_modules=[ext_hello],
        py_modules=['hello'],
    )

# config.add_library("hello", sources=hello_sources)
# config.add_extension("hello_f2py",
#                      sources=["hello.pyf"],
#                      libraries=["hello"], depends=hello_sources)

# config = Configuration()

# config.add_library("hello", sources=hello_sources)
# config.add_extension("hello_f2py",
#                      sources=[hello_f2py.pyf],
#                      libraries=["hello"], depends=hello_sources)

# setup(**config.todict())
