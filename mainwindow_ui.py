# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/tristanopp/Documents/creative Num'Sup/sem26-27-28 python/projet_final/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 600)
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.loginTab = QtWidgets.QWidget()
        self.loginTab.setObjectName("loginTab")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.loginTab)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.labelNickname = QtWidgets.QLabel(self.loginTab)
        self.labelNickname.setObjectName("labelNickname")
        self.verticalLayout.addWidget(self.labelNickname)
        self.nicknameEdit = QtWidgets.QLineEdit(self.loginTab)
        self.nicknameEdit.setText("")
        self.nicknameEdit.setObjectName("nicknameEdit")
        self.verticalLayout.addWidget(self.nicknameEdit)
        self.arenaLabel = QtWidgets.QLabel(self.loginTab)
        self.arenaLabel.setObjectName("arenaLabel")
        self.verticalLayout.addWidget(self.arenaLabel)
        self.arenaEdit = QtWidgets.QLineEdit(self.loginTab)
        self.arenaEdit.setObjectName("arenaEdit")
        self.verticalLayout.addWidget(self.arenaEdit)
        self.passwordLabel = QtWidgets.QLabel(self.loginTab)
        self.passwordLabel.setObjectName("passwordLabel")
        self.verticalLayout.addWidget(self.passwordLabel)
        self.passwordEdit = QtWidgets.QLineEdit(self.loginTab)
        self.passwordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordEdit.setObjectName("passwordEdit")
        self.verticalLayout.addWidget(self.passwordEdit)
        self.connectButton = QtWidgets.QPushButton(self.loginTab)
        self.connectButton.setObjectName("connectButton")
        self.verticalLayout.addWidget(self.connectButton)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.tabWidget.addTab(self.loginTab, "")
        self.robotTab = QtWidgets.QWidget()
        self.robotTab.setObjectName("robotTab")
        self.formLayout = QtWidgets.QFormLayout(self.robotTab)
        self.formLayout.setObjectName("formLayout")
        self.lifeInfoLabel = QtWidgets.QLabel(self.robotTab)
        self.lifeInfoLabel.setObjectName("lifeInfoLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lifeInfoLabel)
        self.lifeBar = QtWidgets.QProgressBar(self.robotTab)
        self.lifeBar.setProperty("value", 24)
        self.lifeBar.setObjectName("lifeBar")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lifeBar)
        self.lifeLabel = QtWidgets.QLabel(self.robotTab)
        self.lifeLabel.setObjectName("lifeLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lifeLabel)
        self.ammoInfoLabel = QtWidgets.QLabel(self.robotTab)
        self.ammoInfoLabel.setObjectName("ammoInfoLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.ammoInfoLabel)
        self.ammoBar = QtWidgets.QProgressBar(self.robotTab)
        self.ammoBar.setProperty("value", 24)
        self.ammoBar.setObjectName("ammoBar")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.ammoBar)
        self.ammoLabel = QtWidgets.QLabel(self.robotTab)
        self.ammoLabel.setObjectName("ammoLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.ammoLabel)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButtonUp = QtWidgets.QPushButton(self.robotTab)
        self.pushButtonUp.setObjectName("pushButtonUp")
        self.gridLayout.addWidget(self.pushButtonUp, 2, 1, 1, 1)
        self.pushButtonDown = QtWidgets.QPushButton(self.robotTab)
        self.pushButtonDown.setObjectName("pushButtonDown")
        self.gridLayout.addWidget(self.pushButtonDown, 4, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 3, 1, 1, 1)
        self.pushButtonLeft = QtWidgets.QPushButton(self.robotTab)
        self.pushButtonLeft.setObjectName("pushButtonLeft")
        self.gridLayout.addWidget(self.pushButtonLeft, 3, 0, 1, 1)
        self.pushButtonRight = QtWidgets.QPushButton(self.robotTab)
        self.pushButtonRight.setObjectName("pushButtonRight")
        self.gridLayout.addWidget(self.pushButtonRight, 3, 2, 1, 1)
        self.autoMode = QtWidgets.QCheckBox(self.robotTab)
        self.autoMode.setObjectName("autoMode")
        self.gridLayout.addWidget(self.autoMode, 2, 0, 1, 1)
        self.formLayout.setLayout(4, QtWidgets.QFormLayout.SpanningRole, self.gridLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButtonShoot = QtWidgets.QPushButton(self.robotTab)
        self.pushButtonShoot.setObjectName("pushButtonShoot")
        self.verticalLayout_2.addWidget(self.pushButtonShoot)
        self.pushButtonStopShoot = QtWidgets.QPushButton(self.robotTab)
        self.pushButtonStopShoot.setObjectName("pushButtonStopShoot")
        self.verticalLayout_2.addWidget(self.pushButtonStopShoot)
        self.formLayout.setLayout(6, QtWidgets.QFormLayout.FieldRole, self.verticalLayout_2)
        self.tabWidget.addTab(self.robotTab, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 750, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.arenaEdit.textEdited['QString'].connect(MainWindow.onArenaTextChanged) # type: ignore
        self.connectButton.clicked.connect(MainWindow.onConnectButtonClicked) # type: ignore
        self.nicknameEdit.textEdited['QString'].connect(MainWindow.onNicknameTextChanged) # type: ignore
        self.passwordEdit.textEdited['QString'].connect(MainWindow.onPasswordTextChanged) # type: ignore
        self.pushButtonUp.pressed.connect(MainWindow.onUpButtonClicked) # type: ignore
        self.pushButtonDown.pressed.connect(MainWindow.onDownButtonClicked) # type: ignore
        self.pushButtonLeft.pressed.connect(MainWindow.onLeftButtonClicked) # type: ignore
        self.pushButtonRight.pressed.connect(MainWindow.onRightButtonClicked) # type: ignore
        self.pushButtonShoot.pressed.connect(MainWindow.onShootButtonClicked) # type: ignore
        self.pushButtonStopShoot.clicked.connect(MainWindow.onNotShootButtonClicked) # type: ignore
        self.autoMode.toggled['bool'].connect(MainWindow.onAutoMode) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelNickname.setText(_translate("MainWindow", "Nickname"))
        self.nicknameEdit.setPlaceholderText(_translate("MainWindow", "Enter your nickname here"))
        self.arenaLabel.setText(_translate("MainWindow", "Arena"))
        self.arenaEdit.setPlaceholderText(_translate("MainWindow", "Enter the arena"))
        self.passwordLabel.setText(_translate("MainWindow", "Password"))
        self.passwordEdit.setPlaceholderText(_translate("MainWindow", "Enter password here"))
        self.connectButton.setText(_translate("MainWindow", "Connect"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.loginTab), _translate("MainWindow", "Login"))
        self.lifeInfoLabel.setText(_translate("MainWindow", "Life"))
        self.lifeLabel.setText(_translate("MainWindow", "0/0"))
        self.ammoInfoLabel.setText(_translate("MainWindow", "Ammo"))
        self.ammoLabel.setText(_translate("MainWindow", "0/0"))
        self.pushButtonUp.setText(_translate("MainWindow", "haut "))
        self.pushButtonDown.setText(_translate("MainWindow", "bas"))
        self.pushButtonLeft.setText(_translate("MainWindow", "gauche"))
        self.pushButtonRight.setText(_translate("MainWindow", "droite"))
        self.autoMode.setText(_translate("MainWindow", "Auto"))
        self.pushButtonShoot.setText(_translate("MainWindow", "Tirer"))
        self.pushButtonStopShoot.setText(_translate("MainWindow", "stop Tirer "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.robotTab), _translate("MainWindow", "Robot"))
