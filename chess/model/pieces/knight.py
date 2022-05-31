"""Modèle un cavalier"""

from chess.model.pieces.piece import Piece

class Knight(Piece):
    """Classe Knight, hérité de Piece
    Attributs :
    - Couleur
    - Board
    - À bougé
    """

    def get_deplacements(self):
        """Liste des déplacement possible de la piece
        TODO
        """
