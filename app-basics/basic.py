"""
The first step in building a Textual app is to import the App class and create a subclass.
Event handlers are methods prefixed with on_ followed by the name of the event.
One such event is the mount event which is sent to an application after it enters application mode.
"""

from textual.app import App
from textual import events


class EventApp(App):

    COLORS = [
        "white",
        "maroon",
        "red",
        "purple",
        "fuchsia",
        "olive",
        "yellow",
        "navy",
        "teal",
        "aqua",
    ]

    def on_mount(self) -> None:
        """-> None is a function annotation, this means on_mount is a method that takes only self and returns nothing."""
        self.screen.styles.background = "darkblue"

    def on_key(self, event: events.Key) -> None:
        """This means that the event parameter is expected to be of type Key, and the function returns nothing"""
        if event.key.isdecimal():
            self.screen.styles.background = self.COLORS[int(event.key)]


if __name__ == "__main__":
    app = EventApp()
    app.run()
