"""

Textual offers a convenient way of handling specific keys.
If you create a method beginning with key_ followed by the key name (the event's name attribute),
then that method will be called in response to the key press.

"""

from textual.app import App, ComposeResult
from textual import events
from textual.widgets import RichLog


class MyApp(App):
    """App to display key events"""

    def compose(self) -> ComposeResult:

        yield RichLog()

    def on_key(self, event: events.Key) -> None:
        self.query_one(RichLog).write(event)

    def key_space(self) -> None:
        self.bell()


if __name__ == "__main__":
    app = MyApp()
    app.run()
