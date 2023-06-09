"""Modèlise une tour"""

from chess.model.pieces.piece import Piece

class Rook(Piece):
    """Classe Rook, hérité de Piece
    Attributs :
    - Couleur
    - Board
    - À bougé
    """

    def get_deplacements(self):
        """Liste des déplacement possible de la piece
        """

        deplacements = []
        deplacements+=self.deplacements_one_direction(1,0)
        deplacements+=self.deplacements_one_direction(-1,0)
        deplacements+=self.deplacements_one_direction(0,1)
        deplacements+=self.deplacements_one_direction(0,-1)

        return deplacements
