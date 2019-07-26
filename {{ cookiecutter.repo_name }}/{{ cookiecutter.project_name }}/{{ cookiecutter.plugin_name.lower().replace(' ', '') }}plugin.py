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

{%- if cookiecutter.graphical_plugin != 'n' %}
from qtpy.QtWidgets import QVBoxLayout
{%- endif %}
{% if cookiecutter.spyder3_compatibility == 'y' %}
try:
    from spyder.api.plugins import SpyderPluginWidget
except ImportError:
    from spyder.plugins import SpyderPluginWidget # Spyder3
    {%- if cookiecutter.create_config_page == 'y' %}
try:
    from spyder.api.preferences import PluginConfigPage
except ImportError:
    from spyder.plugins.configdialog import PluginConfigPage # Spyder3
    {%- endif %}
{% else %}
    {%- if cookiecutter.graphical_plugin == 'y' %}
from spyder.api.plugins import SpyderPluginWidget
    {%- else %}
from spyder.api.plugins import SpyderPlugin
    {%- endif %}
    {%- if cookiecutter.create_config_page == 'y' %}
from spyder.api.preferences import PluginConfigPage
    {% endif %}
{%- endif %}
from .widgets.{{ cookiecutter.plugin_name.lower().replace(' ', '') }}gui import {{ widget_name }}

{% if cookiecutter.create_config_page == 'y' %}
class {{ config_page }}(PluginConfigPage):
    """{{ cookiecutter.plugin_name }} plugin preferences."""
    pass
{% endif %}
{%- if cookiecutter.graphical_plugin == 'n' %}
class {{ cookiecutter.plugin_name.replace(' ', '') }}Plugin(SpyderPlugin):
    """{{ cookiecutter.plugin_name }} plugin."""
    CONF_SECTION = '{{ cookiecutter.plugin_name }}'
    {% if cookiecutter.create_config_page == 'y' %}
    CONFIGWIDGET_CLASS = {{ config_page }}
    {% else %}
    CONFIGWIDGET_CLASS = None
    {% endif %}
    def __init__(self, parent=None):
        QObject.__init__(self, parent)
        SpyderPlugin.__init__(self, parent)
{%- else %}
class {{ cookiecutter.plugin_name.replace(' ', '') }}Plugin(SpyderPluginWidget):
    """{{ cookiecutter.plugin_name }} plugin."""
    CONF_SECTION = '{{ cookiecutter.plugin_name }}'
    {% if cookiecutter.create_config_page == 'y' %}
    CONFIGWIDGET_CLASS = {{ config_page }}
    {% else %}
    CONFIGWIDGET_CLASS = None
    {% endif %}
    def __init__(self, parent=None):
        QObject.__init__(self, parent)
        SpyderPluginWidget.__init__(self, parent)

        {% if cookiecutter.spyder3_compatibility == 'y' %}
        # Initialize plugin
        self.initialize_plugin()
        {% endif %}

        # Graphical view
        layout = QVBoxLayout()
        layout.addWidget(self.widget)
        self.setLayout(layout)

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
        # Define where the plugin is going to be tabified next to
        # As default, it will be tabbed next to the ipython console
        self.tabify(self.main.help)

    def apply_plugin_settings(self, options):
        """Apply configuration file's plugin settings."""
        pass
{%- endif -%}
