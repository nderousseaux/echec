"""Modèle une dame"""

from chess.model.pieces.piece import Piece

class Queen(Piece):
    """Classe Queen, hérité de Piece
    Attributs :
    - Couleur
    - Board
    - À bougé
    """

    def get_deplacements(self):
        """Liste des déplacement possible de la piece
        TODO
        """
