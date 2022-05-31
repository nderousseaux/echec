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
        """
        if self.winner != None:
            raise ValueError("La partie est finie")

        Board.coord_valid(move_to)
        Board.coord_valid(move_from)

        piece = self.board.get_piece(move_to)

        #On vérifie qu'il y a une pièce à l'emplacement
        if piece is None:
            raise ValueError("Il n'y a pas de pièce aux coordonnées indiquées")

        #On vérifie le trait
        if piece.color != self.line:
            raise ValueError("La couleur de la pièce n'est pas égale à la couleur du trait")

        self.board.move(move_to, move_from)

        #On teste si c'est echec et mat
        if not self.checkmate():
            if self.line == Colors.WHITE:
                self.line=Colors.BLACK
            else:
                self.line=Colors.WHITE
        else:
            self.winner = self.line

    def checkmate(self):
        """Vérifie si le joueur adverse est en échec et mat
        Si oui, il met à jour la variable winner
        """
        color_opponent = Colors.WHITE if self.line == Colors.BLACK else Colors.BLACK
        king = self.board.get_king(color_opponent)

        if king.is_chess():

            deplacements_opponents = []
            for opponent in self.board.get_pieces_color(color_opponent):
                deplacements_opponents+=self.board.get_deplacements(
                    self.board.get_position(opponent)
                )

            if len(deplacements_opponents) == 0:
                return True

        return False

    def get_deplacements(self, pos):
        """Renvoie la liste des déplacements possible pour
        la piece dont la position est en paramètre
        - Vérifie que la piece qui correspond au trait
        - Appelle Board:get_deplacements, qui vérifiera toutes
            les conditions liées à la disposition du plateau
        """
        Board.coord_valid(pos)

        #On vérifie qu'il y a une pièce à l'emplacement
        piece = self.board.get_piece(pos)
        if piece is None:
            raise ValueError("Il n'y a pas de pièce aux coordonnées indiquées")

        #On vérifie le trait
        if piece.color != self.line:
            raise ValueError("La couleur de la pièce n'est pas égale à la couleur du trait")

        return self.board.get_deplacements(pos)

    def get_piece(self, pos):
        """Renvoie la piece à la position indiquée en paramètres
        """
        Board.coord_valid(pos)

        return self.board.get_piece(pos)

    def get_chess(self):
        """Renvoie la position du roi en échec.
        Si le roi n'est pas en échec, renvoie None
        """
        king = self.board.get_king(self.line)
        if king.is_chess():
            return self.board.get_position(king)

        return None

    def move_list(self):
        """Renvoie la liste des mouvements pour la vue
        TODO
        """
        return ""
