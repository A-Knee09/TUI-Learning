from textual.app import App
from textual.widgets import Label, Button
from pathlib import Path


class MyApp(App[str]):

    CSS_PATH = Path("test.tcss")

    def compose(self):
        yield Label("Do you love Textual?", id="question")
        yield Button("Yes", id="yes", variant="primary")
        yield Button("No", id="no", variant="error")

    def on_button_pressed(self, event: Button.Pressed):
        self.exit(event.button.id)


if __name__ == "__main__":
    app = MyApp()
    reply = app.run()
    print(reply)
