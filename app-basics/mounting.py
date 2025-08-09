"""
While composing is the preferred way of adding widgets when your app starts it is sometimes necessary to add new widget(s) in response to events. You can do this by calling mount() which will add a new widget to the UI.
"""

from textual.app import App, ComposeResult
from textual import events
from textual.widgets import Welcome


class MyApp(App):

    def on_key(self) -> None:
        self.mount(Welcome())

    def on_button_pressed(self) -> None:
        self.exit()


if __name__ == "__main__":
    myapp = MyApp()
    myapp.run()
