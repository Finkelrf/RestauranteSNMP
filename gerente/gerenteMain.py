import sys
import ExtendedQLabel
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtGui
from SnmpComm import *
from TablePopup import *

class Window(QtGui.QWidget):
    BUTTON_IMAGE_FREE = 'table-green.png'
    BUTTON_IMAGE_OCUPY = 'table-red.png'
    BUTTON_IMAGE_RESERVED = 'table-blue.png'
    BUTTON_IMAGE_UNAVAILABLE= 'table-black.png'

    def __init__(self):
        super(Window, self).__init__()
        self.width = 800
        self.height = 600
        self.setGeometry(50, 50, self.width, self.height)
        self.setWindowTitle("Restaurant management")

        vbox = QtGui.QVBoxLayout()
        gridNorth = QtGui.QGridLayout()
        gridSouth = QtGui.QGridLayout()
        gridSouth.setContentsMargins(10,10,10,10)
        self.setLayout(vbox)
        vbox.addLayout(gridNorth)
        vbox.addLayout(gridSouth)

        title = QLabel("Restaurant Management")
        lotAtual = SnmpComm.getSnmpVar("lotAtual")
        capacidade = SnmpComm.getSnmpVar("capacidade")
        gridNorth.addWidget(title,1,1)
        lotCapLabel = QLabel(lotAtual+"/"+capacidade)
        gridNorth.addWidget(lotCapLabel,2,2)



        #formating tableMap
        tableWidth = 56
        tableheight = 56
        tableSpace = 20

        tablesPerLine = int(self.width/(tableWidth+tableSpace+tableSpace))
        print "tablesPerLine "+str(tablesPerLine)
        i = 0
        j = 0
        counter = 0
        self.tableButton = []
        while counter<int(capacidade):
            #create images and start event handlers
            self.tableButton.append(ExtendedQLabel.ExtendedQLabel(self))
            self.tableButton[counter].setId(counter)
            tableStatus = SnmpComm.getTableStatus(counter)
            if tableStatus == TableStatusEnum.Free:
                self.tableButton[counter].setPixmap(QPixmap(self.BUTTON_IMAGE_FREE))
            elif tableStatus == TableStatusEnum.Ocupy:
                self.tableButton[counter].setPixmap(QPixmap(self.BUTTON_IMAGE_OCUPY))
            elif tableStatus == TableStatusEnum.Reserved:
                self.tableButton[counter].setPixmap(QPixmap(self.BUTTON_IMAGE_RESERVED))
            elif tableStatus == TableStatusEnum.Unavailable:
                self.tableButton[counter].setPixmap(QPixmap(self.BUTTON_IMAGE_UNAVAILABLE))
            self.tableButton[counter].setScaledContents(False)
            self.connect(self.tableButton[counter], SIGNAL('clicked()'), self.buttonClicked)
            self.connect(self.tableButton[counter], SIGNAL('scroll(int)'), self.wheelScrolled)
            #add the created imageButton to the grid
            gridSouth.addWidget(self.tableButton[counter],j,i)
            counter = counter+1
            print str(i)+" "+str(j)
            if i > tablesPerLine:
                i = 0
                j = j+1
            else:
                i = i+1


        self.show()


    def close_application(self):
        print("whooaaaa so custom!!!")
        sys.exit()

    def buttonClicked(self):
        tableId = self.sender().id
        print('Button {0} Clicked'.format(tableId))
        print "Opening a new popup window..."
        self.tablePopup = TablePopup(tableId)
        self.tablePopup.setGeometry(QRect(100, 100, 400, 200))
        self.tablePopup.setWindowTitle("Table "+str(tableId)+" configuration")
        self.tablePopup.show()


    def wheelScrolled(self, scrollAmount):
        scrollAmount /= 10
        self.ImageButton.resize(self.ImageButton.width() + scrollAmount, self.ImageButton.height() + scrollAmount)
        self.resize(self.ImageButton.size())


def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run()