"""
Does the following:

1. Removes _version file and run versionner install if use_versionner == y
"""

from __future__ import print_function
import os
from subprocess import call

# Get the root project directory
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)


def remove_version_file():
    """Removes the _version file if versionner is going to be used."""
    file_name = os.path.join(PROJECT_DIRECTORY,
                             '{{ cookiecutter.project_name }}/_version.py')
    remove_file(file_name)


def install_versioneer():
    """Start versioneer in the repository, this will create
    versioneer.py and _version.py."""
    call(['versioneer', 'install'])

# 1. Removes _version file and run versionner install if use_versionner == y

if '{{ cookiecutter.use_versioneer }}'.lower() == 'y':
    remove_version_file()
    try:
        install_versioneer()
    except Exception:
        print(
            "versioneer isn't avalaible, please install versioneer and run:\n  $ versioneer install")
