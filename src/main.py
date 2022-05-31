from view.graphical_view import Graphical_view

class Controller():
    white_line = True
    
    winner = None

    move_list = [
        [[1,1],[1,5]],
        [[1,1],[1,5]],
        [[1,1],[1,5]],
        [[1,1],[1,5]]
    ]

    board = [
        {"type": "rook", "coord": [0,0], "isWhite": True},
        {"type": "knight", "coord": [1,0], "isWhite": True},
        {"type": "bishop", "coord": [2,0], "isWhite": True},
        {"type": "queen", "coord": [3,0], "isWhite": True},
        {"type": "king", "coord": [4,0], "isWhite": True},
        {"type": "bishop", "coord": [5,0], "isWhite": True},
        {"type": "knight", "coord": [6,0], "isWhite": True},
        {"type": "rook", "coord": [7,0], "isWhite": True},
        {"type": "pawn", "coord": [0,1], "isWhite": True},
        {"type": "pawn", "coord": [1,1], "isWhite": True},
        {"type": "pawn", "coord": [2,1], "isWhite": True},
        {"type": "pawn", "coord": [3,1], "isWhite": True},
        {"type": "pawn", "coord": [4,1], "isWhite": True},
        {"type": "pawn", "coord": [5,1], "isWhite": True},
        {"type": "pawn", "coord": [6,1], "isWhite": True},
        {"type": "pawn", "coord": [7,1], "isWhite": True},
        {"type": "rook", "coord": [0,7], "isWhite": False},
        {"type": "knight", "coord": [1,7], "isWhite": False},
        {"type": "bishop", "coord": [2,7], "isWhite": False},
        {"type": "queen", "coord": [3,7], "isWhite": False},
        {"type": "king", "coord": [4,7], "isWhite": False},
        {"type": "bishop", "coord": [5,7], "isWhite": False},
        {"type": "knight", "coord": [6,7], "isWhite": False},
        {"type": "rook", "coord": [7,7], "isWhite": False},
        {"type": "pawn", "coord": [0,6], "isWhite": False},
        {"type": "pawn", "coord": [1,6], "isWhite": False},
        {"type": "pawn", "coord": [2,6], "isWhite": False},
        {"type": "pawn", "coord": [3,6], "isWhite": False},
        {"type": "pawn", "coord": [4,6], "isWhite": False},
        {"type": "pawn", "coord": [5,6], "isWhite": False},
        {"type": "pawn", "coord": [6,6], "isWhite": False},
        {"type": "pawn", "coord": [7,6], "isWhite": False},
    ]

    def get(self, i, j):
        for p in self.board:
            if p["coord"][0] == i and p["coord"][1]==j:
                return p
        return None

    def new_game(self):
        self.winner=None
        self.white_line = True
        print("newGame")

    def import_pgn(self, pgn):
        print(pgn)

    def input_move(self, coord_from, coord_to):
        try:            
            self.get(coord_from[0],coord_from[1])["coord"] = coord_to
            self.white_line = not self.white_line 
        except Exception:
            pass
        print("Move {} to {}".format(coord_from, coord_to))

    def possibles_moves(self, coord_from):
        return [
         [3,0],
         [3,1],
         [3,2],
         [3,3],
         [3,4],
         [3,5],
         [3,6],
         [3,7]
        ]
    
    def resign(self, is_white):
        self.winner = is_white

    def echec(self):
        return [2,4]

    



if __name__ == "__main__":

    c = Controller()

    Graphical_view(c)


