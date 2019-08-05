"""
Does the following:

"""

from __future__ import print_function
import os
import sys
import shutil
from subprocess import call

# Get the root project directory
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove(filepath):
    """Remove files or directory given a path."""
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


create_widget = '{{cookiecutter.graphical_plugin}}' == 'y'

if not create_widget:
    # Remove the widgets folder if the plugin is not graphical
    remove(os.path.join(PROJECT_DIRECTORY,
                        '{{cookiecutter.python_package_name}}', 'widgets'))


valid_name = '{{cookiecutter.python_package_name}}'.startswith('spyder_')

if not valid_name:
    print("Python package names for third-party Spyder plugins must start"
          "with spyder_")
    sys.exit(1)


def init_git():
    """Start git repository"""
    try:
        call(['git', 'init'])
    except Exception:
        print("git isn't avalaible, please install git and run:\n  $ git init")


# 1. Moves gitattributes to .gitattributes
# Having a .gitattributes with wrong syntax (because it has some jinja syntax)
# cause some annoying warnings

old_gitattributes = os.path.join(PROJECT_DIRECTORY, 'gitattributes')
new_gitattributes = os.path.join(PROJECT_DIRECTORY, '.gitattributes')

os.rename(old_gitattributes, new_gitattributes)


# 2. Create empty assets directory

assets_dir = os.path.join(PROJECT_DIRECTORY,
                          '{{ cookiecutter.python_package_name }}',
                          'assets')

os.mkdir(assets_dir)
