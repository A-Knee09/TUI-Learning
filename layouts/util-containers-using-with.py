"""
Context managers in Python are like "setup → do something → cleanup" helpers that make sure resources are properly prepared and released, even if an error happens in between.

A context manager is any object that implements two special methods:
1. __enter__() → runs when you enter the with block
2. __exit__() → runs when you leave it (even if there’s an error)

`with self.suspend():` ,suspend() is a context manager,
        Setup -> Pause the TUI,
        Do Something -> Run Nano,
        Cleanup -> Resume TUI once nano exits
"""

from textual.app import App, ComposeResult
from textual.widgets import Static
from textual.containers import Horizontal, Vertical
from textual import events


class MyApp(App):

    CSS_PATH = "./tcss/with-container.tcss"

    def compose(self) -> ComposeResult:

        with Horizontal():
            with Vertical(classes="column"):
                yield Static("One")
                yield Static("Two")

            with Vertical(classes="column"):
                yield Static("Three")
                yield Static("Four")

    def on_key(self, event: events.Key):
        if event.key == "q":
            self.exit()


if __name__ == "__main__":
    app = MyApp()
    app.run()
