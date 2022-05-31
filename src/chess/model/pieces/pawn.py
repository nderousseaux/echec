"""Modèle un pion"""

from chess.model.colors_enum import Colors
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
        """
        position = self.board.get_position(self)

        deplacements = []

        direction = +1
        if self.color == Colors.BLACK:
            direction = -1

        moves_attack = [
            [position[0]-1, position[1]+(direction*1)],
            [position[0]+1, position[1]+(direction*1)],
        ]

        #Déplacement normal
        deplacement_base = [position[0], position[1]+(direction*1)]
        if self.board.get_piece(deplacement_base) is None:
            deplacements.append(deplacement_base)

        #Déplacement *2
        deplacement_two = [position[0], position[1]+(direction*2)]
        if (
            self.board.get_piece(deplacement_base) is None and
            self.board.get_piece(deplacement_two) is None and
            not self.has_move
        ):
            deplacements.append(deplacement_two)

        #Prise
        for move in moves_attack:
            piece = self.board.get_piece(move)
            if piece is not None and piece.color != self.color:
                deplacements.append(move)

        return deplacements
