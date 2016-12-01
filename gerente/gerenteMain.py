import sys
import ExtendedQLabel
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtGui
from SnmpComm import *
from TablePopup import *

class Window(QtGui.QWidget):
    BUTTON_IMAGE_FREE = 'table-green.png'
    BUTTON_IMAGE_OCCUPIED = 'table-red.png'
    BUTTON_IMAGE_RESERVED = 'table-blue.png'
    BUTTON_IMAGE_UNAVAILABLE= 'table-black.png'
    tablePopup = None

    def __init__(self):
        super(Window, self).__init__()
        self.width = 800
        self.height = 300
        self.setGeometry(50, 50, self.width, self.height)
        self.setWindowTitle("Restaurant management")

        self.makeHome()

        self.show()

    def makeHome(self):
        #define layouts 
        vbox = QtGui.QVBoxLayout()
        northLayout = QtGui.QHBoxLayout()
        middleLayout = QtGui.QHBoxLayout()
        sideLayout = QtGui.QVBoxLayout()
        self.changeableLayout = QtGui.QVBoxLayout()
        

        font = QtGui.QFont("Helvetica")
        font.setPointSize(30)
        font.setBold(True)

        titleLabel = QLabel("Restaurant Management")
        titleLabel.setFont(font)
        self.setFixedWidgetSize(titleLabel,100,100)
        self.lotAtual = SnmpComm.getSnmpVar("lotAtual")
        self.capacidade = SnmpComm.getSnmpVar("capacidade")
        northLayout.addWidget(titleLabel)
        lotCapLabel = QLabel(self.lotAtual+"/"+self.capacidade)
        self.setFixedWidgetSize(lotCapLabel,100,100)
        lotCapLabel.setFont(font)
        lotCapLabel.setAlignment(QtCore.Qt.AlignRight)
        northLayout.addWidget(lotCapLabel)


        #sideLayout
        btnTables = QPushButton("Tables")
        btnTables.clicked.connect(lambda: self.menuButtonClicked("tables"))
        self.setFixedWidgetSize(btnTables,100,100)
        btnMenu = QPushButton("Menu")
        btnMenu.clicked.connect(lambda: self.menuButtonClicked("menu"))
        self.setFixedWidgetSize(btnMenu,100,100)
        btnOrders = QPushButton("Orders")
        btnOrders.clicked.connect(lambda: self.menuButtonClicked("orders"))
        self.setFixedWidgetSize(btnOrders,100,100)

        sideLayout.addWidget(btnTables)
        sideLayout.addWidget(btnMenu)
        sideLayout.addWidget(btnOrders)

        
        #layouts structure
        vbox.addLayout(northLayout)
        vbox.addLayout(middleLayout)
        middleLayout.addLayout(sideLayout)
        middleLayout.addLayout(self.changeableLayout)
        self.setLayout(vbox)

        self.showTablesFunction()

        #check update timer
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.updateInfo)
        timer.start(1000)

    def updateInfo(self):
        #check if any table has changed function
        newLotAtual = SnmpComm.getSnmpVar("lotAtual")
        newCapacidade = SnmpComm.getSnmpVar("capacidade")
        if newCapacidade != self.capacidade or newLotAtual != self.lotAtual:
            self.showTablesFunction()

        
    def showTablesFunction(self):
        self.clearLayout(self.changeableLayout)
        tablesGrid = QtGui.QGridLayout()
        self.changeableLayout.addLayout(tablesGrid)

        tablesGrid.setContentsMargins(10,10,10,10)
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
        while counter<int(self.capacidade):
            #create images and start event handlers
            self.tableButton.append(ExtendedQLabel.ExtendedQLabel(self))
            self.tableButton[counter].setId(counter)
            tableStatus = SnmpComm.getTableStatus(counter)
            if tableStatus == TableStatusEnum.Free:
                self.tableButton[counter].setPixmap(QPixmap(self.BUTTON_IMAGE_FREE))
            elif tableStatus == TableStatusEnum.Occupied:
                self.tableButton[counter].setPixmap(QPixmap(self.BUTTON_IMAGE_OCCUPIED))
            elif tableStatus == TableStatusEnum.Reserved:
                self.tableButton[counter].setPixmap(QPixmap(self.BUTTON_IMAGE_RESERVED))
            elif tableStatus == TableStatusEnum.Unavailable:
                self.tableButton[counter].setPixmap(QPixmap(self.BUTTON_IMAGE_UNAVAILABLE))
            self.tableButton[counter].setScaledContents(False)
            self.connect(self.tableButton[counter], SIGNAL('clicked()'), self.buttonClicked)
            #add the created imageButton to the grid
            tablesGrid.addWidget(self.tableButton[counter],j,i)
            counter = counter+1
            print str(i)+" "+str(j)
            if i > tablesPerLine:
                i = 0
                j = j+1
            else:
                i = i+1

    def buttonClicked(self):
        tableId = self.sender().id
        print('Button {0} Clicked'.format(tableId))
        if self.tablePopup is None:
            #cria objeto no primeiro acesso
            self.tablePopup = TablePopup(tableId)
        if self.tablePopup.apearing == True:
            print "fechando popup que tava aberta"
            self.tablePopup.close()
        print "Opening a new popup window..."
        self.tablePopup = TablePopup(tableId)
        self.tablePopup.setGeometry(QRect(100, 100, 400, 200))
        self.tablePopup.setWindowTitle("Table "+str(tableId)+" configuration")
        self.tablePopup.apearing = True
        self.tablePopup.show()

        
    def menuButtonClicked(self,function):
        if function is "tables":
            self.showTablesFunction()
        elif function is "menu":
            self.clearLayout(self.changeableLayout)
            self.changeableLayout.addWidget(QPushButton("oba oba"))
            print "lerere"
        elif function is "orders":
            print "orders"

        

    def clearLayout(self, layout):
        for i in reversed(range(layout.count())):
            item = layout.itemAt(i)

            if isinstance(item, QtGui.QWidgetItem):
                print "widget" + str(item)
                item.widget().close()
                # or
                # item.widget().setParent(None)
            elif isinstance(item, QtGui.QSpacerItem):
                print "spacer " + str(item)
                # no need to do extra stuff
            else:
                print "layout " + str(item)
                self.clearLayout(item.layout())

            # remove the item from layout
            layout.removeItem(item)    

    def setFixedWidgetSize(self,widget,width,height):
        widget.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run()