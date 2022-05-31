import PySimpleGUI as sg
import os

CHESS_PATH = './img'
ICON_PATH = CHESS_PATH+'/queenb.ico'

LOOK = "SystemDefaultForReal"

blank = os.path.join(CHESS_PATH, 'blank.png')
bishopB = os.path.join(CHESS_PATH, 'bishopb.png')
bishopW = os.path.join(CHESS_PATH, 'bishopw.png')
pawnB = os.path.join(CHESS_PATH, 'pawnb.png')
pawnW = os.path.join(CHESS_PATH, 'pawnw.png')
knightB = os.path.join(CHESS_PATH, 'knightb.png')
knightW = os.path.join(CHESS_PATH, 'knightw.png')
rookB = os.path.join(CHESS_PATH, 'rookb.png')
rookW = os.path.join(CHESS_PATH, 'rookw.png')
queenB = os.path.join(CHESS_PATH, 'queenB.png')
queenW = os.path.join(CHESS_PATH, 'queenW.png')
kingB = os.path.join(CHESS_PATH, 'kingb.png')
kingW = os.path.join(CHESS_PATH, 'kingw.png')

images = {"bishopB": bishopB, "bishopW": bishopW, "pawnB": pawnB, "pawnW": pawnW, "knightB": knightB, "knightW": knightW,
          "rookB": rookB, "rookW": rookW, "kingB": kingB, "kingW": kingW, "queenB": queenB, "queenW": queenW, "blank":blank}

DARK_CASE = "#F0D9B5"
LIGHT_CASE = "#B58863"
POSSIBLE_DARK_CASE = '#B8B1A7'
POSSIBLE_LIGHT_CASE = '#99806B'

class Graphical_view():

    def get_image(self, piece):
        """Renvoie l'image correspondant a la piece en paramètre
        """
        if piece == None:
            return images["blank"]
        
        return images[piece["type"] + ("W" if piece["isWhite"] else "B")]        

    def new_game(self):
        self.controller.new_game()
        self.disable_buttons(False)
        self.window["subtitle"].Update("Line : {}".format("white" if self.controller.white_line else "black"))

    def open_pgn(self):
        filename = sg.PopupGetFile('', no_window=True)
        if filename is not None:
            with open(filename) as f:
                lines = f.readlines()

            self.controller.import_pgn(lines);

    def move(self, coord):
        """Bouge une pièce
        """
        #On sélectionne une pièce
        if self.move_from == None:
            self.set_move_from(coord)
            
        #On choisi ou elle va
        else:
            self.set_move_to(coord)

    def set_move_from(self, coord):
        """Sélectionne la pièce à bouger
        """
        piece = self.controller.get(coord[0], coord[1])
        if piece != None and piece["isWhite"] == self.controller.white_line:
            self.move_from = coord
            self.possibles_moves = self.controller.possibles_moves(self.move_from)

    def set_move_to(self, coord):
        """Sélectionne la destination de la piece
        """
        self.move_to = coord

        if self.move_from != self.move_to: 
            self.controller.input_move(self.move_from, self.move_to)

        self.move_from = None
        self.move_to = None
        self.possibles_moves = []

    def disable_buttons(self, disabled):
        """Active/desactive les bouttons de jeu
        """
        self.window["Resign - White"].update(disabled=disabled)
        self.window["Resign - Black"].update(disabled=disabled)
        self.window["Draw"].update(disabled=disabled)
        for i in range(8):
            for j in range(8):
                self.window[(i,j)].update(disabled=disabled)

    def draw_board(self):
        winner = self.controller.winner

        self.window["move_list"].update(self.controller.move_list)

        if  winner == None:
            for i in range(8):
                for j in range(8):
                    piece_image = self.get_image(self.controller.get(i, j))
                    #Ma pièce
                    if (i,j) == self.move_from:
                        color = 'green'

                    #Coups possible
                    elif [i,j] in self.possibles_moves:
                        color = POSSIBLE_DARK_CASE if (i + j) % 2 else POSSIBLE_LIGHT_CASE
                    
                    #Echec
                    elif [i,j] == self.controller.echec():
                        color = 'red'

                    #Cas normal
                    else:
                        color =  DARK_CASE if (i + j) % 2 else LIGHT_CASE
                                        
                    self.window[(i,j)].Update(button_color=('white', color),
                            image_filename=piece_image, )

            self.window["subtitle"].Update("Line : {}".format("white" if self.controller.white_line else "black"))
        else:
            if type(winner) == bool:
                winner_str = "white" if winner else "black"
            else:
                winner_str = "white and black"
            
            info_str = 'The winner is : {}'.format(winner_str)
            sg.Popup(info_str, icon=ICON_PATH,title="Winner !")
            self.window["subtitle"].Update(info_str)

            #On désactive tout les boutons
            self.disable_buttons(True)
            

    def resign(self,is_white):
        self.controller.resign(is_white)
                

    def loop_input(self):
        """Boucle sur les entrées utilisateur
        """
        while True:
            self.draw_board()

            button, value = self.window.Read()
            if button in (None, 'Exit'):
                break
            if button == 'New Game':
                self.new_game()
            if button == "Open PGN":
                self.open_pgn()  
            if button == "Resign - White":
                self.resign(True)
            if button == "Resign - Black":
                self.resign(False)
            if button == "Draw":
                self.resign([True, False])

            if type(button) is tuple: #Si c'est une case
                self.move(button)

    def __init__(self, controller):
        self.controller = controller
        self.move_from = None
        self.move_to = None
        self.possibles_moves = []

        sg.ChangeLookAndFeel(LOOK)

        #On dessine le plateau
        board_layout = [[sg.T('          ')] + [sg.T('{}'.format(a), pad=((29,27),0), font='Any 13') for a in 'abcdefgh']]
        for i in range(8):
            row = [sg.T(str(8-i)+'    ', font='Any 13')]
            for j in range(8):
                image = self.get_image(self.controller.get(j, 7-i))
                color = DARK_CASE if (7-i + j) % 2 else LIGHT_CASE
                case = sg.RButton('', image_filename=image, size=(1, 1), button_color=('white', color), pad=(0, 0), key=(j, 7-i))
                row.append(case)
            row.append(sg.T(str(8-i)+'    ', font='Any 13'))
            board_layout.append(row)
        board_layout.append([sg.T('          ')] + [sg.T('{}'.format(a), pad=((29,27),0), font='Any 13') for a in 'abcdefgh'])
        


        #On règle les boutons à droite
        board_controls = [
            [sg.RButton('New Game'), sg.RButton('Open PGN')],
            [sg.RButton('Resign - White'), sg.RButton('Resign - Black')],
            [sg.RButton('Draw')],
            [sg.Text('Move List')],
            [sg.Multiline([], do_not_clear=True, autoscroll=True, size=(30,40),key='move_list')],]

        # the main window layout
        layout = [
            [
                sg.Column(board_layout),
                sg.Column(board_controls)
            ],
            [sg.Text("", font='_ 14', key="subtitle")]]

        self.window = sg.Window('Chess', default_button_element_size=(12,1), auto_size_buttons=False, icon=ICON_PATH, finalize=True).Layout(layout)
        self.window.finalize()
        self.new_game()

        self.loop_input()
