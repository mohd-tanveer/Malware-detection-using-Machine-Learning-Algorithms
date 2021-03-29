    # -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 18:23:34 2018

@author: lenovo
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize    
from PyQt5.QtWidgets import QFileDialog
from qroundprogressbar import QRoundProgressBar
#from vp_file import *

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QColor, QPalette
from percentage_window import *
from home_window import *
import _pickle as cPickle


     
class FolderWindow(QWidget):
    def __init__(self,parent=None):
#        super(HelloWindow, self).__init__(parent)
        QMainWindow.__init__(self,parent=None)
        self.setWindowFlags( QtCore.Qt.Window |  QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

        self.setFixedSize(QSize(800,500))    
#        self.setMinimumSize(QSize(800,500))
     
        self.setWindowTitle("VP") 
        
         
        self.check_box()
        
        backbutton2 = QPushButton('back', self)
        backbutton2.setStyleSheet("background-image: url(image/back1.png);color: transparent;")
        backbutton2.clicked.connect(self.backMethod2)
        backbutton2.resize(60,36)
        backbutton2.move(30, 30)
        
        submitbutton = QPushButton('Submit', self)
#        submitbutton.setStyleSheet("background-image: url(image/back1.png);color: transparent;")
        submitbutton.clicked.connect(self.submitMethod)
        submitbutton.resize(60,36)
        submitbutton.move(680, 430)
        
        homebutton = QPushButton('Home', self)
#        submitbutton.setStyleSheet("background-image: url(image/back1.png);color: transparent;")
        homebutton.clicked.connect(self.homeMethod)
        homebutton.resize(60,36)
        homebutton.move(680, 30)
        
        ltext = QLabel(self)
        text= "Delete"
        ltext.setText(text)
        ltext.move(540,90) 
#        font = ltext.font()
#        font.setPixelSize(25)
#        ltext.setFont(font)
        
        
#        ltext = QLabel(self)
#        text= "Mark safe"
#        ltext.setText(text)
#        ltext.move(580,90) 
        
        
#        font = ltext.font()
#        font.setPixelSize(25)
#        ltext.setFont(font)
        
        
        
    def backMethod2(self):
        from percentage_window import Resolve
        self.c=Resolve(self)
        self.hide()
 
        self.c.show()   
        
    def submitMethod(self):
        from home_window import HomeWindow
        self.d=HomeWindow(self)
        self.hide()
        import os
        with open('delete.pkl', 'rb') as fid:
            delete= cPickle.load(fid)
        
        with open('folder.pkl', 'rb') as fid:
            folder= cPickle.load(fid)
         
        path=folder[0]
        for i in range(0,len(delete)):
            delete[i]=path+delete[i]
            ## if file exists, delete it ##
        for i in range(0,len(delete)):
            if os.path.isfile(delete[i]):
                os.remove(delete[i])
            else:    ## Show an error ##
                print("Error: %s file not found" % delete[i])
        self.d.show()
        
    def homeMethod(self):
        from home_window import HomeWindow

        self.e=HomeWindow(self)
        self.hide()
        self.e.show()        
        
        
                
    def check_box(self):  
        with open('folder.pkl', 'rb') as fid:
            folder= cPickle.load(fid)
         
        path=folder[0]
        list=folder[1][:]
        pred=folder[2]

        final_list=[]
        for i in range(0,len(pred)):
            if(pred[i]==1):
                final_list.append(list[i])
        global l,g,d,flag_d,flag_s,s,l1
        l=final_list
        g=l[:]
        l1=l[:]
        d=[]
        s=[]
        flag_d=[0]*len(l)
        flag_s=[0]*len(l)


    
        h=50
        for i in range(0,len(l)):
            
            l[i] = QPushButton(g[i]+'d', self)
            l[i].setCheckable(True)
            l[i].resize(20,20)
            l[i].move(550,70+h)
          
            l[i].clicked[bool].connect(self.selected)
#            l[i].setStyleSheet("background-color: black; color: black; ")
            l[i].setStyleSheet("background-image: url(image/uncheck.png);color: transparent;")
#            l[i].hide()
            
#            l1[i] = QPushButton(g[i]+'s', self)
#            l1[i].setCheckable(True)
#            l1[i].resize(20,20)
#            l1[i].move(580,70+h)
#          
#            l1[i].clicked[bool].connect(self.selected)
##            l[i].setStyleSheet("background-color: black; color: black; ")
#            l1[i].setStyleSheet("background-image: url(image/uncheck.png);color: transparent;")
            
            
            ltext = QLabel(self)
            text= g[i]
            ltext.setText(text)
            ltext.move(200,70+h)  
            font = ltext.font()
            font.setPixelSize(15)
            ltext.setFont(font)
            h=h+30



    def selected(self,pressed):
        
        source = self.sender()
#        m=[]
#        print(source.text)
        for i in range(0,len(g)):
            if source.text() == g[i]+'d':
                if(flag_d[i]==0):
                    d.append(g[i])
                    flag_d[i]=flag_d[i]+1
                    l[i].setStyleSheet("background-image: url(image/check.png); color: transparent;")

#                    l[i].setStyleSheet("background-color: black; ")
                else:
                    d.remove(g[i])
                    l[i].setStyleSheet("background-image: url(image/uncheck.png);color: transparent;")

#                    l[i].setStyleSheet("background-color: black color:none; ")
                    flag_d[i]=flag_d[i]-1  
                    
#        for i in range(0,len(g)):
#            if source.text() == g[i]+'s':
#                if(flag_s[i]==0):
#                    s.append(g[i])
#                    flag_s[i]=flag_s[i]+1
#                    l1[i].setStyleSheet("background-image: url(image/check.png); color: transparent;")
#
##                    l[i].setStyleSheet("background-color: black; ")
#                else:
#                    s.remove(g[i])
#                    l1[i].setStyleSheet("background-image: url(image/uncheck.png);color: transparent;")
#
##                    l[i].setStyleSheet("background-color: black color:none; ")
#                    flag_s[i]=flag_s[i]-1        
                    
                    
    
        
        
             
        
        print(d)
#        print("\n")
#        print(s)
        print("\n")
#        d=['a','b','c','d']
         
        with open('delete.pkl', 'wb') as fid:
            cPickle.dump(d, fid)
           
                
        
   
        
   
#        self.nd = FileWindow(self)    
#        self.nd.show()
#        self.close
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
        mainWin = FolderWindow()
        mainWin.show()
#        mainWin.home_window()
        app.exec_()
    run_app()