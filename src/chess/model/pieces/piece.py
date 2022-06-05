"""Modèle une piece"""

from chess.model import board as board_module

class Piece:
    """Classe abstraite piece
    Attributs :
    - Couleur
    - Board
    - À bougé
    """

    def __init__(self, color, board):
        """Crée la piece en définissant ses attributs
        """
        self.color = color
        self.board = board
        self.has_move = False


    def get_deplacements(self):
        """Liste des déplacement possible de la piece
        """

    def verify_move(self, move):
        """Vérifie si un mouvement est valide (ne sort pas du plateau)
        Renvoie la position absolue de la piece après mouvement
        """
        position = self.board.get_position(self)

        deplacement = [position[0]+move[0], position[1]+move[1]]

        #Si on sort du plateau, on arrête
        board_module.Board.coord_valid(deplacement)

        return deplacement

    def deplacements_list(self, moves):
        """Renvoie une liste de déplacement, en suivant une liste de mouvements possible
        """
        deplacements = []
        for move in moves:
            try:
                deplacements.append(self.verify_move(move))
            except ValueError:
                continue

        return deplacements

    def deplacements_one_direction(self, incr_x, incr_y):
        """Retourne une liste de déplacement, en suivant un incrément x/y en paramètre.
        S'arrête quand il rencontre un obstacle ou quand il sort du plateau
        """
        deplacements = []

        for i in range(1, 8):
            try:
                move = [incr_x*i, incr_y*i]
                deplacement = self.verify_move(move)

                deplacements.append(deplacement)

                #Si il y a un obstacle sur la route, on arrête
                if self.board.get_piece(deplacement) is not None:
                    raise ValueError("Obstacle sur la route")

            except ValueError:
                break

        return deplacements
    