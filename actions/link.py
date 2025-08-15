from textual.app import App, ComposeResult
from textual.widgets import Static


TEXT = """
[b] Set your background [/b]

[@click=app.set_background('red')] RED [/]
[@click=app.set_background('cornflowerblue')] Blue [/]
[@click=app.set_background('yellow')] Yellow [/]
"""


class ActionApp(App):

    def compose(self) -> ComposeResult:
        yield Static(TEXT)

    def action_set_background(self, color: str) -> None:
        self.screen.styles.background = color


if __name__ == "__main__":
    app = ActionApp()
    app.run()
