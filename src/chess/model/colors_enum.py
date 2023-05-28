"""Liste des couleurs"""

from enum import Enum

class Colors(Enum):
    """ Énumération des couleurs
    Le WHITE_AND_BLACK est utile en cas d'égalité
    """
    WHITE = 0
    BLACK = 1
    WHITE_AND_BLACK = 2
