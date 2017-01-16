# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) {{ cookiecutter.author }}
#
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------
"""{{ cookiecutter.plugin_name }} Plugin."""

from spyder.api.plugins import SpyderPluginWidget
{% if cookiecutter.create_config_page == 'y' %}
from spyder.api.preferences import PluginConfigPage
{% endif %}

{% if cookiecutter.create_config_page == 'y' %}
class {{ cookiecutter.plugin_name.replace(' ', '') }}ConfigPage(PluginConfigPage):
    """{{ cookiecutter.plugin_name }} plugin preferences."""
    pass
{% endif %}

class {{ cookiecutter.plugin_name.replace(' ', '') }}Plugin(SpyderPluginWidget):
    """{{ cookiecutter.plugin_name }} plugin."""
    pass

