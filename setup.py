# -*- coding: utf-8 -*-
"""
    katla
    :copyright: (c) 2016 by Yann Gravrand.
    :license: BSD, see LICENSE for more details.
"""

from setuptools import setup, find_packages


setup(
    name='katla',
    version='0.0.1',
    author='Yann Gravrand',
    author_email='y.gravrand@gmail.com',
    description='Katla is a web renderer using components, written in Python',
    long_description='',
    license='BSD',
    keywords='',
    url='',
    packages=find_packages(),
    zip_safe=True,
    install_requires=(
        'lxml',
    ),
    extras_require={'test': ('pytest', 'werkzeug')}
)
