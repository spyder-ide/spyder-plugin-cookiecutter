# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) {{ cookiecutter.author }}
#
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------
"""{{ cookiecutter.plugin_name }} Widget."""

from qtpy.QtWidgets import QWidget

class {{ cookiecutter.plugin_name.replace(' ', '') }}Widget(QWidget):
    """{{ cookiecutter.plugin_name }} widget."""
    def __init__(self, parent):
        QWidget.__init__(self, parent)

        self.setWindowTitle("{{ cookiecutter.plugin_name }}")
