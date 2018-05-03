# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
import Qss
import time
import LoginFulei
import images_qr


class TextEdit(QtWidgets.QTextEdit):
    clicked = pyqtSignal()

    def mouseReleaseEvent(self, QMouseEvent):
        self.clicked.emit()


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(892, 693)
        MainWindow.setWindowIcon(QtGui.QIcon(":/Resouces/flkjlogo.png"))
        MainWindow.setIconSize(QtCore.QSize(30, 30))
        MainWindow.setDocumentMode(False)
        MainWindow.setMaximumSize(QtCore.QSize(892, 720))
        MainWindow.setMinimumSize(QtCore.QSize(892, 693))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(30, 10, 831, 631))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(60, 10, 711, 161))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 20, 651, 121))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(40, 200, 104, 31))
        self.textEdit.setInputMethodHints(QtCore.Qt.ImhMultiLine | QtCore.Qt.ImhPreferNumbers)
        self.textEdit.setObjectName("textEdit")
        self.textEdit_3 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_3.setGeometry(QtCore.QRect(170, 200, 104, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = TextEdit(self.tab)
        self.textEdit_4.setGeometry(QtCore.QRect(310, 200, 104, 31))
        self.textEdit_4.setInputMethodHints(QtCore.Qt.ImhDate | QtCore.Qt.ImhMultiLine)
        self.textEdit_4.setObjectName("textEdit_4")

        self.textEdit_5 = TextEdit(self.tab)
        self.textEdit_5.setGeometry(QtCore.QRect(440, 200, 104, 31))
        self.textEdit_5.setInputMethodHints(QtCore.Qt.ImhDate | QtCore.Qt.ImhMultiLine)
        self.textEdit_5.setObjectName("textEdit_5")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(590, 200, 78, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab)
        self.comboBox_2.setGeometry(QtCore.QRect(710, 200, 78, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setGeometry(QtCore.QRect(40, 260, 761, 331))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(28, 40, 60, 24))
        self.label_4.setObjectName("label_4")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_1.setGeometry(QtCore.QRect(90, 40, 131, 24))
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.progressBar_1 = QtWidgets.QProgressBar(self.groupBox_3)
        self.progressBar_1.setGeometry(QtCore.QRect(500, 45, 250, 20))
        self.progressBar_1.setProperty("value", 0)
        self.progressBar_1.setObjectName("progressBar_1")
        self.pushButton_1 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_1.setGeometry(QtCore.QRect(300, 40, 91, 30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Resouces/ok.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_1.setIcon(icon)
        self.pushButton_1.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_1.setObjectName("pushButton_1")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(420, 42, 71, 24))
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(220, 45, 51, 21))
        self.label_3.setObjectName("label_3")
        self.textEdit_1 = QtWidgets.QTextEdit(self.groupBox_3)
        self.textEdit_1.setGeometry(QtCore.QRect(50, 90, 651, 221))
        self.textEdit_1.setObjectName("textEdit_1")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_4.setGeometry(QtCore.QRect(60, 10, 731, 191))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label_6.setGeometry(QtCore.QRect(30, 20, 661, 141))
        self.label_6.setObjectName("label_6")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_5.setGeometry(QtCore.QRect(30, 220, 771, 371))
        self.groupBox_5.setObjectName("groupBox_5")
        self.textEdit_6 = TextEdit(self.groupBox_5)
        self.textEdit_6.setGeometry(QtCore.QRect(230, 30, 104, 31))
        self.textEdit_6.setInputMethodHints(QtCore.Qt.ImhDate | QtCore.Qt.ImhMultiLine)
        self.textEdit_6.setObjectName("textEdit_6")
        self.textEdit_7 = TextEdit(self.groupBox_5)
        self.textEdit_7.setGeometry(QtCore.QRect(360, 30, 104, 31))
        self.textEdit_7.setInputMethodHints(QtCore.Qt.ImhDate | QtCore.Qt.ImhMultiLine)
        self.textEdit_7.setObjectName("textEdit_7")
        self.textEdit_8 = QtWidgets.QTextEdit(self.groupBox_5)
        self.textEdit_8.setGeometry(QtCore.QRect(90, 30, 104, 31))
        self.textEdit_8.setInputMethodHints(QtCore.Qt.ImhMultiLine | QtCore.Qt.ImhPreferNumbers)
        self.textEdit_8.setObjectName("textEdit_8")
        self.progressBar_2 = QtWidgets.QProgressBar(self.groupBox_5)
        self.progressBar_2.setGeometry(QtCore.QRect(500, 95, 250, 20))
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName("progressBar_2")
        self.label_7 = QtWidgets.QLabel(self.groupBox_5)
        self.label_7.setGeometry(QtCore.QRect(220, 95, 51, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_5)
        self.label_8.setGeometry(QtCore.QRect(420, 92, 71, 24))
        self.label_8.setObjectName("label_8")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 90, 131, 24))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_9 = QtWidgets.QLabel(self.groupBox_5)
        self.label_9.setGeometry(QtCore.QRect(28, 90, 60, 24))
        self.label_9.setObjectName("label_9")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 90, 91, 30))
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit_9 = QtWidgets.QTextEdit(self.groupBox_5)
        self.textEdit_9.setGeometry(QtCore.QRect(50, 150, 651, 201))
        self.textEdit_9.setObjectName("textEdit_9")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 892, 25))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionAbout = QtWidgets.QAction(MainWindow)
        aboutico = QtGui.QIcon()
        aboutico.addPixmap(QtGui.QPixmap(":/Resouces/about.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(aboutico)
        self.actionAbout.setObjectName("actionAbout")

        self.actionQuit = QtWidgets.QAction(MainWindow)
        quitico = QtGui.QIcon()
        quitico.addPixmap(QtGui.QPixmap(":/Resouces/quit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(quitico)
        self.actionQuit.setObjectName("actionQuit")

        self.actionAuthor = QtWidgets.QAction(MainWindow)
        authorico = QtGui.QIcon()
        authorico.addPixmap(QtGui.QPixmap(":/Resouces/author.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAuthor.setIcon(authorico)
        self.actionAuthor.setObjectName("actionAuthor")
        self.menu.addAction(self.actionAbout)
        self.menu.addSeparator()
        self.menu.addAction(self.actionAuthor)
        self.menu.addSeparator()
        self.menu.addAction(self.actionQuit)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Kadawo小工具"))
        self.groupBox.setTitle(_translate("MainWindow", "操作流程"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p>1.选择下面六项条件，可以为空。<font color='red'>注意时间为空默认为当天</font></p><p>2.可以自己修改文件名。<font color='red'>注意请勿使用非法文件名称，否则程序会崩溃！</font></p><p>3.点击开始按钮即可开始程序，等待完成</p></body></html>"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "请输入设备id"))
        self.textEdit_3.setPlaceholderText(_translate("MainWindow", "请输入设备名称"))
        self.textEdit_4.setPlaceholderText(_translate("MainWindow", "请输入开始时间"))
        self.textEdit_5.setPlaceholderText(_translate("MainWindow", "请输入结束时间"))
        self.comboBox.setItemText(0, _translate("MainWindow", "商户选择"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "经销商选择"))
        self.groupBox_3.setTitle(_translate("MainWindow", "运行过程"))
        self.label_4.setText(_translate("MainWindow", "文件名称："))
        self.pushButton_1.setText(_translate("MainWindow", "开始"))
        self.label_5.setText(_translate("MainWindow", "完成进度："))
        self.label_3.setText(_translate("MainWindow", ".xlsx"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "按条件导出所有或单个机器数据"))
        self.groupBox_4.setTitle(_translate("MainWindow", "操作流程"))
        self.label_6.setText(_translate("MainWindow",
                                        "<html><head/><body><p>1.请输入设备id、开始时间、结束时间。<font color='red'>注意:id为必选项，而且要15位数设备id</font></p><p>2.可以自己修改文件名。<font color='red'>注意请勿使用非法文件名称，否则程序会崩溃！我这里就没有对文件名做安全验证了</font></p><p>3.点击开始按钮即可开始程序，等待完成</p></body></html>"))
        self.groupBox_5.setTitle(_translate("MainWindow", "运行过程"))
        self.textEdit_6.setPlaceholderText(_translate("MainWindow", "请输入开始时间"))
        self.textEdit_7.setPlaceholderText(_translate("MainWindow", "请输入结束时间"))
        self.textEdit_8.setPlaceholderText(_translate("MainWindow", "请输入设备id"))
        self.label_7.setText(_translate("MainWindow", ".xlsx"))
        self.label_8.setText(_translate("MainWindow", "完成进度："))
        self.label_9.setText(_translate("MainWindow", "文件名称："))
        self.pushButton_2.setText(_translate("MainWindow", "开始"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "导出单个机器详细数据"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "其它"))
        self.menu.setTitle(_translate("MainWindow", "帮助(H)"))
        self.actionAbout.setText(_translate("MainWindow", "关于"))
        self.actionAuthor.setText(_translate("MainWindow", "作者"))
        self.actionQuit.setText(_translate("MainWindow", "退出"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))

        self.lineEdit_1.setText(str(int(time.time())) + "_More")
        self.lineEdit_2.setText(str(int(time.time())) + "_One")

        # 设置鼠标样式和提示语
        for each in [self.pushButton_1, self.pushButton_2]:
            each.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.setMyStyle()

    def setMyStyle(self):
        qss = Qss.Qss()
        self.setStyleSheet(qss.myQss)


class LoginDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setWindowTitle(u'登录')
        self.setWindowIcon(QtGui.QIcon(":/Resouces/flkjlogo.png"))
        self.resize(320, 120)
        self.setMaximumSize(QtCore.QSize(320, 120))
        self.setMinimumSize(QtCore.QSize(320, 120))
        self.leName = QtWidgets.QLineEdit(self)
        self.leName.setPlaceholderText(u'用户名')
        self.lePassword = QtWidgets.QLineEdit(self)
        self.lePassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lePassword.setPlaceholderText(u'密码')
        self.pbLogin = QtWidgets.QPushButton(u'登录', self)
        self.pbCancel = QtWidgets.QPushButton(u'取消', self)
        self.pbLogin.clicked.connect(self.login)
        self.pbCancel.clicked.connect(self.reject)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.leName)
        layout.addWidget(self.lePassword)
        # 放一个间隔对象美化布局
        spacerItem = QtWidgets.QSpacerItem(80, 48, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        layout.addItem(spacerItem)
        # 按钮布局
        buttonLayout = QtWidgets.QHBoxLayout()
        # 左侧放一个间隔
        spancerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        buttonLayout.addItem(spancerItem2)
        buttonLayout.addWidget(self.pbLogin)
        buttonLayout.addWidget(self.pbCancel)
        layout.addLayout(buttonLayout)
        qss = Qss.Qss()
        self.setLayout(layout)
        self.setStyleSheet(qss.myQss)

    def login(self):
        lo = LoginFulei.LoginFulei()
        lo.doLogin(self.leName.text(), self.lePassword.text())
        check = lo.isLogin()
        if check:
            self.accept()  # 关闭对话框并返回1
        else:
            QtWidgets.QMessageBox.critical(self, u'错误', u'用户名密码不匹配')


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    my_ui = Ui_MainWindow()
    my_ui.show()
    sys.exit(app.exec_())
