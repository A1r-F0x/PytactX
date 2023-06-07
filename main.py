import j2l.pytactx.agent as pytactx
from PyQt5 import QtWidgets, uic, QtCore
import sys
import j2l.pytactx.agent as pytactx
agent=None
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.arena = "" # On créer des attributs pour sauvegarder les textes entrés jusqu'à ce que le bouton connect soit cliqué
        self.password = ""
        self.nickname = ""
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
        global agent
        self.timer.start()
        agent = pytactx.AgentFr(
            nom=self.nickname,
            arene=self.arena,
            username="demo",
            password=self.password,
            url="mqtt.jusdeliens.com",
            verbosite=3
        )
    def onNicknameTextChanged(self, text):
        print("Nickname text changed:",text)
        self.nickname = text
    def onArenaTextChanged(self, text):
        print("Arena text changed:",text)
        self.arena = text
    def onPasswordTextChanged(self, text):
        #print("Password text changed:",text) #A décommenter uniquement pour debug, pour ne pas dévoiler le mot de passe !
        self.password = text
    def onTimerUpdate(self):
        global agent
        if ( agent != None ):
            agent.orienter((agent.orientation+1)%4)
            agent.actualiser()
            # MAJ de la ui selon l'état du robot
            if ( agent.vie > self.ui.lifeBar.maximum() ):
                self.ui.lifeBar.setMaximum(agent.vie)
            self.ui.lifeBar.setValue(agent.vie)
            self.ui.lifeLabel.setText(str(agent.vie))
            if ( agent.vie > self.ui.ammoBar.maximum() ):
                self.ui.ammoBar.setMaximum(agent.munitions)
            self.ui.ammoBar.setValue(agent.munitions)
            self.ui.ammoLabel.setText(str(agent.munitions))
    def onUpButtonClicked(self):
        global agent
        agent.orienter(1)
        agent.deplacer(0,-1)
        agent.actualiser()
    def onLeftButtonClicked(self):
        global agent
        agent.orienter(2)
        agent.deplacer(-1,0)
        agent.actualiser()
    def onDownButtonClicked(self):
        global agent
        agent.orienter(3)
        agent.deplacer(0,+1)
        agent.actualiser()
    def onRightButtonClicked(self):
        global agent
        agent.orienter(0)
        agent.deplacer(+1,0)
        agent.actualiser()
    def onShootButtonClicked(self):
        global agent 
        agent.tirer(True)
        agent.orienter(0)
        agent.actualiser()
    def onNotShootButtonClicked(self):
        global agent 
        agent.tirer(False)
        agent.orienter(0)
        agent.actualiser()
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()