"""Modèle une piece"""

from chess.model import board

class Piece:
    """Classe abstraite piece
    Attributs :
    - Couleur
    - Board
    - À bougé
    """

    def __init__(self, color, board):
        """Crée la piece en définissant ses attributs
        """
        self.color = color
        self.board = board
        self.has_move = False


    def get_deplacements(self):
        """Liste des déplacement possible de la piece
        """

    def deplacements_one_direction(self, incr_x, incr_y):
        """Retourne une liste de déplacement, en suivant un incrément x/y en paramètre.
        S'arrête quand il rencontre un obstacle ou quand il sort du plateau
        """
        deplacements = []

        position = self.board.get_position(self)
        for i in range(1, 8):
            try:
                deplacement = [position[0]+(incr_x*i), position[1]+(incr_y*i)]
                
                #Si on sort du plateau, on arrête
                board.Board.coord_valid(deplacement)

                deplacements.append(deplacement)

                #Si il y a un obstacle sur la route, on arrête
                if self.board.get_piece(deplacement) is not None:
                    raise ValueError("Obstacle sur la route")

            except ValueError:
                break

        return deplacements
    