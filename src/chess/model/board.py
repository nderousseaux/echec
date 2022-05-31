"""Modèlise le plateau
"""
from copy import deepcopy

from chess.model.pieces import Bishop, King, Knight, Pawn, Queen, Rook
from chess.model.colors_enum import Colors

class Board():
    """Classe représentant le plateau de jeu
    Attributs:
    - Dictionnaire des pieces (position:Piece)
    """

    @staticmethod
    def coord_valid(pos):
        """Teste si la position en paramètre est une position valide
        """
        if (
            not isinstance(pos, list) or
            len(pos) != 2 or
            pos[0] < 0 or
            pos[0] > 7 or
            pos[1] < 0 or
            pos[1] > 7
        ):
            raise ValueError("La position n'est pas valide")

    def __init__(self, pieces=None):
        """Initialise le plateau
        Place les piece au bon endroit au début
        """

        if pieces is None:
            # self.pieces = {
            #     Rook(Colors.WHITE, self): [0,0],
            #     Knight(Colors.WHITE, self): [1,0],
            #     Bishop(Colors.WHITE, self): [2,0],
            #     Queen(Colors.WHITE, self): [3,0],
            #     King(Colors.WHITE, self): [4,0],
            #     Bishop(Colors.WHITE, self): [5,0],
            #     Knight(Colors.WHITE, self): [6,0],
            #     Rook(Colors.WHITE, self): [7,0],
            #     Pawn(Colors.WHITE, self): [0,1],
            #     Pawn(Colors.WHITE, self): [1,1],
            #     Pawn(Colors.WHITE, self): [2,1],
            #     Pawn(Colors.WHITE, self): [3,1],
            #     Pawn(Colors.WHITE, self): [4,1],
            #     Pawn(Colors.WHITE, self): [5,1],
            #     Pawn(Colors.WHITE, self): [6,1],
            #     Pawn(Colors.WHITE, self): [7,1],

            #     Rook(Colors.BLACK, self): [0,7],
            #     Knight(Colors.BLACK, self): [1,7],
            #     Bishop(Colors.BLACK, self): [2,7],
            #     Queen(Colors.BLACK, self): [3,7],
            #     King(Colors.BLACK, self): [4,7],
            #     Bishop(Colors.BLACK, self): [5,7],
            #     Knight(Colors.BLACK, self): [6,7],
            #     Rook(Colors.BLACK, self): [7,7],
            #     Pawn(Colors.BLACK, self): [0,6],
            #     Pawn(Colors.BLACK, self): [1,6],
            #     Pawn(Colors.BLACK, self): [2,6],
            #     Pawn(Colors.BLACK, self): [3,6],
            #     Pawn(Colors.BLACK, self): [4,6],
            #     Pawn(Colors.BLACK, self): [5,6],
            #     Pawn(Colors.BLACK, self): [6,6],
            #     Pawn(Colors.BLACK, self): [7,6]
            # }
            self.pieces = {                
                King(Colors.WHITE, self): [0,0],
                Queen(Colors.WHITE, self): [0,6],
                Queen(Colors.WHITE, self): [1,0],
                King(Colors.BLACK, self): [7,7],
            }
        else:
            self.pieces = pieces

    def get_position(self,piece):
        """Renvoie la position d'une piece
        """

        return self.pieces[piece]

    def get_piece(self,pos):
        """Renvoie la piece à la position
        None si il n'y a pas de piece
        """

        for key, value in self.pieces.items():
            if value == pos:
                return key

        return None

    def get_pieces_color(self, color):
        """Récupérer les piéces d'une certaine couleur
        """
        return [piece for piece in self.pieces if piece.color == color]

    def get_king(self, color):
        """Renvoie le roi de la couleur en paramètre
        """
        for key in self.pieces:
            if isinstance(key, King) and key.color == color:
                return key

    def get_deplacements(self, pos):
        """Renvoie la liste des déplacements possibles pour la piece sur la case en paramètre
        - Appelle Piece:get_deplacements
        - Supprime les déplacements sur un allié
        - Supprime les déplacements qui mettrait le roi adverse en échec
        """
        Board.coord_valid(pos)

        #On vérifie qu'il y a une pièce à l'emplacement
        piece = self.get_piece(pos)
        if piece is None:
            raise ValueError("Il n'y a pas de pièce aux coordonnées indiquées")

        #On appelle piece deplacement
        deplacements = piece.get_deplacements()

        #On supprime les déplacements sur un allié
        deplacements_new = []
        for deplacement in deplacements:
            piece_dest = self.get_piece(deplacement)
            if piece_dest is None or piece_dest.color != piece.color:
                deplacements_new.append(deplacement)

        deplacements = deplacements_new

        #On supprime les déplacements qui mettraient notre roi en échec
        deplacements_new = []
        for deplacement in deplacements:
            new_board = deepcopy(self)

            #On fait le mouvement
            new_board.move(pos, deplacement, test=True)

            #Si le roi n'est pas en échec, on garde le mouvement
            king = new_board.get_king(piece.color)
            if not king.is_chess():
                deplacements_new.append(deplacement)

        deplacements = deplacements_new

        return deplacements

    def move(self, move_to, move_from, test=False):
        """Déplace la piece si le déplacement est dans la liste des déplacements possible
        """
        Board.coord_valid(move_to)
        Board.coord_valid(move_from)

        #On vérifie qu'il y a une pièce à l'emplacement
        piece = self.get_piece(move_to)
        position = self.get_position(piece)
        if piece is None:
            raise ValueError("Il n'y a pas de pièce aux coordonnées indiquées")

        if not test:
            if move_from not in self.get_deplacements(move_to):
                raise ValueError("La pièce n'a pas le droit de se déplacer ici")

        #Si il y a une piece à l'arrivée, on la mange
        piece_from = self.get_piece(move_from)
        if piece_from is not None:
            del self.pieces[piece_from]


        #Si c'est un roque
        if isinstance(piece, King) and not piece.has_move and move_from[0] in [2,6]:
            #Roque de gauche
            if move_from[0] == 2:
                rook = self.get_piece([0,position[1]])
                self.pieces[rook] = [3,position[1]]
            #Roque de gauche
            elif move_from[0] == 6:
                rook = self.get_piece([7,position[1]])
                self.pieces[rook] = [5,position[1]]
            rook.has_move = True

        #On bouge la pièce
        self.pieces[piece] = move_from
        piece.has_move = True
