"""Modèlise le plateau
"""

class Board():
    """Classe représentant le plateau de jeu
    Attributs:
    - Dictionnaire des pieces (position:Piece)
    """

    @staticmethod
    def coord_valid(pos):
        """Teste si la position en paramètre est une position valide
        """

    def __init__(self):
        """Initialise le plateau
        Place les piece au bon endroit au début
        TODO
        """

    def get_position(self,piece):
        """Renvoie la position d'une piece
        TODO
        """

    def get_piece(self,pos):
        """Renvoie la piece à la position
        None si il n'y a pas de piece
        TODO
        """

    def get_deplacements(self, pos):
        """Renvoie la liste des déplacement possible pour la piece sur la case en paramètre
        - Appelle Piece:get_deplacement
        - Supprime les déplacement qui mettrait le roi adverse en échec
        TODO
        """

    def move(self, move_to, move_from):
        """Déplace la piece si le déplacement est dans la liste des déplacements possible
        TODO
        """
    