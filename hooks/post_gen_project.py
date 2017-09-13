"""
Does the following:

1. Removes _version file and run versioneer install if use_versioneer == y
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
    """Removes the _version file if versioneer is going to be used."""
    file_name = os.path.join(PROJECT_DIRECTORY,
                             '{{ cookiecutter.project_name }}',
                             '_version.py')
    remove_file(file_name)


def install_versioneer():
    """Start versioneer in the repository, this will create
    versioneer.py and _version.py."""
    try:
        call(['versioneer', 'install'])
    except Exception:
        print(
            "versioneer isn't avalaible, please install versioneer and run:\n  $ versioneer install")

def init_git():
    """Start git repository"""
    try:
        call(['git', 'init'])
    except Exception:
        print("git isn't avalaible, please install git and run:\n  $ git init")


# 1. Removes _version file and run versioneer install if use_versioneer == y

if '{{ cookiecutter.use_versioneer }}'.lower() == 'y':
    remove_version_file()

    init_git()
    install_versioneer()


# 2. Moves gitattributes to .gitattributes
# Having a .gitattributes with wrong syntax (because it has some jinja syntax)
# cause some annoying warnings

old_gitattributes = os.path.join(PROJECT_DIRECTORY, 'gitattributes')
new_gitattributes = os.path.join(PROJECT_DIRECTORY, '.gitattributes')


os.rename(old_gitattributes, new_gitattributes)
