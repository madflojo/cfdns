#!/usr/bin/env python

from setuptools import setup

def get_long_description():
    try:
        with open('README.md', 'r') as f:
            return f.read()
    except IOError:
        return ''

setup(
    name="cfdns",
    version="0.1.0",
    author='madflojo',
    author_email='ben@bencane.com',
    description='Command line tool for manipulating DNS of CloudFlare hosted domains',
    url='https://github.com/madflojo/cfdns',
    long_description=get_long_description(),
    packages=["cfdns"],
    entry_points={
        'console_scripts': [
            'cfdns = cfdns:main'
        ]
    },
    license='Apache 2',
    install_requires=["requests", "argparse", "logging"],
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Internet :: Name Service (DNS)'
    ]
)
