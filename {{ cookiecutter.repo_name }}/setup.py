# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) {{ cookiecutter.author }}
#
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------
"""Setup script for {{ cookiecutter.project_name }}."""

# Standard library imports
import ast
import os

# Third party imports
from setuptools import find_packages, setup


HERE = os.path.abspath(os.path.dirname(__file__))


def get_description():
    """Get long description."""
    with open(os.path.join(HERE, 'README.rst'), 'r') as f:
        data = f.read()
    return data


REQUIREMENTS = ['spyder']


setup(
    name='{{ cookiecutter.repo_name }}',
    keywords=['Spyder', 'Plugin'],
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',
    license='MIT',
    author='{{ cookiecutter.author }}',
    author_email='{{ cookiecutter.email }}',
    description='{{ cookiecutter.description }}',
    long_description=get_description(),
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=REQUIREMENTS,
    include_package_data=True,
    package_data={'assets':['*']},
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
{%- if cookiecutter.support_python_2 == 'y' %}
        'Programming Language :: Python :: 2.7',
{%- endif %}
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ])
