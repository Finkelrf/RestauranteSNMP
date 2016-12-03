from PyQt4.QtGui import *
from PyQt4 import QtGui
from PyQt4 import QtCore


#TODO make it always on top
class Dialog(QWidget):
	def __init__(self,message):
		QWidget.__init__(self)
		outerlayout = QVBoxLayout()
		self.setLayout(outerlayout)
		msgLbl = QLabel(message)
		btn = QPushButton("ok")
		btn.clicked.connect(self.btnClicked)
		outerlayout.addWidget(msgLbl)
		outerlayout.addWidget(btn)


	def btnClicked(self):
		self.close()

