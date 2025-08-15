"""
Action methods are methods on your app or widgets prefixed with action_.
Aside from the prefix these are regular methods which you could call directly if you wished
"""

from textual.app import App, ComposeResult
from textual import events


class MyApp(App):

    def action_set_background(self, color: str) -> None:
        self.screen.styles.background = color

    def on_key(self, event: events.Key) -> None:
        if event.key == "r":
            self.action_set_background("red")

        if event.key == "b":
            self.action_set_background("cornflowerblue")


if __name__ == "__main__":

    app = MyApp()
    app.run()
