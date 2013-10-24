#!/usr/bin/env python

from setuptools import setup

def readme():
    with open("README.rst") as it:
        return it.read()

if __name__ == '__main__':
    setup(
        name = 'pipeto',
        version = '0.0.1',
        description = 'linux pipe style for python',
        long_description = readme(),
        author = "Yan Wenjun",
        author_email = "mylastnameisyan@gmail.com",
        license = 'MIT',
        url = 'https://github.com/v2e4lisp/pipeto'
        py_modules = ["pipeto"],
        classifiers = [
            'License :: OSI Approved :: MIT License',
            'Topic :: Software Development :: Libraries',
        ]
    )
