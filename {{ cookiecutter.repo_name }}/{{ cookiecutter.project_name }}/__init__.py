# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) {{ cookiecutter.author }}
#
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------
"""Spyder {{ cookiecutter.plugin_name }} Plugin."""

{% if cookiecutter.use_versioneer == 'y' -%}
from ._version import get_versions

__version__ = get_versions()['version']
del get_versions

{%- else %}
from ._version import __version__
{%- endif %}

# The following statements are required to register this 3rd party plugin:

from .{{ cookiecutter.plugin_name.lower().replace(' ', '') }}plugin import {{ cookiecutter.plugin_name.replace(' ', '') }}Plugin

PLUGIN_CLASS = {{ cookiecutter.plugin_name.replace(' ', '') }}Plugin
