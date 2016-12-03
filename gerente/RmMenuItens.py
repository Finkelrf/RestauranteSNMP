from PyQt4.QtGui import *
from PyQt4 import QtGui
from PyQt4 import QtCore
from SnmpComm import *

class RmMenuItens(QWidget):
	def __init__(self):
		QWidget.__init__(self)
		outerLayout = QVBoxLayout()
		self.setLayout(outerLayout)
		northLayout = QHBoxLayout()
		outerLayout.addLayout(northLayout)

		font = QtGui.QFont("Helvetica")
		font.setPointSize(30)
		font.setBold(True)

		self.codLbl = QLabel("Code")
		self.codTxtEdit = QTextEdit("")
		self.codLbl.setFont(font)
		self.codTxtEdit.setFont(font)
		northLayout.addWidget(self.codLbl)
		northLayout.addWidget(self.codTxtEdit)

		btn = QPushButton("Remove Item")
		btn.clicked.connect(self.btnClicked)

		outerLayout.addWidget(btn)



	def btnClicked(self):
		print "btn clicked"
