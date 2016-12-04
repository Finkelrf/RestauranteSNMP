import sys
import ExtendedQLabel
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtGui
from SnmpComm import *
from TablePopup import *
from AddMenuItens import *
from RmMenuItens import *

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
        

        self.font = QtGui.QFont("Helvetica")
        self.font.setPointSize(30)
        self.font.setBold(True)

        titleLabel = QLabel("Restaurant Management")
        titleLabel.setFont(self.font)
        self.setFixedWidgetSize(titleLabel,100,100)
        self.lotAtual = SnmpComm.getSnmpVar("lotAtual")
        self.capacidade = SnmpComm.getSnmpVar("capacidade")
        northLayout.addWidget(titleLabel)
        lotCapLabel = QLabel(self.lotAtual+"/"+self.capacidade)
        self.setFixedWidgetSize(lotCapLabel,100,100)
        lotCapLabel.setFont(self.font)
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

    def showMenuFunction(self):
        self.clearLayout(self.changeableLayout)
        outerLayout = QVBoxLayout()
        self.changeableLayout.addLayout(outerLayout)

        #labels 
        labelsLayout = QHBoxLayout()

        codLabel = QLabel("Code")
        codLabel.setAlignment(QtCore.Qt.AlignCenter)
        nameLabel = QLabel("Name")
        nameLabel.setAlignment(QtCore.Qt.AlignCenter)
        descLabel = QLabel("Description")
        descLabel.setAlignment(QtCore.Qt.AlignCenter)
        labelsLayout.addWidget(codLabel)
        labelsLayout.addWidget(nameLabel)
        labelsLayout.addWidget(descLabel)
        outerLayout.addLayout(labelsLayout)

        #scroll area
        self.scrollArea = QtGui.QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtGui.QWidget(self.scrollArea)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 380, 247))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        outerLayout.addWidget(self.scrollArea)


        #info grid
        menuInfoGrid = QGridLayout(self.scrollAreaWidgetContents)
        outerLayout.addLayout(menuInfoGrid)
        cod = []
        name = []
        desc = []
        # cod.append(QLabel("Code"))
        # cod[0].setAlignment(QtCore.Qt.AlignCenter)
        # name.append(QLabel("Name"))
        # name[0].setAlignment(QtCore.Qt.AlignCenter)
        # desc.append(QLabel("Description"))
        # desc[0].setAlignment(QtCore.Qt.AlignCenter)
        # menuInfoGrid.addWidget(cod[0],0,0)
        # menuInfoGrid.addWidget(name[0],0,1)
        # menuInfoGrid.addWidget(desc[0],0,2)

        arrayOfValues = []
        listSize,arrayOfValues = SnmpComm.walk("menuTable")

        for i in range(1,listSize+1):
            cod.append(QLabel("Code"))
            cod[i].setAlignment(QtCore.Qt.AlignCenter)
            name.append(QLabel("Name"))
            name[i].setAlignment(QtCore.Qt.AlignCenter)
            desc.append(QLabel("Description"))
            desc[i].setAlignment(QtCore.Qt.AlignCenter)
            menuInfoGrid.addWidget(cod[i],i,0)
            menuInfoGrid.addWidget(name[i],i,1)
            menuInfoGrid.addWidget(desc[i],i,2)

        #add and remove menu buttons
        btnLayout = QHBoxLayout()
        outerLayout.addLayout(btnLayout)

        addMenuBtn = QPushButton("Add item")
        addMenuBtn.clicked.connect(self.addMenuItensClicked)
        rmvMenuBtn = QPushButton("Remove item")
        rmvMenuBtn.clicked.connect(self.rmMenuItensClicked)
        btnLayout.addWidget(addMenuBtn)
        btnLayout.addWidget(rmvMenuBtn)

    def addMenuItensClicked(self):
        self.addItens = AddMenuItens()
        self.addItens.setGeometry(QRect(100, 100, 400, 200))
        self.addItens.setWindowTitle("Add itens to menu")
        self.addItens.show()

    def rmMenuItensClicked(self):
        self.rmItens = RmMenuItens()
        self.rmItens.setGeometry(QRect(100, 100, 400, 100))
        self.rmItens.setWindowTitle("Add itens to menu")
        self.rmItens.show()







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
            # print str(i)+" "+str(j)
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
            self.showMenuFunction()
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