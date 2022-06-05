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
        """

        deplacements = []

        for i in [-1,0,1]:
            for j in [-1,0,1]:
                if i == 0 and j == 0:
                    continue

                deplacements+=self.deplacements_one_direction(i,j)

        return deplacements
