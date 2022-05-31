"""Modèle un cavalier"""

from chess.model.pieces.piece import Piece
from chess.model import board


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

        position = self.board.get_position(self)

        moves = [[2,1],[1,2],[-1,2],[-2,1],[-2,-1],[-1,-2],[1,-2],[2,-1]]
        for move in moves:
            try:
                deplacement = [position[0]+move[0], position[1]+move[1]]
                #Si on sort du plateau, on arrête
                board.Board.coord_valid(deplacement)

                deplacements.append(deplacement)

            except ValueError:
                continue

        return deplacements
