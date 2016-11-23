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

		self.idInfoLabel = QLabel(str(tableId))
		self.idInfoLabel.setFont(font)
		self.idInfoLabel.setAlignment(QtCore.Qt.AlignCenter)

		#Capacity
		capacityTextLabel = QLabel("Capacity: ")
		capacityTextLabel.setFont(font)
		capacityTextLabel.setAlignment(QtCore.Qt.AlignCenter)

		capacity = SnmpComm.getTable(tableId).capacity
		self.capacityTextEdit = QTextEdit(str(capacity))
		self.capacityTextEdit.setFont(font)
		self.capacityTextEdit.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter) #vertical align not working properlly
		self.capacityTextEdit.setMinimumSize(100,30)

		#Clients
		clientsTextLabel = QLabel("Clients: ")
		clientsTextLabel.setFont(font)
		clientsTextLabel.setAlignment(QtCore.Qt.AlignCenter)

		clients = SnmpComm.getTable(tableId).clients
		self.clientsTextEdit = QTextEdit(str(clients))
		self.clientsTextEdit.setFont(font)
		self.clientsTextEdit.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter) #vertical align not working properlly
		self.clientsTextEdit.setMinimumSize(100,30)

		#Status
		statusTextLabel = QLabel("Status: ")
		statusTextLabel.setFont(font)
		statusTextLabel.setAlignment(QtCore.Qt.AlignCenter)

		statusStr = SnmpComm.getTable(tableId).getStatusStr()
		self.statusTextEdit = QTextEdit(statusStr)
		self.statusTextEdit.setFont(font)
		self.statusTextEdit.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter) #vertical align not working properlly
		self.statusTextEdit.setMinimumSize(100,30)

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
		layoutGrid.addWidget(self.idInfoLabel,1,2)
		layoutGrid.addWidget(capacityTextLabel,2,1)
		layoutGrid.addWidget(self.capacityTextEdit,2,2)
		layoutGrid.addWidget(clientsTextLabel,3,1)
		layoutGrid.addWidget(self.clientsTextEdit,3,2)
		layoutGrid.addWidget(statusTextLabel,4,1)
		layoutGrid.addWidget(self.statusTextEdit,4,2)



	def handleButton(self,function):
		if function == "apply":
			#TODO Fix status fazer barrinha com opcoes
			tableId = self.idInfoLabel.text()
			tableCapacity = self.capacityTextEdit.toPlainText()
			tableClients = self.clientsTextEdit.toPlainText()
			tableObj = Table(tableId,tableCapacity,tableClients,0)
			print str(tableId)+' '+str(tableCapacity)+' '+str(tableClients)
			SnmpComm.setTable(tableObj)
			print "Apply"
			self.close()
		elif function == "refresh":
			tableObj = SnmpComm.getTable(self.idInfoLabel.text())
			self.capacityTextEdit.setText(str(tableObj.capacity))
			self.capacityTextEdit.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter) #vertical align not working properlly
			self.clientsTextEdit.setText(str(tableObj.clients))
			self.clientsTextEdit.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter) #vertical align not working properlly
			statusStr = tableObj.getStatusStr()
			self.statusTextEdit.setText(statusStr)
			self.statusTextEdit.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter) #vertical align not working properlly
			print "refresh"
		elif function == "cancel":
			print "cancel"
			self.close()
		else:
			print "Unknown button"
