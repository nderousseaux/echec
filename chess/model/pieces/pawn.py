"""Modèle un pion"""

from chess.model.pieces.piece import Piece

class Pawn(Piece):
    """Classe Pawn, hérité de Piece
    Attributs :
    - Couleur
    - Board
    - À bougé
    """

    def get_deplacements(self):
        """Liste des déplacement possible de la piece
        TODO
        """
