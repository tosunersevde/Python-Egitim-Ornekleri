# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 09:54:04 2022

@author: tosun
"""

import sys #uygulamalar komut satirindan calisacagi icin
from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import QApplication,QMainWindow,QToolTip
from PyQt5.QtGui import QIcon

class myWindow(QMainWindow):
    def __init__(self):
        super(myWindow,self).__init__()
        
        self.setWindowTitle("First Application")
        self.setGeometry(200,200,500,500) #╔yatay-dikey-boyut
        self.setWindowIcon(QIcon("icon.png")) #Pencere iconu
        self.setToolTip("my_tooltip")
        self.initUI()
        
    
        
    def initUI(self):
         self.lbl_name = QtWidgets.QLabel(self)
         self.lbl_name.setText("Adiniz")
         self.lbl_name.move(50,30) #konum
        
         self.lbl_surname = QtWidgets.QLabel(self)
         self.lbl_surname.setText("Soyadiniz")
         self.lbl_surname.move(50,70)
         
         self.lbl_result = QtWidgets.QLabel(self)
         ##self.lbl_result.setText("Sonuc:")
         self.lbl_result.resize(300,50)
         self.lbl_result.move(150,150)
        
         self.text_name = QtWidgets.QLineEdit(self)
         self.text_name.move(150,30)
         self.text_name.resize(200,32)
        
         self.text_surname = QtWidgets.QLineEdit(self)
         self.text_surname.move(150,70)
         self.text_surname.resize(200,32)
         
         self.btn_save = QtWidgets.QPushButton(self)
         self.btn_save.setText("Kaydet")
         self.btn_save.move(150,110)
         self.btn_save.clicked.connect(self.clicked)
         
    def clicked(self): #window elemanlarina erisim icin icinde tanimlandi
        #print("Butona tiklandi name: "+ self.text_name.text() + " surname: "+self.text_surname.text())
        self.lbl_result.setText("Ad: "+ self.text_name.text() + " Soyad: "+self.text_surname.text())


def window():
    app = QApplication(sys.argv)
    win = myWindow()

    win.show()
    sys.exit(app.exec_()) 
    
window()


"""def window():
    app = QApplication(sys.argv) #QtWidgets.QApplication
    win = QMainWindow() #pencere olusum
    
    win.setWindowTitle("First Application")
    win.setGeometry(200,200,500,500) #╔yatay-dikey-boyut
    win.setWindowIcon(QIcon("icon.png")) #Pencere iconu
    win.setToolTip("my_tooltip") #Mouse ile gezerken olusur.
    
    lbl_name = QtWidgets.QLabel(win)
    lbl_name.setText("Adiniz")
    lbl_name.move(50,30) #konum
    
    lbl_surname = QtWidgets.QLabel(win)
    lbl_surname.setText("Soyadiniz")
    lbl_surname.move(50,70)
    
    text_name = QtWidgets.QLineEdit(win)
    text_name.move(150,30)
    
    text_surname = QtWidgets.QLineEdit(win)
    text_surname.move(150,70)
    
    def clicked(self): #window elemanlarina erisim icin icinde tanimlandi
        print("Butona tiklandi name: "+ text_name.text() + "surname: "+text_surname.text())
    
    btn_save = QtWidgets.QPushButton(win)
    btn_save.setText("Kaydet")
    btn_save.move(150,110)
    btn_save.clicked.connect(clicked)
    
    win.show()
    sys.exit(app.exec_()) #x ile uygulama kapatma
    
window()"""