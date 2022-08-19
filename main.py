from datetime import datetime
import threading
import time
import sys
import requests
import random
from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsDropShadowEffect
from PyQt5 import QtWidgets, QtCore
from principal import Ui_MainWindow
from secundaria import Ui_second

class PantallaPrincipal(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.vprincipal = Ui_MainWindow()
        self.vprincipal.setupUi(self)
        self.show()
        self.vprincipal.label.setText("")
        self.vprincipal.label_2.setText("")
        # boton request
        self.vprincipal.request.clicked.connect(self.request_sw)
        self.vprincipal.listWidget.itemClicked.connect(self.getItem)

        def timer(timer_runs, ):
            while timer_runs.is_set():
                date = datetime.now()
                fecha = date.date()
                hora = date.time()
                self.vprincipal.label.setText(str(fecha))
                self.vprincipal.label_2.setText(str(hora))
                time.sleep(1)

        timer_runs = threading.Event()
        timer_runs.set()
        t = threading.Thread(target=timer, args=(timer_runs,))
        t.start()

    def getItem(self,item):
        it=self.vprincipal.listWidget.currentRow()
        selec=data[it]
        print(selec)
        names = requests.get('https://swapi.dev/api/people/' + str(selec))
        datajson=names.json()
        height = str((datajson['height']))
        mass = str((datajson['mass']))
        hair_color = str((datajson['hair_color']))
        skin_color = str((datajson['skin_color']))
        eye_color = str((datajson['eye_color']))
        birth_year = str((datajson['birth_year']))
        gender = str((datajson['gender']))
        self.ventana= QtWidgets.QMainWindow()
        self.ui=Ui_second()
        self.ui.setupUi(self.ventana)
        self.ventana.show()
        self.ui.lblheight.setText(height)
        self.ui.lblmass.setText(mass)
        self.ui.lblhair_color.setText(hair_color)
        self.ui.lblskin_color.setText(skin_color)
        self.ui.lbleye_color.setText(eye_color)
        self.ui.lblbirth_year.setText(birth_year)
        self.ui.lblgender.setText(gender)

    def person(self):
        global data
        data = []
        for i in range(10):
            data.append(str(random.randint(1, 83)))

    def request_sw(self):
        self.vprincipal.listWidget.clear()
        self.person()
        #print(data)
        namesjson = []
        for i in range(10):
            names = requests.get('https://swapi.dev/api/people/' + str(data[i]))
            namesjson.append((names.json())['name'])
        self.vprincipal.listWidget.addItems(namesjson)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PantallaPrincipal()
    sys.exit(app.exec_())
