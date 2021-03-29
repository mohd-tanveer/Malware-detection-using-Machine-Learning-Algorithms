# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QBrush, QColor, QPalette

from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize    
from PyQt5.QtWidgets import QFileDialog
from qroundprogressbar import QRoundProgressBar
from vp_file import *
#from cb4 import *
from percentage_window import *
import _pickle as cPickle


from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QColor, QPalette

     
class HomeWindow(QWidget):
    def __init__(self,parent=None):
#        super(HelloWindow, self).__init__(parent)
        QMainWindow.__init__(self,parent=None)
        self.setWindowFlags( QtCore.Qt.Window |  QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

        self.setFixedSize(QSize(800,500))    
#        self.setMinimumSize(QSize(800,500))
        global filebutton, folderbutton
        self.setWindowTitle("VP")
        self.file=[]
        self.folder=[]
        
#        centralWidget = QWidget(self)          
#        self.setCentralWidget(centralWidget)   
        
#        gridLayout = QGridLayout(self)     
#        centralWidget.setLayout(gridLayout) 
  
        
#home window code    
        filebutton = QPushButton('File', self)
        filebutton.clicked.connect(self.fileMethod)
        filebutton.resize(100,45)
#        filebutton.move(70, 70)  
        filebutton.move(480, 70) 

        
        folderbutton = QPushButton('Folder', self)
        folderbutton.clicked.connect(self.folderMethod)
        folderbutton.resize(100,45)
        folderbutton.move(600, 70) 
#        folderbutton.move(340, 70) 
#        folderbutton.setEnabled(False)
        
        resetbutton = QPushButton('Reset', self)
        resetbutton.clicked.connect(self.resetMethod)
        resetbutton.resize(100,45)
#        resetbutton.move(600, 70) 
        resetbutton.move(490, 360) 
        
        scanbutton = QPushButton('Scan', self)
        scanbutton.clicked.connect(self.scanMethod)
        scanbutton.resize(100,45)
        scanbutton.move(600, 360) 
        
        label = QLabel(self)
        pixmap = QPixmap('image/h2.jpg')
        label.setPixmap(pixmap)
        label.move(70,80)
        
        self.show()
        
#    def file_window(self):    
#        self.show()
#        print("Hello")
        
        
    
    
    def fileMethod(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","AllFIles(*);;Files (*.exe | *.dll | *.sys);", options=options)
        global file
        self.file=[]
        if files:
            print(files)
            self.file.append(files)
            folderbutton.setEnabled(False)
        print('file selected')
        
    def folderMethod(self):
        directory = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        global folder
        self.folder = []
        if directory:
            print(directory)
            self.folder.append(directory)
            filebutton.setEnabled(False)
        print('folder selected')
        
    def scanMethod(self):       
        print(self.file)
        print(self.folder)
        if(len(self.file)>0):         
            from one import classify
            pred=classify(0,self.file)
            print(pred)
            from vp_file import FileWindow
            self.i = FileWindow(self) 
            self.hide()
            self.i.show()
            
        if(len(self.folder)>0):
            from one import classify
            pred=classify(1,self.folder)
            print(pred)
            from percentage_window import Resolve
            self.a=Resolve(self)
            self.hide()
            self.a.show()
            
            
                
            
        print('scanned')
#        self.file_window()
#        if(len(self.file)==1):
        
        
#        if(len(self.folder==1)):
       
            
#        self.hide()
#        self.Window = FileWindow(self)
#        self.setWindowTitle("VP")
#        self.setCentralWidget(self.Window)
       
#        self.startFileWindow
#        self.show()
        
    def resetMethod(self):
         filebutton.setEnabled(True)
         folderbutton.setEnabled(True)
         self.folder=[]
         self.file=[]

        
            
        
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
        mainWin = HomeWindow()
        mainWin.show()
#        mainWin.home_window()
        app.exec_()
    run_app()