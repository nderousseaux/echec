"""Main du projet
"""

from chess.controller.game_controller import Game
from chess.view.graphical_view import GraphicalView


if __name__ == "__main__":

    controller = Game()

    GraphicalView(controller)
