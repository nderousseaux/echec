"""Modèle un fou"""

from chess.model.pieces.piece import Piece

class Bishop(Piece):
    """Classe Bishop, hérité de Piece
    Attributs :
    - Couleur
    - Board
    - À bougé
    """

    def get_deplacements(self):
        """Liste des déplacement possible de la piece
        """

        deplacements = []
        for i in [-1,1]:
            for j in [-1,1]:
                deplacements+=self.deplacements_one_direction(i,j)

        return deplacements
