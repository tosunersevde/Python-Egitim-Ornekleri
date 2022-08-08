# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 20:58:29 2022

@author: tosun
"""
#%%
#Layout olsturma
import sys 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow
from PyQt5.QtGui import QPalette,QColor

class Color(QWidget):
    def __init__(self,color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True) #arkapaln boyama
        
        palette = self.palette()
        palette.setColor(QPalette.Window,QColor(color))
        self.setPalette(palette)
        
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(100,100,500,500)
        
        #layout = QtWidgets.QVBoxLayout()
        #layout = QtWidgets.QHBoxLayout()
        
        hlayout1 = QtWidgets.QHBoxLayout()
        
        hlayout1.addWidget(Color('red'))
        hlayout1.addWidget(Color('blue'))
        hlayout1.addWidget(Color('green'))
        hlayout1.addWidget(Color('yellow'))
        hlayout1.setContentsMargins(50,0,0,0) #Sagdan,ustten vs bosluk birakir.
        hlayout1.setSpacing(50) #Sutunlar arasi bosluk
        
        hlayout2 = QtWidgets.QHBoxLayout()
        
        hlayout2.addWidget(Color('red'))
        hlayout2.addWidget(Color('blue'))
        hlayout2.addWidget(Color('green'))
        
        vlayout = QtWidgets.QVBoxLayout()
        vlayout.addLayout(hlayout1)
        vlayout.addLayout(hlayout2)
        
        """layout = QtWidgets.QGridLayout()
        
        layout.addWidget(Color('red'),0,0) #yatayda saga-dikeyde asagi
        layout.addWidget(Color('blue'),1,0)
        layout.addWidget(Color('green'),0,2)
        layout.addWidget(Color('yellow'),3,1)"""
        
        
        #widget = Color('blue')
        widget = QWidget()
        
        #widget.setLayout(layout)
        widget.setLayout(vlayout)
        #widget.setLayout(layout)
        
        self.setCentralWidget(widget)
        
def app():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
    
app()


#%%
#checkbox
import sys
from PyQt5 import QtWidgets
from _checkboxForm import Ui_MainWindow

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.cbSinema.stateChanged.connect(self.show_state)
        self.ui.cbKitapOkumak.stateChanged.connect(self.show_state)
        self.ui.cbSpor.stateChanged.connect(self.show_state)

        self.ui.btnHobilerSecilenleriAl .clicked.connect(self.getAllHobiler)
        self.ui.btnDerslerSecilenleriAl.clicked.connect(self.getAllDersler)

    def getAllHobiler(self):
        result = ''
        items = self.ui.groupHobiler.findChildren(QtWidgets.QCheckBox)
        for cb in items:
            if cb.isChecked():
                result += cb.text() + '\n'

        self.ui.lblResultHobiler.setText(result)

    def getAllDersler(self):
        result = ''
        items = self.ui.groupDersler.findChildren(QtWidgets.QCheckBox)
        for cb in items:
            if cb.isChecked():
                result += cb.text() + '\n'

        self.ui.lblResultDersler.setText(result)

    def show_state(self, value):
        cb = self.sender()

        print(value)
        print(cb.text())
        print(cb.isChecked())


def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())

app()

#%%
#combobox
from PyQt5 import QtWidgets
import sys
from _comboboxForm import Ui_MainWindow

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
    
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)      

        combo = self.ui.cbSehirler

        # combo.addItem('Ankara')
        # combo.addItem('İstanbul')
        # combo.addItem('Kocaeli')
        # combo.addItems(['Adana','İzmir','Rize'])

        self.ui.btnLoadItems.clicked.connect(self.LoadItems)
        self.ui.btnGetItem.clicked.connect(self.GetItem)
        self.ui.btnClear.clicked.connect(self.ClearItems)

        self.ui.cbSehirler.currentIndexChanged.connect(self.SelectedChangedIndex)
        self.ui.cbSehirler.currentIndexChanged[str].connect(self.SelectedChangedText)

    def ClearItems(self):
        self.ui.cbSehirler.clear()

    def LoadItems(self):
        sehirler = ['Adana','İzmir','Rize']
        
        self.ui.cbSehirler.addItems(sehirler)

    def GetItem(self):
        print(self.ui.cbSehirler.currentText())
        print(self.ui.cbSehirler.currentIndex())
        
        count = self.ui.cbSehirler.count()
        for index in range(count):
            print(self.ui.cbSehirler.itemText(index))

    def SelectedChangedIndex(self, index):
        print(index)

    def SelectedChangedText(self, text):
        print(text)
   
app = QtWidgets.QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())

#%%
#date
import sys
from PyQt5 import QtWidgets
from _dateForm import Ui_MainWindow
from PyQt5.QtCore import QDate, QTime, QDateTime

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)    

        self.ui.btnCalculate.clicked.connect(self.calculate)

    def calculate(self):
        start = self.ui.dateStart.date()
        end = self.ui.dateEnd.date()
        print(start, end)

        print('Days in month: {0}'.format(start.daysInMonth()))
        print('Days in year: {0}'.format(start.daysInYear()))

        print('total days: {0}'.format(start.daysTo(end)))

        now = QDate.currentDate()

        print('total days from now: {0}'.format(start.daysTo(now)))


def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())

app()

#%%
#list
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QMessageBox
from _listForm import Ui_MainWindow
import sys

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()   

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  

        # load Students
        self.loadStudents()

        # add New Student
        self.ui.btnAdd.clicked.connect(self.addStudent)

        # edit Student
        self.ui.btnEdit.clicked.connect(self.editStudent)

        # delete Student
        self.ui.btnRemove.clicked.connect(self.removeStudent)

        # Up 
        self.ui.btnUp.clicked.connect(self.upStudent)

        # Down 
        self.ui.btnDown.clicked.connect(self.downStudent)

        # sort
        self.ui.btnSort.clicked.connect(self.sortStudents)

        # close
        self.ui.btnExit.clicked.connect(self.close)

    def loadStudents(self):
        self.ui.listItems.addItems(['Ahmet','Ali','Çınar'])
        self.ui.listItems.setCurrentRow(1)

    def addStudent(self):
        currentIndex = self.ui.listItems.currentRow()
        text, ok = QInputDialog.getText(self, "New Student", "Student Name")
        if ok and text is not None:
            self.ui.listItems.insertItem(currentIndex ,text)

    def editStudent(self):
        index = self.ui.listItems.currentRow()
        item = self.ui.listItems.item(index)

        if item is not None:
            text, ok = QInputDialog.getText(self, "Edit Student", "Student Name", QLineEdit.Normal, item.text())
            if text and ok is not None:
                item.setText(text)
    
    def removeStudent(self):
        index = self.ui.listItems.currentRow()
        item = self.ui.listItems.item(index)
        
        if item is None:
            return

        q = QMessageBox.question(self, "Remove Student", "Do you want to remove student: " + item.text(), QMessageBox.Yes | QMessageBox.No)
        if q == QMessageBox.Yes:
            item = self.ui.listItems.takeItem(index)
            del item

    def upStudent(self):
        index = self.ui.listItems.currentRow()
        if index >= 1:
            item = self.ui.listItems.takeItem(index)
            self.ui.listItems.insertItem(index-1, item)
            self.ui.listItems.setCurrentItem(item)

    def downStudent(self):
        index = self.ui.listItems.currentRow()
        if index < self.ui.listItems.count()-1:
            item = self.ui.listItems.takeItem(index)
            self.ui.listItems.insertItem(index+1, item)
            self.ui.listItems.setCurrentItem(item)

    def sortStudents(self):
        self.ui.listItems.sortItems()

    def close(self):
        quit()
            
def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

app()

#%%
#Messagebox
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from _msgboxForm import Ui_MainWindow
import sys

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()   

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  

        self.ui.btnExit.clicked.connect(self.showDialog)

    def showDialog(self):

        result = QMessageBox.question(self, 'Close Application', 'Are you sure ?', QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Ignore, QMessageBox.Cancel)
        if result == QMessageBox.Ok:
            print('Yes clicked')
            QtWidgets.qApp.quit()
        else:
            print('No clicked')

        # msg = QMessageBox()

        # msg.setWindowTitle('Close Application')
        # msg.setText('Are you sure ?')
        # msg.setIcon(QMessageBox.Warning)
        # msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Ignore)
        # msg.setDefaultButton(QMessageBox.Cancel)
        # msg.setDetailedText('details....')
        # msg.buttonClicked.connect(self.popup_button)

        # x = msg.exec_()
        # print(x)

    # def popup_button(self, i):
    #     print(i.text())

    #     if i.text() == 'OK':
    #         print('OKEY...')
    #         QtWidgets.qApp.quit()
    #     elif i.text() == 'Cancel':
    #         print('Cancel...')
    #     else:
    #         print('Ignore...')
def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

app()

#%%
#radio Button
from PyQt5 import QtWidgets
import sys
from _radiobuttonForm import Ui_MainWindow

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
    
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.radioTurkiye.setChecked(True)
        self.ui.radioLise.setChecked(True)

        self.ui.radioTurkiye.toggled.connect(self.onClickedUlke)
        self.ui.radioAzerbaycan.toggled.connect(self.onClickedUlke)
        self.ui.radioAlmanya.toggled.connect(self.onClickedUlke)
        self.ui.radioYunanistan.toggled.connect(self.onClickedUlke)

        self.ui.radioilkokul.toggled.connect(self.onClickedEgitim)
        self.ui.radioLise.toggled.connect(self.onClickedEgitim)
        self.ui.radioUniversite.toggled.connect(self.onClickedEgitim)
        self.ui.radioYuksekLisans.toggled.connect(self.onClickedEgitim)

        self.ui.btnUlke.clicked.connect(self.getSelectedUlke)
        self.ui.btnEgitim.clicked.connect(self.getSelectedEgitim)

    def onClickedUlke(self):
        rb = self.sender()
        if rb.isChecked():
            print('seçilen ülke: '+ rb.text())

    def onClickedEgitim(self):
        rb = self.sender()
        if rb.isChecked():
            print('seçilen eğitim: '+ rb.text())

    def getSelectedUlke(self):
        items = self.ui.groupBoxUlke.findChildren(QtWidgets.QRadioButton)
        for rb in items:
            if rb.isChecked():
                self.ui.lblUlke.setText('seçilen ülke: '+ rb.text())

    def getSelectedEgitim(self):
        items = self.ui.groupBoxEgitim.findChildren(QtWidgets.QRadioButton)
        for rb in items:
            if rb.isChecked():
                self.ui.lblEgitim.setText('seçilen eğitim: '+ rb.text())

app = QtWidgets.QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())

#%%
#table
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from _tableForm import Ui_MainWindow
import sys

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()   

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)    

        self.loadProducts()
        self.ui.btnSave.clicked.connect(self.saveProduct)
        self.ui.tableProducts.doubleClicked.connect(self.doubleClick)

    def doubleClick(self):
        for item in self.ui.tableProducts.selectedItems():            
            print(item.row(), item.column(), item.text())    


    def saveProduct(self):
        name = self.ui.txtName.text()
        price = self.ui.txtPrice.text()

        if name and price is not None:
            rowCount = self.ui.tableProducts.rowCount()
            print(rowCount)
            self.ui.tableProducts.insertRow(rowCount)
            self.ui.tableProducts.setItem(rowCount,0, QTableWidgetItem(name))
            self.ui.tableProducts.setItem(rowCount,1, QTableWidgetItem(price))

    def loadProducts(self):

        products = [
            {'name': 'Samsung S5', 'price': 2000},
            {'name': 'Samsung S6', 'price': 3000},
            {'name': 'Samsung S7', 'price': 4000},
            {'name': 'Samsung S8', 'price': 5000}
        ]

        self.ui.tableProducts.setRowCount(len(products))
        self.ui.tableProducts.setColumnCount(2)
        self.ui.tableProducts.setHorizontalHeaderLabels(('Name','Price'))
        self.ui.tableProducts.setColumnWidth(0,200)
        self.ui.tableProducts.setColumnWidth(1,100)

        rowIndex = 0
        for product in products:
            self.ui.tableProducts.setItem(rowIndex,0, QTableWidgetItem(product['name']))
            self.ui.tableProducts.setItem(rowIndex,1, QTableWidgetItem(str(product['price'])))
            
            rowIndex+=1
            
def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

app()

#%%


















