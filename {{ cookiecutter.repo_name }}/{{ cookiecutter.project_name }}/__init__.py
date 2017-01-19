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
