"""Modèle un roi"""

from chess.model.pieces.piece import Piece
from chess.model import board

class King(Piece):
    """Classe Rook, hérité de Piece
    Attributs :
    - Couleur
    - Board
    - has_move
    - À bougé
    """

    def get_deplacements(self):
        """Liste des déplacement possible de la piece
        """
        deplacements = []

        position = self.board.get_position(self)

        moves = [[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1]]
        for move in moves:
            try:
                deplacement = [position[0]+move[0], position[1]+move[1]]
                #Si on sort du plateau, on arrête
                board.Board.coord_valid(deplacement)

                deplacements.append(deplacement)

            except ValueError:
                continue


        return deplacements

    def is_chess(self):
        """Teste si le roi est en échec
        """

        opponents_deplacements = []
        for opponents in self.board.pieces:
            if opponents.color != self.color:
                opponents_deplacements+=opponents.get_deplacements()

        if self.board.get_position(self) in opponents_deplacements:
            return True

        return False
