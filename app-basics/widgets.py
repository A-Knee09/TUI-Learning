"""
To add widgets to your app implement a compose() method which should return an iterable of Widget instances
A list would work, but it is convenient to yield widgets, making the method a generator.
"""

from textual.app import App, ComposeResult
from textual import events
from textual.widgets import Welcome


class MyApp(App):

    def compose(self) -> ComposeResult:
        yield Welcome()

    def on_button_pressed(self) -> None:
        self.exit()


if __name__ == "__main__":
    myapp = MyApp()
    myapp.run()
