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
{%- if cookiecutter.use_versioneer == 'y' %}
import versioneer
{%- endif %}


HERE = os.path.abspath(os.path.dirname(__file__))

{%- if cookiecutter.use_versioneer == 'n' %}
def get_version(module='{{ cookiecutter.project_name }}'):
    """Get version."""
    with open(os.path.join(HERE, module, '_version.py'), 'r') as f:
        data = f.read()
    lines = data.split('\n')
    for line in lines:
        if line.startswith('version_info'):
            version_tuple = ast.literal_eval(line.split('=')[-1].strip())
            version = '.'.join(map(str, version_tuple))
            break
    return version
{%- endif %}

def get_description():
    """Get long description."""
    with open(os.path.join(HERE, 'README.rst'), 'r') as f:
        data = f.read()
    return data


REQUIREMENTS = ['spyder']


setup(
    name='{{ cookiecutter.project_name }}',
{%- if cookiecutter.use_versioneer == 'y' %}
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
{%- else %}
    version=get_version(),
{%- endif %}
    keywords=['Spyder', 'Plugin'],
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_username }}',
    license='MIT',
    author='{{ cookiecutter.author }}',
    author_email='{{ cookiecutter.email }}',
    description='{{ cookiecutter.description }}',
    long_description=get_description(),
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=REQUIREMENTS,
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
