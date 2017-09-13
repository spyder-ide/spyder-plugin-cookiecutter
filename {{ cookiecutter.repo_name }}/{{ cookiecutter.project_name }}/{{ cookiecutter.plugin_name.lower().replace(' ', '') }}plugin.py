# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) {{ cookiecutter.author }}
#
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------
"""{{ cookiecutter.plugin_name }} Plugin."""

{%- set widget_name = cookiecutter.plugin_name.replace(' ', '') + 'Widget' -%}
{%- set config_page = cookiecutter.plugin_name.replace(' ', '') + 'ConfigPage' %}

from qtpy.QtWidgets import QVBoxLayout

{% if cookiecutter.spyder3_compatibility == 'y' -%}
try:
    from spyder.api.plugins import SpyderPluginWidget
except ImportError:
    from spyder.plugins import SpyderPluginWidget # Spyder3
    {%- if cookiecutter.create_config_page == 'y' %}
try:
    from spyder.api.preferences import
except ImportError:
    from spyder.plugins.configdialog import PluginConfigPage # Spyder3
    {%- endif %}
{% else -%}
from spyder.api.plugins import SpyderPluginWidget
    {%- if cookiecutter.create_config_page == 'y' %}
from spyder.api.preferences import PluginConfigPage
    {%- endif %}
{%- endif -%}

from .widgets.{{ cookiecutter.plugin_name.lower().replace(' ', '') }}gui import {{ widget_name }}
{% if cookiecutter.create_config_page == 'y' %}

class {{ config_page }}(PluginConfigPage):
    """{{ cookiecutter.plugin_name }} plugin preferences."""
    pass
{% endif %}

class {{ cookiecutter.plugin_name.replace(' ', '') }}Plugin(SpyderPluginWidget):
    """{{ cookiecutter.plugin_name }} plugin."""
    CONF_SECTION = '{{ cookiecutter.plugin_name }}'
{% if cookiecutter.create_config_page == 'y' %}
    CONFIGWIDGET_CLASS = {{ config_page }}
{% else %}
    CONFIGWIDGET_CLASS = None
{% endif %}

    def __init__(self, parent=None):
        SpyderPluginWidget.__init__(self, parent)
        self.main = parent # Spyder3

        # Create widget and add to dockwindow
        self.widget = {{ widget_name }}(self.main)
        layout = QVBoxLayout()
        layout.addWidget(self.widget)
        self.setLayout(layout)

        # Initialize plugin
        self.initialize_plugin()

    # --- SpyderPluginWidget API ----------------------------------------------
    def get_plugin_title(self):
        """Return widget title."""
        return "{{ cookiecutter.plugin_name }}"

    def get_focus_widget(self):
        """Return the widget to give focus to."""
        return self.widget

    def refresh_plugin(self):
        """Refresh {{ widget_name }} widget."""
        pass

    def get_plugin_actions(self):
        """Return a list of actions related to plugin."""
        return []

    def register_plugin(self):
        """Register plugin in Spyder's main window."""
        self.main.add_dockwidget(self)

    def on_first_registration(self):
        """Action to be performed on first plugin registration."""
        self.main.tabify_plugins(self.main.help, self)

    def apply_plugin_settings(self, options):
        """Apply configuration file's plugin settings."""
        pass
