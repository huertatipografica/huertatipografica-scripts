# MenuTitle: Python Package Manager
# -*- coding: utf-8 -*-

"""
Install or uninstall pip packages for Glyphs’ embedded Python (sys.prefix).
"""

import os
import subprocess
import sys
import threading

from PyObjCTools import AppHelper
from vanilla import Button, EditText, PopUpButton, TextEditor, Window

_window = None

_ACTION_LABELS = ("install", "uninstall")


def pip_run(action, package, log):
    python = os.path.join(sys.prefix, "bin", "python3")

    if not os.path.exists(python):
        log(f"❌ Python binary not found at: {python}")
        return

    log(f"🐍 Using Python: {python}")

    if action == "install":
        log(f"📦 Installing: {package}\n")
        cmd = [python, "-m", "pip", "install", package]
    elif action == "uninstall":
        log(f"🗑️  Uninstalling: {package}\n")
        cmd = [python, "-m", "pip", "uninstall", package, "-y"]
    else:
        log(f"❌ Unknown action: {action!r}. Use 'install' or 'uninstall'.")
        return

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.stdout:
        log(result.stdout.rstrip("\n"))
    if result.stderr:
        log(result.stderr.rstrip("\n"))

    if result.returncode == 0:
        log(f"✅ {package!r} {action}ed successfully!")
    else:
        log(f"❌ Failed to {action} {package!r} (exit code {result.returncode})")


class PipToolWindow:
    def __init__(self):
        self.w = Window((480, 420), "Pip (Glyphs Python)", minSize=(360, 280))

        self.w.actionPopup = PopUpButton((12, 12, -12, 20), list(_ACTION_LABELS))
        self.w.packageField = EditText((12, 40, -12, 22), "requests")
        self.w.runButton = Button((12, 72, -12, 24), "Run", callback=self.run_)
        self.w.output = TextEditor((12, 106, -12, -12), text="", readOnly=True)

        self.w.open()

    def append_log(self, message):
        current = self.w.output.get()
        if current:
            self.w.output.set(current + "\n" + message)
        else:
            self.w.output.set(message)

    def _log_async(self, message):
        AppHelper.callAfter(self.append_log, message)

    def run_(self, sender):
        self.w.output.set("")
        action = _ACTION_LABELS[self.w.actionPopup.get()]
        package = self.w.packageField.get().strip()
        if not package:
            self.append_log("❌ Enter a package name.")
            return

        def task():
            pip_run(action, package, self._log_async)

        threading.Thread(target=task, daemon=True).start()


def main():
    global _window
    _window = PipToolWindow()


if __name__ == "__main__":
    main()
