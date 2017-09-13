# -*- coding: utf-8 -*-

import pytest


@pytest.fixture
def context():
    return {
        'author': 'Spyder Project Contributors',
        'email': 'admin@spyder-ide.org',
        'github_username': 'spyder-ide',
        'plugin_name': 'Demo',
        'repo_name': 'spyder-demo',
        'project_name': 'spyder_demo',
        'description': 'Plugin for Spyder IDE.',
        'version': '0.1.0',
    }


def test_default_configuration(cookies, context):
    result = cookies.bake(extra_context=context)
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == context['repo_name']
    assert result.project.isdir()

    # Test creation of project files

    toplevel_files = ['.github', 'conda.recipe', 'CHANGELOG.md',
                      'CONTRIBUTORS.md', 'LICENSE.txt', 'MANIFEST.in',
                      'README.rst', 'RELEASE.md', 'setup.py',
                      'requirements.txt', '.gitattributes']

    found_toplevel_files = [f.basename for f in result.project.listdir()]

    for path in toplevel_files:
        assert path in found_toplevel_files

    # Test creation of plugin files

    project_files = ['widgets', 'assets', 'demoplugin.py', '_version.py',
                     '__init__.py', 'tests']

    project_dir = result.project.join(context['project_name'])
    found_project_files = [f.basename for f in project_dir.listdir()]

    for path in project_files:
        assert path in found_project_files
