# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys
#from classifier import *
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize    
from PyQt5.QtWidgets import QFileDialog
from qroundprogressbar import QRoundProgressBar
from PyQt5.QtWidgets import QApplication, qApp

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QColor, QPalette
from final_window import *
from home_window import *
import _pickle as cPickle




    
class Resolve(QWidget):
    def __init__(self,parent=None):
        QMainWindow.__init__(self,parent=None)
        self.setWindowFlags( QtCore.Qt.Window |  QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

        self.setFixedSize(QSize(800,500))    
        self.setWindowTitle('VPS')
        
        
        with open('folder.pkl', 'rb') as fid:
            folder= cPickle.load(fid)
        sum=0
        for i in folder[2]:
            sum=sum+i
        percent=(sum/len(folder[2]))*100
        
        j=sum
        
        backbutton1 = QPushButton('Click me', self)
        backbutton1.setStyleSheet("background-image: url(image/back1.png);color: transparent;")
        backbutton1.clicked.connect(self.backMethod1)
        backbutton1.resize(60,36)
        backbutton1.move(30, 30)        
    
        resolvebutton = QPushButton('Resolve', self)
#        resolvebutton.setStyleSheet("background-image: url(image/back1.png);color: transparent;")
        resolvebutton.clicked.connect(self.resolveMethod)
        resolvebutton.resize(60,36)
        resolvebutton.move(680, 430)  
        if(percent==0):
            resolvebutton.setEnabled(False)
        ltext = QLabel(self)
        s=" files are infected do you want to resolve this?"
        s =str(j)+s
        text= s
        ltext.setText(text)
        ltext.move(80,380) 
        font = ltext.font()
        font.setPixelSize(25)
        ltext.setFont(font)
                
         
#Progressbar 
        i=percent
        progress = QRoundProgressBar(self)
        progress.setBarStyle(QRoundProgressBar.BarStyle.DONUT)
        progress.resize(200,200)
        progress.move(320,120)
        
        palette = QPalette()
        brush = QBrush(QColor(255, 105-i, 100-i))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush)
        progress.setPalette(palette)
        
       
        progress.setValue(i)
        qApp.processEvents()
        
        
        self.show()

    def backMethod1(self):
        from home_window import HomeWindow
        self.b=HomeWindow(self)
        self.hide()
        self.b.show()
        
        
    def resolveMethod(self):
        self.c=FolderWindow(self)
        self.hide()
        self.c.show()
        
    
#    
# 
#        title = QLabel("Hello World from PyQt", self) 
#        title.setAlignment(QtCore.Qt.AlignCenter)
#        gridLayout.addWidget(title, 0, 0)
#        
#        menu = self.menuBar().addMenu('Action for quit')
#        action = menu.addAction('Quit')
#        action.triggered.connect(QtWidgets.QApplication.quit)
 
if __name__ == "__main__":
  def run_app():
        app = QtWidgets.QApplication(sys.argv)
        mainWin = Resolve()
        mainWin.show()
#        mainWin.home_window()
        app.exec_()
  run_app()
    # -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 14:04:49 2018

@author: lenovo
"""

