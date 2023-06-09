import j2l.pytactx.agent as pytactx
from PyQt5 import QtWidgets, uic, QtCore
import sys
import j2l.pytactx.agent as pytactx
import auto
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.arena = "" # On créer des attributs pour sauvegarder les textes entrés jusqu'à ce que le bouton connect soit cliqué
        self.password = ""
        self.nickname = ""
        self.auto=False
        self.agent=None
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
        agent = pytactx.AgentFr(
            nom=self.nickname,
            arene=self.arena,
            username="demo",
            password=self.password,
            url="mqtt.jusdeliens.com",
            verbosite=3
        )
        auto.setAgent(agent)
        self.timer.start()
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
        
        if ( self.agent != None ):
            self.agent.actualiser()
            if self.auto:        #quand la checkbox est cochée on rentre dans la boucle
                auto.actualiserAgent()
            # MAJ de la ui selon l'état du robot
            if ( self.agent.vie > self.ui.lifeBar.maximum() ):
                self.ui.lifeBar.setMaximum(self.agent.vie)
            self.ui.lifeBar.setValue(self.agent.vie)
            self.ui.lifeLabel.setText(str(self.agent.vie))
            if ( self.agent.vie > self.ui.ammoBar.maximum() ):
                self.ui.ammoBar.setMaximum(self.agent.munitions)
            self.ui.ammoBar.setValue(self.agent.munitions)
            self.ui.ammoLabel.setText(str(self.agent.munitions))
    def onUpButtonClicked(self):
        self.agent.orienter(1)
        self.agent.deplacer(0,-1)
        self.agent.actualiser()
    def onLeftButtonClicked(self):
        self.agent.orienter(2)
        self.agent.deplacer(-1,0)
        self.agent.actualiser()
    def onDownButtonClicked(self):
        self.agent.orienter(3)
        self.agent.deplacer(0,+1)
        self.agent.actualiser()
    def onRightButtonClicked(self):
        self.agent.orienter(0)
        self.agent.deplacer(+1,0)
        self.agent.actualiser()
    def onShootButtonClicked(self):
        self.agent.tirer(True)
        self.agent.orienter(0)
        self.agent.actualiser()
    def onNotShootButtonClicked(self):
         
        self.agent.tirer(False)
        self.agent.orienter(0)
        self.agent.actualiser()

    def onAutoMode(self,isChecked):
        self.auto=isChecked
        
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()