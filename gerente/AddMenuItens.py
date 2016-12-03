from PyQt4.QtGui import *
from PyQt4 import QtGui
from PyQt4 import QtCore
from SnmpComm import *
from Dialog import *

class AddMenuItens(QWidget):
	def __init__(self):
		QWidget.__init__(self)
		outerLayout = QGridLayout()
		self.setLayout(outerLayout)

		font = QtGui.QFont("Helvetica")
		font.setPointSize(30)
		font.setBold(True)


		self.codLbl = QLabel("Code")
		self.codTxtEdit = QTextEdit("")
		self.nameLbl = QLabel("Name")
		self.nameTxtEdit = QTextEdit("")
		self.descLbl = QLabel("Desc")
		self.descTxtEdit = QTextEdit("")
		okBtn = QPushButton("Ok")
		okBtn.clicked.connect(self.okBtnClicked)
		cancelBtn = QPushButton("Cancel")
		cancelBtn.clicked.connect(self.cancelBtnClicked)

		self.codLbl.setFont(font)
		self.codTxtEdit.setFont(font)
		self.nameLbl.setFont(font)
		self.nameTxtEdit.setFont(font)
		self.descLbl.setFont(font)
		self.descTxtEdit.setFont(font)

		outerLayout.addWidget(self.codLbl,0,0)
		outerLayout.addWidget(self.codTxtEdit,0,1)
		outerLayout.addWidget(self.nameLbl,1,0)
		outerLayout.addWidget(self.nameTxtEdit,1,1)
		outerLayout.addWidget(self.descLbl,2,0)
		outerLayout.addWidget(self.descTxtEdit,2,1)
		outerLayout.addWidget(okBtn,3,0)
		outerLayout.addWidget(cancelBtn,3,1)

	def okBtnClicked(self):
		isItOk,message = self.checkInputs()
		if isItOk:	
			self.close()
		else:
			self.dialog = Dialog(message)
			self.dialog.show()

	def cancelBtnClicked(self):
		SnmpComm.get("mesasTable")
		self.close()

	def checkInputs(self):
		message = "lererer"
		return False,message

	



