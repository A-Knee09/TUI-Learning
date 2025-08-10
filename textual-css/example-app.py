from textual.app import App, ComposeResult
from textual.widgets import Header, Button, Footer, Static
from textual.containers import Container, Horizontal
from textual.screen import Screen

QUESTION = """Do you love textual ?"""


class YipeeScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Static("Yipee!", id="yipee-message")

    def on_key(self) -> None:
        self.app.pop_screen()  # Return to the previous screen


class MyApp(App):

    CSS_PATH = "example-app.tcss"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Container(
            Static(QUESTION, classes="question"),
            Horizontal(
                Button("Yes :D", variant="success", id="yes"),
                Button("No :(", variant="error", id="no"),
                classes="button",
            ),
            id="dialog",
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "yes":
            self.push_screen(YipeeScreen())  # Open the Yipee screen

        if event.button.id == "no":
            self.exit()


if __name__ == "__main__":
    app = MyApp()
    app.run()
