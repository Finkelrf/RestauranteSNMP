import sys
import ExtendedQLabel
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtGui
from SnmpComm import *
from TablePopup import *
from AddMenuItens import *
from RmMenuItens import *
from TrapHandler import *
from multiprocessing import Queue
from threading import Thread

class Window(QtGui.QWidget):
    BUTTON_IMAGE_FREE = 'table-green.png'
    BUTTON_IMAGE_OCCUPIED = 'table-red.png'
    BUTTON_IMAGE_RESERVED = 'table-blue.png'
    BUTTON_IMAGE_UNAVAILABLE= 'table-black.png'
    tablePopup = None
    mesasStatusList = []
    numMesas =0


    def __init__(self):
        super(Window, self).__init__()
        self.showingTables = 0
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
        self.lotAtual = SnmpComm.get("lotAtual.0")
        self.capacidade = SnmpComm.get("capacidade.0")
        northLayout.addWidget(titleLabel)
        self.lotCapLabel = QLabel(self.lotAtual+"/"+self.capacidade)
        self.setFixedWidgetSize(self.lotCapLabel,100,100)
        self.lotCapLabel.setFont(self.font)
        self.lotCapLabel.setAlignment(QtCore.Qt.AlignRight)
        northLayout.addWidget(self.lotCapLabel)

       

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

        #check if rest is open or closed
        statusRest = SnmpComm.get("status.0")
        if statusRest == "aberto(0)":
            btnText = "Open"
        else:
            btnText = "Closed"
        self.openClosedButton = QPushButton(btnText)
        self.setFixedWidgetSize(self.openClosedButton,100,100)
        self.openClosedButton.clicked.connect(self.openCloseBtnClicked)
        sideLayout.addWidget(self.openClosedButton)


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

        q = Queue()
        t1 = Thread(target = TrapHandler, args=(q,))
        t2 = Thread(target = self.trapListener, args=(q,))
        t1.start()
        t2.start()

    def trapListener(in_q):
        data = in_q.get()
        dial = Dialog(data)
        dial.show()

    def openCloseBtnClicked(self):
        statusRest = SnmpComm.get("status.0")
        if statusRest == "aberto(0)":
            SnmpComm.set("status.0","1")
            btnText = "Closed"
            self.openClosedButton.setStyleSheet('color: red;')
        else:
            SnmpComm.set("status.0","0")
            btnText = "Open"
            self.openClosedButton.setStyleSheet('color: black;')
        self.openClosedButton.setText(btnText)


    def updateInfo(self):
        #check if any table has changed function
        newLotAtual = SnmpComm.get("lotAtual.0")
        newCapacidade = SnmpComm.get("capacidade.0")
        if newCapacidade != self.capacidade or newLotAtual != self.lotAtual:
            self.lotAtual = newLotAtual
            self.capacidade  = newCapacidade
            self.lotCapLabel.setText(self.lotAtual+"/"+self.capacidade)
            if self.showingTables == 1:
                self.showTablesFunction()

    def showMenuFunction(self):
        self.showingTables = 0
        self.clearLayout(self.changeableLayout)
        outerLayout = QVBoxLayout()
        self.changeableLayout.addLayout(outerLayout)

        #labels 
        labelsLayout = QHBoxLayout()

        codLabel = QLabel("Code")
        codLabel.setAlignment(QtCore.Qt.AlignCenter)
        descLabel = QLabel("Description")
        descLabel.setAlignment(QtCore.Qt.AlignCenter)
        labelsLayout.addWidget(codLabel)
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
        desc = []


        arrayOfValues = []
        listSize,arrayOfValues = SnmpComm.walk("menuEntry.2")

        for i in range(0,listSize):
            cod.append(QLabel(str(i)))
            cod[i].setAlignment(QtCore.Qt.AlignCenter)
            desc.append(QLabel(arrayOfValues[i]))
            desc[i].setAlignment(QtCore.Qt.AlignCenter)
            menuInfoGrid.addWidget(cod[i],i,0)
            menuInfoGrid.addWidget(desc[i],i,1)

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
        self.showingTables = 1
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
        self.numMesas,self.mesasStatusList = SnmpComm.walk("mesasEntry.4")
        print str(self.numMesas)+" mesas no estabelescimento"
        print self.mesasStatusList
        while counter<int(self.numMesas):
            #create images and start event handlers
            self.tableButton.append(ExtendedQLabel.ExtendedQLabel(self))
            self.tableButton[counter].setId(counter)
            tableStatus = self.mesasStatusList[counter]
            if tableStatus == "livre(0)":
                self.tableButton[counter].setPixmap(QPixmap(self.BUTTON_IMAGE_FREE))
            elif tableStatus == "ocupada(1)":
                self.tableButton[counter].setPixmap(QPixmap(self.BUTTON_IMAGE_OCCUPIED))
            elif tableStatus == "reservada(2)":
                self.tableButton[counter].setPixmap(QPixmap(self.BUTTON_IMAGE_RESERVED))
            elif tableStatus == "indisponivel(3)":
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
        tableId = self.sender().id +1
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
            self.showOrdersFunction()
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


    def showOrdersFunction(self):
        self.showingTables = 0
        self.clearLayout(self.changeableLayout)
        outerLayout = QVBoxLayout()
        self.changeableLayout.addLayout(outerLayout)

        #labels 
        labelsLayout = QHBoxLayout()

        itemLabel = QLabel("Item")
        itemLabel.setAlignment(QtCore.Qt.AlignCenter)
        tableLabel = QLabel("Table")
        tableLabel.setAlignment(QtCore.Qt.AlignCenter)
        statusLabel = QLabel("Status")
        statusLabel.setAlignment(QtCore.Qt.AlignCenter)
        labelsLayout.addWidget(itemLabel)
        labelsLayout.addWidget(tableLabel)
        labelsLayout.addWidget(statusLabel)
        outerLayout.addLayout(labelsLayout)

        #scroll area
        self.scrollArea = QtGui.QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtGui.QWidget(self.scrollArea)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 380, 247))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        outerLayout.addWidget(self.scrollArea)


        #info grid
        ordersInfoGrid = QGridLayout(self.scrollAreaWidgetContents)
        outerLayout.addLayout(ordersInfoGrid)
        itens = []
        tables = []
        status = []


        itensList = []
        tablesList = []
        statusList = []
        listSize,itensList = SnmpComm.walk("ordersEntry.2")
        listSize,tablesList = SnmpComm.walk("ordersEntry.3")
        listSize,statusList = SnmpComm.walk("ordersEntry.4")

        for i in range(0,listSize):
            itemDesc = SnmpComm.get("menuEntry.2."+str(itensList[i]))
            itens.append(QLabel(itemDesc))
            itens[i].setAlignment(QtCore.Qt.AlignCenter)
            tables.append(QLabel(tablesList[i]))
            tables[i].setAlignment(QtCore.Qt.AlignCenter)
            status.append(QLabel(statusList[i]))
            status[i].setAlignment(QtCore.Qt.AlignCenter)
            ordersInfoGrid.addWidget(itens[i],i,0)
            ordersInfoGrid.addWidget(tables[i],i,1)
            ordersInfoGrid.addWidget(status[i],i,2)

        

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run()