
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
import pytactx.agent as pytactx

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("login.ui", self)
    
    def onPushButtonClicked(self):
        print("bouton cliqué")
    
    def ontxtchanged(self,text):
        print("texte changed: ",text)
    def ontxtchanged(self,text):
        print("texte changed: ",text)
    def ontxtchanged(self,text):
        print("texte changed: ",text)
 # On crée un timer pour régulièrement envoyer les requetes de l'agent au server et actualiser son état 
        self.timer = QtCore.QTimer()
        self.timer.setTimerType(QtCore.Qt.PreciseTimer)
        self.timer.setInterval(20)
        self.timer.timeout.connect(self.onTimerUpdate)
        self.ui = uic.loadUi("mainwindow.ui", self) # Le fichier mainwindow.ui généré par Qt Designer doit être à côté du uisample.py
    def onConnectButtonClicked(self):
        """
        Callback de slot associée au signal du PushButton 
        dans Qt Designer, via 
        - click droit sur MainWindow -> Modifier signaux/slots -> "+" -> onPushButtonClicked
        - menu Editeur de signaux et slots -> "+" -> 
            Emetteur : "pushButton"
            Signal : clicked()
            Receveur : MainWindow
            Slot : onPushButtonClicked()
        """
        print("Connecting")
        self.timer.start()
        self.agent = pytactx.AgentFr(
            nom=self.nickname, 
            arene=self.arena, 
            username="demo",
            password=self.password, 
            url="mqtt.jusdeliens.com", 
            verbosite=3
        )
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()