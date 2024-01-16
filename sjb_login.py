from PyQt5 import QtCore, QtGui, QtWidgets
# import mysql.connector as mc
# import pymysql
from PyQt5.QtWidgets import QTableWidgetItem, QAbstractItemView, QVBoxLayout, QHBoxLayout, QHeaderView,QTableWidget
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
import sys
from sjb import Ui_MainWindow
import sqlite3
import os



class Ui_mainForm(object):

    def open_window(self):
        self.window =QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        mainForm.close()
        self.window.show()

    def messageBox(self,title,message):
        mess=QtWidgets.QMessageBox()
        mess.setStyleSheet('QMessageBox {background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 255)); color: white;}\
            QPushButton{color: white; font-size: 16px; background-color: rgb(75,75,75);\
            border-radius: 5px; padding: 10px; text-align: center;} QPushButton:hover{color: rgb(0, 170, 127);}')
        mess.setWindowTitle(title)
        mess.setWindowIcon(QtGui.QIcon('logo/ico_logo.ico'))
        mess.setText(message)
        mess.setIcon(QMessageBox.Information)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()

    def close(self):
        #sys.exit()
        app.quit()

    # def log(self):

    #     user=self.user_edit.text()
    #     password=self.pass_edit.text()

    #     self.conn=pymysql.connect(host="localhost", user="root", password="noahkuan03", db="myproject3")
    #     cur=self.conn.cursor()
    #     data = cur.execute ("SELECT * from adminlogin WHERE user_name = '"+user+"' AND password = '"+password+"'")
        
    #     if (data):
    #         self.messageBox("Information", "Login Successful")
    #         self.open_window()
    #     else:
    #         self.messageBox("Information", "Invalid Username or Password")
    #         return 

    def log(self):
        user = self.user_edit.text()
        password = self.pass_edit.text()

        # Connect to SQLite3 database
        conn = sqlite3.connect("myproject3.db")
        cur = conn.cursor()

        # Use placeholders to prevent SQL injection
        cur.execute("SELECT * FROM adminlogin WHERE user_name = ? AND password = ?", (user, password))
        data = cur.fetchone()

        if data:
            self.messageBox("Information", "Login Successful")
            self.open_window()
        else:
            self.messageBox("Information", "Invalid Username or Password")

        # Close the database connection
        conn.close()

    def create_database(self):
        database_file = "myproject3.db"

        # Check if the database file already exists
        if os.path.exists(database_file):
            print(f"The database file '{database_file}' already exists.")
            return

        # Connect to SQLite3 database (this will create a new database file if it doesn't exist)
        conn = sqlite3.connect(database_file)
        cur = conn.cursor()

        # Create the adminlogin table if it doesn't exist
        cur.execute('''
            CREATE TABLE IF NOT EXISTS adminlogin (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_name TEXT,
                password TEXT
            )
        ''')

        # Commit the changes and close the connection
        self.messageBox("Information", "Database Created")
        conn.commit()
        conn.close()

    def retrieve_data():
        conn = sqlite3.connect("myproject3.db")
        cur = conn.cursor()

        # Example: Select all rows from the adminlogin table
        cur.execute("SELECT * FROM adminlogin")
        
        # Fetch all rows as a list of tuples
        rows = cur.fetchall()

        # Print or process the retrieved data
        for row in rows:
            print(row)

        # Close the database connection
        conn.close()

    def insert_data(self):
        user=self.user_edit.text()
        password=self.pass_edit.text()

        conn = sqlite3.connect("myproject3.db")
        cur = conn.cursor()

        # Example: Insert a new row into the adminlogin table
        cur.execute("INSERT INTO adminlogin (user_name, password) VALUES (?, ?)", (user, password))

        self.messageBox("Information", "Data added")

        # Commit the changes
        conn.commit()

        # Close the database connection
        conn.close()

    # Call the function to insert new data
   



    def setupUi(self, mainForm):
        mainForm.setObjectName("mainForm")
        mainForm.resize(588, 440)
        mainForm.setMaximumSize(QtCore.QSize(588, 440))
        mainForm.setMinimumSize(QtCore.QSize(588, 440))
        mainForm.setWindowFlags( QtCore.Qt.WindowCloseButtonHint )
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo/ico_logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainForm.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(mainForm)
        self.centralwidget.setObjectName("centralwidget")
        
        
        self.login = QtWidgets.QPushButton(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(210, 320, 91, 41))
        self.login.setObjectName("login")
        self.login.clicked.connect(self.log)
        # self.login.clicked.connect(self.retrieve_data)
        # self.login.clicked.connect(self.insert_data)
        
        self.cancel = QtWidgets.QPushButton(self.centralwidget)
        self.cancel.setGeometry(QtCore.QRect(320, 320, 91, 41))
        self.cancel.setObjectName("cancel")
        self.cancel.clicked.connect(self.close)
        
        self.user_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.user_edit.setGeometry(QtCore.QRect(210, 200, 201, 31))
        self.user_edit.setObjectName("user_edit")
        
        self.pass_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.pass_edit.setGeometry(QtCore.QRect(210, 250, 201, 31))
        self.pass_edit.setObjectName("pass_edit")
        self.pass_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        
        self.user_label = QtWidgets.QLabel(self.centralwidget)
        self.user_label.setGeometry(QtCore.QRect(110, 200, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(12)
        self.user_label.setFont(font)
        self.user_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.user_label.setObjectName("user_label")
        
        self.pass_label = QtWidgets.QLabel(self.centralwidget)
        self.pass_label.setGeometry(QtCore.QRect(110, 250, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(12)
        self.pass_label.setFont(font)
        self.pass_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.pass_label.setObjectName("pass_label")
        
        self.logo_label = QtWidgets.QLabel(self.centralwidget)
        self.logo_label.setGeometry(QtCore.QRect(220, 20, 161, 161))
        self.logo_label.setText("")
        self.logo_label.setPixmap(QtGui.QPixmap("logo/logo.png"))
        self.logo_label.setScaledContents(True)
        self.logo_label.setObjectName("logo_label")
        
        self.background_label = QtWidgets.QLabel(self.centralwidget)
        self.background_label.setGeometry(QtCore.QRect(0, 0, 591, 441))
        self.background_label.setText("")
        self.background_label.setPixmap(QtGui.QPixmap("logo/back2.jpg"))
        self.background_label.setScaledContents(True)
        self.background_label.setObjectName("background_label")
        self.background_label.raise_()
        
        self.login.raise_()
        self.cancel.raise_()
        self.user_edit.raise_()
        self.pass_edit.raise_()
        self.user_label.raise_()
        self.pass_label.raise_()
        self.logo_label.raise_()


        
        mainForm.setCentralWidget(self.centralwidget)
        # self.statusbar = QtWidgets.QStatusBar(mainForm)
        # self.statusbar.setObjectName("statusbar")
        # mainForm.setStatusBar(self.statusbar)

        self.retranslateUi(mainForm)
        QtCore.QMetaObject.connectSlotsByName(mainForm)

    def retranslateUi(self, mainForm):
        _translate = QtCore.QCoreApplication.translate
        mainForm.setWindowTitle(_translate("mainForm", "San Juan Batangas Municipal Council"))
        self.login.setText(_translate("mainForm", "Login"))
        self.cancel.setText(_translate("mainForm", "Cancel"))
        self.user_label.setText(_translate("mainForm", "Username :"))
        self.pass_label.setText(_translate("mainForm", "Password :"))
      


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainForm = QtWidgets.QMainWindow()
    ui = Ui_mainForm()
    ui.setupUi(mainForm)
    mainForm.show()
    sys.exit(app.exec_())
