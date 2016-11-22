from PyQt4.QtGui import *
from PyQt4.QtCore import *

class ExtendedQLabel(QLabel):
    
    def __init(self, parent):
        QLabel.__init__(self, parent) 

    def setId(self,id):
    	self.id = id
     
    def mousePressEvent(self, ev):
        self.emit(SIGNAL('clicked()'))

    def wheelEvent(self, ev):
        self.emit(SIGNAL('scroll(int)'), ev.delta())