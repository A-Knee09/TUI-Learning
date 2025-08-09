from textual.app import App, ComposeResult
from textual.events import Key
from textual.widgets import Button, Header, Label
from pathlib import Path


class MyApp(App[str]):

    CSS_PATH = Path("test.tcss")
    TITLE = "A Question App"
    SUB_TITLE = "The Most Important Question"

    def compose(self) -> ComposeResult:

        yield Header()
        yield Label("Do you love me?", id="question")
        yield Button("Yes :D", id="yes", variant="primary")
        yield Button("No  :(", id="no", variant="error")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.exit()

    def on_key(self, event: Key):
        self.title = event.key
        self.sub_title = f"You pressed the key {event.key}!"


if __name__ == "__main__":
    app = MyApp()
    reply = app.run()
    print(reply)
