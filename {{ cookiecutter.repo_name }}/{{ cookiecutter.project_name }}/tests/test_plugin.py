# -*- coding: utf-8 -*-
#
# Copyright © Spyder Project Contributors
# Licensed under the terms of the MIT License
#
"""Tests for the plugin."""

{%- set module_name = cookiecutter.plugin_name.lower().replace(' ', '') + 'plugin' -%}
{%- set plugin_name = cookiecutter.plugin_name.replace(' ', '') + 'Plugin' -%}
{%- set object_name = cookiecutter.plugin_name.lower() -%}

# Test library imports
import pytest

# Local imports
from {{ cookiecutter.project_name }}.{{ module_name }} import {{ plugin_name }}


@pytest.fixture
def setup_{{ object_name }}(qtbot):
    """Set up the {{ plugin_name }} plugin."""
    {{ object_name }} = {{ plugin_name }}(None)
    qtbot.addWidget({{ object_name }})
    {{ object_name }}.show()
    return {{ object_name }}


def test_basic_initialization(qtbot):
    """Test {{ plugin_name }} initialization."""
    {{ object_name }} = setup_{{ object_name }}(qtbot)

    # Assert that plugin object exist
    assert {{ object_name }} is not None


if __name__ == "__main__":
    pytest.main()
