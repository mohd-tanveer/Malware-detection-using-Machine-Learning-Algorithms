# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 04:27:59 2018

@author: lenovo
"""
#def file_window(self):
#    print("Hello")

import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, 
    QLabel, QApplication)
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize    
from PyQt5.QtWidgets import QFileDialog
from qroundprogressbar import QRoundProgressBar

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QColor, QPalette
from home_window import *
#import home_window
import _pickle as cPickle



     
class FileWindow(QWidget):
    def __init__(self,parent=None):
        QMainWindow.__init__(self,parent=None)
#        self.setWindowFlags( QtCore.Qt.Window |  QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
#
        self.setFixedSize(QSize(800,500))  
        
        with open('file.pkl', 'rb') as fid:
            file= cPickle.load(fid)
        if(file[1][0]==0):
            predict=False
        else:
            predict=True
        if(predict):
            self.threat()
        else:
            self.safe()
        
        

        
        
    def threat(self):      
        label = QLabel(self)
        pixmap = QPixmap('image/image.png')
        label.setPixmap(pixmap)
        label.move(280,125)
       
        ltext = QLabel(self)
        text= "This file is predicted as infected. Do you want to delete it?"
        ltext.setText(text)
        ltext.move(80,380) 
        font = ltext.font()
        font.setPixelSize(25)
        ltext.setFont(font)
        
        ltext = QLabel(self)
        text= "Infected!!!"
        ltext.setText(text)
        ltext.move(320,30)  
        font = ltext.font()
        font.setPixelSize(40)
        ltext.setFont(font)
        ltext.setStyleSheet("color:red;")
        
        backbutton3 = QPushButton('Home', self)
        backbutton3.setStyleSheet("background-image: url(image/back1.png);color: transparent;")
        backbutton3.clicked.connect(self.backMethod3)
        backbutton3.resize(60,36)
        backbutton3.move(20, 20) 
        
        yesbutton = QPushButton('Yes', self)
        yesbutton.clicked.connect(self.yesMethod)
        yesbutton.resize(50,30)
        yesbutton.move(550, 440)   
        
        nobutton = QPushButton('No', self)
        nobutton.clicked.connect(self.noMethod)
        nobutton.resize(50,30)
        nobutton.move(650, 440)   
        
        self.show()
        
    def safe(self):
        label = QLabel(self)
        pixmap = QPixmap('image/safe.png')
        label.setPixmap(pixmap)
        label.move(300,160)
       
        ltext = QLabel(self)
        text= "This file is predicted as benign."
        ltext.setText(text)
        ltext.move(210,380) 
        font = ltext.font()
        font.setPixelSize(25)
        ltext.setFont(font)
        
        ltext = QLabel(self)
        text= "Safe!"
        ltext.setText(text)
        ltext.move(320,40)  
        font = ltext.font()
        font.setPixelSize(40)
        ltext.setFont(font)
        ltext.setStyleSheet("color:green;")

        
        backbutton3 = QPushButton('Home', self)
        backbutton3.setStyleSheet("background-image: url(image/back1.png);color: transparent;")
        backbutton3.clicked.connect(self.backMethod3)
        backbutton3.resize(60,36)
        backbutton3.move(20, 20)  
        
        self.show()
    
    def backMethod3(self):
        from home_window import HomeWindow

        self.f=HomeWindow(self)
        self.hide()
        self.f.show()   
        
    def yesMethod(self):
        from home_window import HomeWindow
        with open('file.pkl', 'rb') as fid:
            file= cPickle.load(fid)
        dfile=file[0][0]
        
        self.g=HomeWindow(self)
        self.hide()
        import os
        for i in range(0,len(dfile)):
            if os.path.isfile(dfile[i]):
                os.remove(dfile[i])
            else:    ## Show an error ##
                print("Error: %s file not found" % dfile[i])
        self.g.show() 
        
    def noMethod(self):
        from home_window import HomeWindow
        self.h=HomeWindow(self)
        self.hide()
        self.h.show() 
        
    
        
if __name__ == "__main__":
    def run_app():
        app = QtWidgets.QApplication(sys.argv)
        mainWin = FileWindow()
        mainWin.show()
#        mainWin.home_window()
        app.exec_()
    run_app()
        
#  