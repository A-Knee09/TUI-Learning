"""
Suspend the app to open another terminal app
"""

from textual.app import App, ComposeResult
from textual.widgets import Button, Label
from os import system
from textual import on


class SuspendingApp(App[None]):

    def compose(self) -> ComposeResult:
        yield Button("Open the editor", id="edit")

    @on(Button.Pressed, "#edit")
    def run_external_editor(self) -> None:
        with self.suspend():
            system("nano")


sp = SuspendingApp()
sp.run()
