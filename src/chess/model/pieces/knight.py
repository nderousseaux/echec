"""Modèlise un cavalier"""

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
        """
        deplacements = []
        moves = [[2,1],[1,2],[-1,2],[-2,1],[-2,-1],[-1,-2],[1,-2],[2,-1]]
        deplacements+=self.deplacements_list(moves)

        return deplacements
