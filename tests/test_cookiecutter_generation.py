# -*- coding: utf-8 -*-

import pytest


@pytest.fixture
def context():
    return {
        'author': 'Spyder Project Contributors',
        'email': 'admin@spyder-ide.org',
        'github_username': 'spyder-ide',
        'plugin_name': 'Demo',
        'git_repo_name': 'spyder-demo',
        'python_package_name': 'spyder_demo',
        'description': 'Plugin for Spyder IDE.',
        'version': '0.1.0',
    }


@pytest.fixture
def non_graphical():
    return {
        'author': 'Spyder Project Contributors',
        'email': 'admin@spyder-ide.org',
        'github_username': 'spyder-ide',
        'plugin_name': 'Demo-nongraphic',
        'git_repo_name': 'spyder-demo-nongraphic',
        'python_package_name': 'spyder_demo_nongraphic',
        'description': 'Plugin for Spyder IDE.',
        'version': '0.1.0',
        'graphical_plugin': 'n'
    }


def test_default_configuration(cookies, context):
    result = cookies.bake(extra_context=context)
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == context['git_repo_name']
    assert result.project.isdir()

    # Test creation of project files

    toplevel_files = ['MANIFEST.in', 'README.rst', 'setup.py',
                      'requirements.txt', '.gitattributes']

    found_toplevel_files = [f.basename for f in result.project.listdir()]

    for path in toplevel_files:
        assert path in found_toplevel_files

    # Test creation of plugin files

    project_files = ['widgets', 'assets', 'demoplugin.py', '_version.py',
                     '__init__.py', 'tests']

    project_dir = result.project.join(context['python_package_name'])
    found_project_files = [f.basename for f in project_dir.listdir()]

    for path in project_files:
        assert path in found_project_files


def test_non_graphical_configuration(cookies, non_graphical):
    """Test generation of non-graphical plugin."""
    result = cookies.bake(extra_context=non_graphical)
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == non_graphical['git_repo_name']
    assert result.project.isdir()

    # Test creation of project files

    toplevel_files = ['MANIFEST.in', 'README.rst', 'setup.py',
                      'requirements.txt', '.gitattributes']

    found_toplevel_files = [f.basename for f in result.project.listdir()]

    for path in toplevel_files:
        assert path in found_toplevel_files

    # Test creation of plugin files

    project_files = ['assets', 'demo-nongraphicplugin.py', '_version.py',
                     '__init__.py', 'tests']

    project_dir = result.project.join(non_graphical['python_package_name'])
    found_project_files = [f.basename for f in project_dir.listdir()]

    for path in project_files:
        assert path in found_project_files
