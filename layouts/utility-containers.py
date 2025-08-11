"""
Textual comes with several "container" widgets. Among them, we have Vertical, Horizontal, and Grid which have the corresponding layout.

The example below shows how we can combine these containers to create a simple 2x2 grid. Inside a single Horizontal container, we place two Vertical containers. In other words, we have a single row containing two columns.
"""

from textual.app import App, ComposeResult
from textual.widgets import Static
from textual.containers import Horizontal, Vertical
from textual import events


class MyApp(App):

    CSS_PATH = "./tcss/util-container.tcss"

    def compose(self) -> ComposeResult:

        yield Horizontal(
            Vertical(Static("One", classes="column"), Static("Two", classes="column")),
            Vertical(
                Static("Three", classes="column"), Static("Four", classes="column")
            ),
        )

    def on_key(self, event: events.Key):
        if event.key == "q":
            self.exit()


if __name__ == "__main__":
    app = MyApp()
    app.run()
