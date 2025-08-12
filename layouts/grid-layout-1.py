"""
To get started with grid layout, define the number of columns and rows in your grid with the grid-size CSS property and set layout: grid.
Widgets are inserted into the "cells" of the grid from left-to-right and top-to-bottom order.
"""

from textual.app import App, ComposeResult
from textual.widgets import Static


class GridApp(App):

    CSS_PATH = "./tcss/grid.tcss"

    def compose(self) -> ComposeResult:
        yield Static("One", classes="box")
        yield Static("Two", classes="box")
        yield Static("Three", classes="box")
        yield Static("Four", classes="box")
        yield Static("Five", classes="box")
        yield Static("Six", classes="box")


if __name__ == "__main__":
    app = GridApp()
    app.run()
