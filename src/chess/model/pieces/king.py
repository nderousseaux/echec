"""Modèlise un roi"""

from copy import deepcopy


from chess.model import board
from chess.model.colors_enum import Colors
from chess.model.pieces.piece import Piece
from chess.model.pieces.rook import Rook

class King(Piece):
    """Classe Rook, hérité de Piece
    Attributs :
    - Couleur
    - Board
    - has_move
    - À bougé
    """

    def get_deplacements(self, enable_rook=True):
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

        #Roque
        if enable_rook:
            #Si le roi n'a pas bougé et n'est pas en échec
            if not self.has_move and not self.is_chess():
                deplacements+=self.add_casteling_deplacements(is_right=True)
                deplacements+=self.add_casteling_deplacements(is_right=False)

        return deplacements

    def is_chess(self):
        """Teste si le roi est en échec
        """

        color_opponent = Colors.WHITE if self.color == Colors.BLACK else Colors.BLACK
        opponents_deplacements = []
        for opponent in self.board.get_pieces_color(color_opponent):
            if isinstance(opponent, King):
                opponents_deplacements+=opponent.get_deplacements(enable_rook=False)
            else:
                opponents_deplacements+=opponent.get_deplacements()

        if self.board.get_position(self) in opponents_deplacements:
            return True

        return False

    def add_casteling_deplacements(self, is_right=True):
        "Ajoute le déplacement 'roque' à la liste des déplacements du roi"
        x_rook = 7 if is_right else 0
        cases = [5,6] if is_right else [1,2,3]
        move = +2 if is_right else -2

        deplacements = []
        position = self.board.get_position(self)

        try:
            #Si la tour n'a pas bougée
            rook = self.board.get_piece([x_rook,position[1]])
            if not isinstance(rook, Rook) or rook.has_move:
                raise ValueError("La tour de gauche à bougée")

            for case in cases:
                deplacement = [case, position[1]]
                #Toutes les cases entre le roi et la tour sont vides
                if self.board.get_piece(deplacement) is not None:
                    raise ValueError("Obstacle sur la route")

                #On regarde si un déplacement du roi ici le mettrait en échec
                new_board = deepcopy(self.board)
                new_board.move(position, deplacement, test=True)
                king = new_board.get_king(self.color)
                if king.is_chess():
                    raise ValueError("Une pièce adverse contrôle la route")

            deplacements.append([position[0]+move, position[1]])
        except ValueError:
            pass

        return deplacements
        