from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QPlainTextEdit, QPushButton, \
    QMessageBox, QGridLayout, QGroupBox, QLabel

boardSize = 15
win_admission = 5
board = list()
buttonsColumn = {}
buttonsBoard = {}

class TurnChecker:
    turn=1
    @classmethod
    def myMethod(cls):

        if(TurnChecker.turn%2):

            TurnChecker.turn = TurnChecker.turn + 1
            return str('X')
        else:

            TurnChecker.turn = TurnChecker.turn + 1
            return str("O")

class BoardCell(object):

    def coordinates(self, X, Y):
        #self.coordinates = '\n'+str(X)+ ' '+str(Y)+'\n' #for testing
        self.coordinates = '\n' +  ' '  + '\n'
        self.coordinateX = X
        self.coordinateY = Y
        self.discription = str(self.coordinateX)+' '+str(self.coordinateY)
        self.display = '-'
    def displayCoordinates(self):
        return str(self.coordinates)

    def activate_button_clicked_connection(self, layout, board): #dodane aby przekazać board i layout
        self.layout = layout
        self.board = board

    def cell_button_clicked(self):
        self.display = TurnChecker.myMethod()
        self.discription = '\n'+ str(self.display) + '\n'
        self.layout.addWidget(QPushButton(str(self.discription)),self.coordinateX,self.coordinateY) # tutaj jest problem bo nie wiadomo jak przekzazć layout

        WinConfirmer.rowAdmission(board)
        WinConfirmer.columnAdmission(board)
        WinConfirmer.cross1Admission(board)
        WinConfirmer.cross2Admission(board)

    def displayReturn(self):
        return self.display



class WinConfirmer:
    winAdmission = win_admission
    @classmethod
    def xWinConfirmation(cls):
        WinAlert.popUp('X win')
        widget.close()
    @classmethod
    def oWinConfirmation(cls):
        WinAlert.popUp('O win')
        widget.close()
    @classmethod
    def columnAdmission(cls, board): #column
        c=0
        for row in range(boardSize):

            a = 0
            for column in range(boardSize-(WinConfirmer.winAdmission-1)):
                b = 0
                winAdmissionFeedback = ''
                for winAdmissionLoop in range(WinConfirmer.winAdmission):
                    winAdmissionFeedback = winAdmissionFeedback + board[(a + b+ c*boardSize)].displayReturn()
                    if (winAdmissionFeedback == 'X' * WinConfirmer.winAdmission):
                        WinConfirmer.xWinConfirmation()
                        # zrobić break pętli
                    elif (winAdmissionFeedback == 'O' * WinConfirmer.winAdmission):
                        WinConfirmer.oWinConfirmation()
                        #zrobić break pętli
                    b = b + 1
                a = a + 1
            c= c + 1


    @classmethod
    def rowAdmission(cls, board):
        c = 0
        for row in range(boardSize):
            a = 0
            for column in range(boardSize-(WinConfirmer.winAdmission-1)):
                b = 0
                winAdmissionFeedback = ''
                for winAdmissionLoop in range(WinConfirmer.winAdmission):
                    winAdmissionFeedback = winAdmissionFeedback + board[(a*boardSize + b*boardSize + c)].displayReturn()
                    if (winAdmissionFeedback == 'X' * WinConfirmer.winAdmission):
                        WinConfirmer.xWinConfirmation()
                        #zrobić break pętli
                    elif (winAdmissionFeedback == 'O' * WinConfirmer.winAdmission):
                        WinConfirmer.oWinConfirmation()
                        #zrobić break pętli
                    b = b + 1
                a = a + 1
            c = c + 1

    @classmethod
    def cross1Admission(cls, board):
        c = 0
        for row in range(boardSize - (WinConfirmer.winAdmission-1)):
            a = 0
            for column in range(boardSize - (WinConfirmer.winAdmission-1)):
                b = 0
                winAdmissionFeedback = ''
                for winAdmissionLoop in range(WinConfirmer.winAdmission):
                    winAdmissionFeedback = winAdmissionFeedback + board[
                        (a * boardSize + b * (boardSize+1) + c)].displayReturn()
                    if (winAdmissionFeedback == 'X' * WinConfirmer.winAdmission):
                        WinConfirmer.xWinConfirmation()
                        # zrobić break pętli
                    elif (winAdmissionFeedback == 'O' * WinConfirmer.winAdmission):
                        WinConfirmer.oWinConfirmation()
                        # zrobić break pętli
                    b = b + 1
                    # print(winAdmissionFeedback)
                a = a + 1
            c = c + 1

    @classmethod
    def cross2Admission(cls, board):
        c = 0
        for row in range(boardSize - (WinConfirmer.winAdmission-1)):
            a = 0
            for column in range(boardSize - (WinConfirmer.winAdmission-1)):
                b = 0
                winAdmissionFeedback = ''
                for winAdmissionLoop in range(WinConfirmer.winAdmission):
                    winAdmissionFeedback = winAdmissionFeedback + board[
                        (a * boardSize + b * (boardSize - 1) + c+(WinConfirmer.winAdmission-1))].displayReturn()
                    if (winAdmissionFeedback == 'X' * WinConfirmer.winAdmission):
                        WinConfirmer.xWinConfirmation()
                        # zrobić break pętli
                    elif (winAdmissionFeedback == 'O' * WinConfirmer.winAdmission):
                        WinConfirmer.oWinConfirmation()
                        # zrobić break pętli
                    b = b + 1

                a = a + 1
            c = c + 1
class WinAlert:
    @classmethod
    def popUp(cls, winSide):
        popUp = QMessageBox()
        popUp.setWindowTitle(winSide)
        popUp.setText(winSide)
        popUp.exec_()


def play_button_clicked():

    widget.open()
    horizontalGroupBox2.close()



def exit_button_clicked():
    app2.quit()

def board_engine(boardSize, layout):

    y = 1
    for column in range(boardSize):
        x = 1
        for buttons in range(boardSize):
            board.append(BoardCell())  # creating each cell to display after click
            board[(y - 1) * boardSize + x - 1].coordinates(x, y)
            board[(y - 1) * boardSize + x - 1].displayCoordinates()
            buttonsColumn.update({x: QPushButton()})  # adding single button to column
            tempVar1 = board[(y - 1) * boardSize + x - 1].displayCoordinates()
            buttonsColumn[x] = QPushButton(tempVar1)  # defining discription on single button
            layout.addWidget(buttonsColumn[x], x, y)  # adding button to layout
            board[(y - 1) * boardSize + x - 1]. activate_button_clicked_connection(layout, board)
            buttonsColumn[x].clicked.connect(board[(y - 1) * boardSize + x - 1].cell_button_clicked)
            x = x + 1
        buttonsBoard.update({y: buttonsColumn})
        y = y + 1

    # layout.removeWidget(buttonsBoard[boardSize][boardSize])


class BoardWidget(QWidget):
    def __init__(self,boardSize):
        super().__init__()
        self.initUI(boardSize)

    def initUI(self,boardSize):
        self.layout = QGridLayout()
        self.setWindowTitle("Title!!")
        self.board_engine = board_engine(boardSize, self.layout)
        self.horizontalGroupBox = QGroupBox("tic tac toe")

        self.horizontalGroupBox.setLayout(self.layout)


    def close(self):
        self.horizontalGroupBox.close()

    def open(self):
        self.horizontalGroupBox.show()

app2 = QApplication([])

widget2 = QWidget()
widget2.setWindowTitle("Title!!")


horizontalGroupBox2 = QGroupBox("tic tac toe")
layout2 = QGridLayout()

buttonPlay = QPushButton('Play')
layout2.addWidget(buttonPlay, 1, 0)
buttonPlay.clicked.connect(play_button_clicked)
buttonClose = QPushButton('Close')
layout2.addWidget(buttonClose, 2, 0)
buttonClose.clicked.connect(exit_button_clicked)
widget = BoardWidget(boardSize)
horizontalGroupBox2.setLayout(layout2)
horizontalGroupBox2.show()

app2.exec_()










