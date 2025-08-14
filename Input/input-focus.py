"""

Only a single widget may receive key events at a time. The widget which is actively receiving key events is said to have input focus.

"""

from textual.app import App, ComposeResult
from textual import events
from textual.widgets import RichLog


class KeyLogger(RichLog):
    def on_key(self, event: events.Key) -> None:
        self.write(event)


class InputApp(App):

    CSS_PATH = "./tcss/input-focus.tcss"

    def compose(self) -> ComposeResult:

        yield KeyLogger(id="top-left")
        yield KeyLogger(id="top-right")
        yield KeyLogger(id="bottom-left")
        yield KeyLogger(id="bottom-right")

    def on_mount(self) -> None:

        top_left = self.query_one("#top-left")
        top_left.border_title = "Top Left Panel"

        top_right = self.query_one("#top-right")
        top_right.border_title = "Top Right Panel"

        bottom_left = self.query_one("#bottom-left")
        bottom_left.border_title = "Bottom Left Panel"

        bottom_right = self.query_one("#bottom-right")
        bottom_right.border_title = "Bottom right Panel"


if __name__ == "__main__":
    app = InputApp()
    app.run()
