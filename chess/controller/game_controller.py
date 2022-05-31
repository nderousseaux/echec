"""Controller du projet
"""

from chess.model.colors_enum import Colors
from chess.model.board import Board

class Game():
    """Classe controlleur, appellée exclusivement par la vue

    Attributs :
     - board
     - line
     - winner
    """

    def __init__(self):
        """Crée simplement une nouvelle partie
        """
        self.board = None
        self.line = None
        self.winner = None

        self.new_game()

    def new_game(self):
        """Crée une nouvelle partie
        Crée un nouveau plateau, remet le trait au blanc et met le gagnant à None
        """
        self.board = Board()
        self.line = Colors.WHITE
        self.winner = None

    def resign(self, color):
        """L'utilisateur se résigne ou égalité
        """
        self.winner = color

    def move(self, move_to, move_from):
        """Demande le déplacement d'une piece
        - Vérifie que la piece qui bouge correspond au trait
        - Appelle Board:Move, qui vérifiera toutes les conditions liées à la disposition du plateau
        TODO
        """

    def get_deplacements(self, pos):
        """Renvoie la liste des déplacements possible pour
        la piece dont la position est en paramètre
        - Vérifie que la piece qui correspond au trait
        - Appelle Board:get_deplacements, qui vérifiera toutes
            les conditions liées à la disposition du plateau
        TODO
        """

    def get_piece(self, pos):
        """Renvoie la piece à la position indiquée en paramètres
        TODO
        """

    def get_chess(self):
        """Renvoie la position du roi en échec.
        Si le roi n'est pas en échec, renvoie None
        TODO
        """

    def move_list(self):
        """Renvoie la liste des mouvements pour la vue
        TODO
        """
        return ""
