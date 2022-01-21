from cgitb import text
from distutils import text_file
import sqlite3
from unittest import loader
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtUiTools import QUiLoader


################################################################################################################################################
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        self.ui = loader.load("main.ui")
        self.ui.show()

        self.ui.setWindowTitle("Contacts")
        self.name=[[]]
        self.conn = sqlite3.connect("contacts.db")
        self.my_cursor = self.conn.cursor()
        self.load_data()

        self.ui.pushButton.clicked.connect(self.openSub)
        self.ui.pushButton_2.clicked.connect(self.opendel)
        self.ui.Deleteall_btn.clicked.connect(self.deleteall)
        self.ui.light_btn.clicked.connect(self.light_mode)
        self.ui.dark_btn.clicked.connect(self.dark_mode)

    def openSub(self):
        self.ui = Window_plus()

    def opendel(self):
        self.ui = Window_del()

    def load_data(self):
        self.my_cursor.execute("SELECT * FROM persons")
        result = self.my_cursor.fetchall()
        
        for item in result:

            self.btn_box = QPushButton( self)
            self.btn_box.setText(F"{item[0]}\n  {item[1]}\t  {item[2]}\n  {item[3]}\n  {item[4]}\n  {item[5]}  ")
            self.name.append(item[1])
            self.ui.verticalLayout.addWidget(self.btn_box)
            #self.btn_box.clicked.connect(self.clickMethod)
            
    ####open information with message box
    def clickMethod(self ):
        text_box = QMessageBox()
        for i in range(self.ui.verticalLayout.count()):
            re=self.my_cursor.execute(f"SELECT * FROM persons WHERE name == \'{self.name[i]}\';")
        for r in re:
            text_box.setText(F"\n ID:\t\t {r[0]}\n FIRST NAME:\t {r[1]}\n LAST NAME:\t {r[2]}\n PHONE NUMBER:\t {r[3]}\n HOME NUMBER:\t {r[4]}\n EMAIL:\t\t {r[5]}")
        text_box.exec_()
            
    def deleteall(self):
        self.my_cursor.execute("DELETE FROM persons;")
        self.conn.commit()
        for i in range(self.ui.verticalLayout.count()):
            self.ui.verticalLayout.itemAt(i).widget().deleteLater()

    def dark_mode(self):
        self.ui.setStyleSheet("background-color: rgb(66, 66, 66);")
        self.ui.pushButton.setStyleSheet("background-color: rgb(240, 173, 61);")
        self.ui.pushButton_2.setStyleSheet("background-color: rgb(240, 173, 61);")
        self.ui.Deleteall_btn.setStyleSheet("background-color: rgb(240, 173, 61);")
        self.ui.light_btn.setStyleSheet("background-color: rgb(240, 173, 61);")
        self.ui.dark_btn.setStyleSheet("background-color: rgb(240, 173, 61);")
        self.ui.label.setStyleSheet("background-color: rgb(240, 173, 61);")
        self.ui.scrollArea.setStyleSheet("background-color: rgb(128, 128, 128);")

    def light_mode(self):
    
        self.ui.setStyleSheet("background-color: rgb(187, 186, 188);")
        self.ui.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.Deleteall_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.light_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.dark_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.scrollArea.setStyleSheet("background-color: rgb(255, 255, 255);")
################################################################################################################################################        
class Window_plus(QWidget):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        self.ad = loader.load("add.ui")
        self.ad.show()
        self.ad.setWindowTitle("Add information")
        self.ad.btn_ok.clicked.connect(self.close_window)
        self.ad.light.clicked.connect(self.light_mode)
        self.ad.dark.clicked.connect(self.dark_mode)
        self.conn = sqlite3.connect("contacts.db")
        self.my_cursor = self.conn.cursor()

    def close_window(self):

        self.id = self.ad.lineEdit_1.text()
        self.name = self.ad.lineEdit_2.text()
        self.family = self.ad.lineEdit_3.text()
        self.phone_number = self.ad.lineEdit_4.text()
        self.mobile_number = self.ad.lineEdit_5.text()
        self.email = self.ad.lineEdit_6.text()
        self.my_cursor.execute(f"INSERT INTO persons(id, name,family,phone_number,mobile_number , email) VALUES ('{self.id}' , '{self.name}' ,'{self.family}', '{self.phone_number}','{self.mobile_number}' , '{self.email}'); " )
        self.conn.commit()
        self.ad = MainWindow

    def dark_mode(self):
        self.ad.setStyleSheet("background-color: rgb(66, 66, 66);")
        self.ad.lineEdit_1.setStyleSheet("background-color: rgb(255, 173, 74);")
        self.ad.lineEdit_2.setStyleSheet("background-color: rgb(255, 173, 74);")
        self.ad.lineEdit_3.setStyleSheet("background-color: rgb(255, 173, 74);")
        self.ad.lineEdit_4.setStyleSheet("background-color: rgb(255, 173, 74);")
        self.ad.lineEdit_5.setStyleSheet("background-color: rgb(255, 173, 74);")
        self.ad.lineEdit_6.setStyleSheet("background-color: rgb(255, 173, 74);")
        self.ad.light.setStyleSheet("background-color: rgb(255, 173, 74);")
        self.ad.dark.setStyleSheet("background-color: rgb(255, 173, 74);")
        self.ad.btn_ok.setStyleSheet("background-color: rgba(255, 137, 33, 225);")

    def light_mode(self):
        self.ad.setStyleSheet("background-color: rgb(187, 186, 188);")
        self.ad.lineEdit_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ad.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ad.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ad.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ad.lineEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ad.lineEdit_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ad.light.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ad.dark.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ad.btn_ok.setStyleSheet("background-color: rgb(255, 245, 201);")
################################################################################################################################################           
class Window_del(QWidget):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        self.dl = loader.load("del.ui")
        self.dl.show()
        self.dl.setWindowTitle("Delete information")
        self.dl.btndl.clicked.connect(self.dell)
        self.dl.dark.clicked.connect(self.dark_mode)
        self.dl.light.clicked.connect(self.light_mode)
        self.conn = sqlite3.connect("contacts.db")
        self.my_cursor = self.conn.cursor()

    def dell(self):

        self.id = self.dl.lineEdit.text()
    
        self.my_cursor.execute(f"DELETE FROM persons WHERE id == \'{self.id}\';")
        self.conn.commit()
        self.dl = MainWindow

    def dark_mode(self):
        self.dl.setStyleSheet("background-color: rgb(66, 66, 66);")
        self.dl.btndl.setStyleSheet("background-color: rgba(255, 137, 33, 225);")
        self.dl.dark.setStyleSheet("background-color: rgb(255, 173, 74);")
        self.dl.light.setStyleSheet("background-color: rgb(255, 173, 74);")
        self.dl.lineEdit.setStyleSheet("background-color: rgb(255, 173, 74);")
    
    def light_mode(self):
        self.dl.setStyleSheet("background-color: rgb(187, 186, 188);")
        self.dl.btndl.setStyleSheet("background-color: rgb(255, 245, 201);")
        self.dl.dark.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dl.light.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dl.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
################################################################################################################################################

      

app = QApplication()
main_window = MainWindow()
app.exec()