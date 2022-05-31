"""Modèle une piece"""

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
        TODO
        """
