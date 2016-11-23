from PyQt4.QtGui import *
from PyQt4 import QtGui
from PyQt4 import QtCore
from SnmpComm import *

class TablePopup(QWidget):
	def __init__(self,tableId):
		QWidget.__init__(self)
		layout = QVBoxLayout()
		self.setLayout(layout)	

		layoutGrid = QGridLayout()
		btnsLayout = QHBoxLayout()


		layout.addLayout(layoutGrid)
		layout.addLayout(btnsLayout)


		font = QtGui.QFont("Helvetica")
		font.setPointSize(30)
		font.setBold(True)


		#ID
		idTextLabel = QLabel("ID: ")
		idTextLabel.setFont(font)
		idTextLabel.setAlignment(QtCore.Qt.AlignCenter)

		idInfoLabel = QLabel(str(tableId))
		idInfoLabel.setFont(font)
		idInfoLabel.setAlignment(QtCore.Qt.AlignCenter)

		#Capacity
		capacityTextLabel = QLabel("Capacity: ")
		capacityTextLabel.setFont(font)
		capacityTextLabel.setAlignment(QtCore.Qt.AlignCenter)

		capacity = SnmpComm.getTable(tableId).capacity
		capacityTextEdit = QTextEdit(str(capacity))
		capacityTextEdit.setFont(font)
		capacityTextEdit.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter) #vertical align not working properlly
		capacityTextEdit.setMinimumSize(100,30)

		#Clients
		clientsTextLabel = QLabel("Clients: ")
		clientsTextLabel.setFont(font)
		clientsTextLabel.setAlignment(QtCore.Qt.AlignCenter)

		clients = SnmpComm.getTable(tableId).clients
		clientsTextEdit = QTextEdit(str(clients))
		clientsTextEdit.setFont(font)
		clientsTextEdit.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter) #vertical align not working properlly
		clientsTextEdit.setMinimumSize(100,30)

		#Status
		statusTextLabel = QLabel("Status: ")
		statusTextLabel.setFont(font)
		statusTextLabel.setAlignment(QtCore.Qt.AlignCenter)

		statusStr = SnmpComm.getTable(tableId).getStatusStr()
		statusTextEdit = QTextEdit(statusStr)
		statusTextEdit.setFont(font)
		statusTextEdit.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter) #vertical align not working properlly
		statusTextEdit.setMinimumSize(100,30)

		#buttons
		self.btnApply = QPushButton("Apply")
		self.btnApply.clicked.connect(lambda: self.handleButton("apply"))
		self.btnRefresh = QPushButton("Refresh")
		self.btnRefresh.clicked.connect(lambda: self.handleButton("refresh"))
		self.btnCancel = QPushButton("Cancel")
		self.btnCancel.clicked.connect(lambda: self.handleButton("cancel"))
		btnsLayout.addWidget(self.btnApply)
		btnsLayout.addWidget(self.btnRefresh)
		btnsLayout.addWidget(self.btnCancel)





		layoutGrid.addWidget(idTextLabel,1,1)
		layoutGrid.addWidget(idInfoLabel,1,2)
		layoutGrid.addWidget(capacityTextLabel,2,1)
		layoutGrid.addWidget(capacityTextEdit,2,2)
		layoutGrid.addWidget(clientsTextLabel,3,1)
		layoutGrid.addWidget(clientsTextEdit,3,2)
		layoutGrid.addWidget(statusTextLabel,4,1)
		layoutGrid.addWidget(statusTextEdit,4,2)



	def handleButton(self,function):
		if function == "apply":
			print "Apply"
		elif function == "refresh":
			print "refresh"
		elif function == "cancel":
			print "cancel"
			self.close()
		else:
			print "Unknown button"

