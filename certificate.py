from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtPrintSupport import QPrintDialog, QPrintPreviewDialog, QPrinter
from PyQt5.Qt import QFileInfo
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QLineEdit, QDialog ,QFileDialog, QInputDialog
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox


class Ui_MainWindow2(object):

    def handlePaintRequest(self, printer):
        printer.setResolution(1000)
        printer.setPageMargins(6, 5, 6, 5, QPrinter.Millimeter)
        painter = QPainter()
        painter.begin(printer)
        screenPixmap = self.centralwidget.grab()
        screenPixmap = screenPixmap.scaledToWidth(int(screenPixmap.width() *8000/screenPixmap.width()))
        painter.drawPixmap(10,10, screenPixmap)
        painter.end()
  
    def printPreviewListMethod(self):
        dialog = QPrintPreviewDialog()
        dialog.paintRequested.connect(self.handlePaintRequest)
        dialog.exec_()

    def setupUi(self, MainWindow2):
        MainWindow2.setObjectName("MainWindow2")
        MainWindow2.resize(939, 760)
        MainWindow2.setMaximumSize(QtCore.QSize(939, 760))
        MainWindow2.setMinimumSize(QtCore.QSize(939, 760))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo/ico_logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow2.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow2)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 941, 711))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../Downloads/cert/certificate_of_legitimacy.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        
        self.name_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.name_edit.setGeometry(QtCore.QRect(306, 339, 465, 71))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.name_edit.setFont(font)
        self.name_edit.setStyleSheet("color: rgb(255, 244, 136);""background-color: rgb(0, 0, 0);")
        self.name_edit.setFrame(False)
        self.name_edit.setObjectName("name_edit")
        
        self.gt_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.gt_edit.setGeometry(QtCore.QRect(360, 459, 265, 20))
        self.gt_edit.setStyleSheet("color: rgb(255, 244, 136);""background-color: rgb(0, 0, 0);")
        self.gt_edit.setFrame(False)
        self.gt_edit.setObjectName("gt_edit")
        
        self.ir_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.ir_edit.setGeometry(QtCore.QRect(360, 440, 113, 20))
        self.ir_edit.setStyleSheet("color: rgb(255, 244, 136);""background-color: rgb(0, 0, 0);")
        self.ir_edit.setFrame(False)
        self.ir_edit.setObjectName("ir_edit")
        
        self.mww_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.mww_edit.setEnabled(True)
        self.mww_edit.setGeometry(QtCore.QRect(360, 477, 261, 20))
        self.mww_edit.setStyleSheet("color: rgb(255, 244, 136);""background-color: rgb(0, 0, 0);")
        self.mww_edit.setFrame(False)
        self.mww_edit.setObjectName("mww_edit")
        
        self.chapter_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.chapter_edit.setEnabled(True)
        self.chapter_edit.setGeometry(QtCore.QRect(460, 528, 301, 20))
        self.chapter_edit.setStyleSheet("color: rgb(255, 244, 136);""background-color: rgb(0, 0, 0);")
        self.chapter_edit.setFrame(False)
        self.chapter_edit.setObjectName("chapter_edit")
        
        self.chairman_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.chairman_edit.setEnabled(True)
        self.chairman_edit.setGeometry(QtCore.QRect(650, 623, 141, 20))
        self.chairman_edit.setStyleSheet("color: rgb(255, 244, 136);""background-color: rgb(0, 0, 0);")
        self.chairman_edit.setFrame(False)
        self.chairman_edit.setObjectName("chairman_edit")
        
        self.date_issued_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.date_issued_edit.setEnabled(True)
        self.date_issued_edit.setGeometry(QtCore.QRect(286, 623, 138, 20))
        self.date_issued_edit.setStyleSheet("color: rgb(255, 244, 136);""background-color: rgb(0, 0, 0);")
        self.date_issued_edit.setFrame(False)
        self.date_issued_edit.setObjectName("date_issued_edit")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 711, 939, 29))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.printPreviewListMethod)
        
        MainWindow2.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow2)
        self.statusbar.setObjectName("statusbar")
        MainWindow2.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow2)

    def retranslateUi(self, MainWindow2):
        _translate = QtCore.QCoreApplication.translate
        MainWindow2.setWindowTitle(_translate("MainWindow2", "Certificate of Legitimacy"))
        self.pushButton.setText(_translate("MainWindow2", "Print"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow2 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow2()
    ui.setupUi(MainWindow2)
    MainWindow2.show()
    sys.exit(app.exec_())
