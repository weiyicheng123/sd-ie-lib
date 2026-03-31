"""Substance Painter plugin starter template.

Usage:
1) Copy folder `ie_painter_starter` to your Substance Painter plugins directory.
2) Restart Painter and enable the plugin.
3) Click menu: Plugins > IE Starter > Say Hello
"""

from __future__ import annotations

import traceback

# NOTE:
# These imports are available inside Substance Painter's Python runtime.
# Running this module in a normal Python interpreter will fail.
import substance_painter.ui as ui
from PySide2 import QtWidgets

PLUGIN_NAME = "IE Painter Starter"
MENU_NAME = "IE Starter"
ACTION_NAME = "Say Hello"

_menu = None
_action = None
_dock = None


def _log(message: str) -> None:
    print(f"[{PLUGIN_NAME}] {message}")


def _on_click() -> None:
    QtWidgets.QMessageBox.information(None, PLUGIN_NAME, "Hello from IE Painter Starter!")


def start_plugin() -> None:
    """Called by Substance Painter when plugin is loaded."""
    global _menu, _action

    try:
        _menu = ui.create_menu(MENU_NAME)
        _action = QtWidgets.QAction(ACTION_NAME)
        _action.triggered.connect(_on_click)
        _menu.addAction(_action)
        _log("Plugin loaded successfully")
    except Exception:
        _log("Failed to load plugin")
        _log(traceback.format_exc())


def close_plugin() -> None:
    """Called by Substance Painter when plugin is unloaded."""
    global _menu, _action, _dock

    try:
        if _action is not None:
            _action.triggered.disconnect(_on_click)
            _action = None

        if _menu is not None:
            ui.delete_ui_element(_menu)
            _menu = None

        if _dock is not None:
            ui.delete_ui_element(_dock)
            _dock = None

        _log("Plugin unloaded")
    except Exception:
        _log("Failed to unload plugin cleanly")
        _log(traceback.format_exc())
