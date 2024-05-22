# -*- coding: utf-8 -*-
"""
Created on Wed May 22 15:13:46 2024

@author: federicomazzetti
"""

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QComboBox, QLabel
from PyQt5 import uic
import sys
 
 
class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi(r"C:\Users\federicomazzetti\Documents\associa\mainwindow.ui", self)
 
        # find the widgets in the xml file
        self.oreResidue = {"Maranghi Samuele" : 18, "Picciolini Matteo" : 18, "Cristiana Neri" : 18}
        self.prof = {"Maranghi Samuele" : 0, "Picciolini Matteo" : 0, "Cristiana Neri" : 0}
        self.profStudente = {"Maranghi Samuele" : "", "Picciolini Matteo" : "", "Cristiana Neri" : ""}
        self.ora = 8
        self.combo = self.findChild(QComboBox, "combo")
        self.comboS = self.findChild(QComboBox, "comboS")
        self.oreProf = self.findChild(QLabel, "oreProf")
        self.textedit = self.findChild(QLineEdit, "search")
        self.button = self.findChild(QPushButton, "bSearch")
        self.buttonCar = self.findChild(QPushButton, "carica")
        self.buttonCar.clicked.connect(self.clickedBtnC)
        self.combo.currentTextChanged.connect(self.impostaOra)
        self.combo.children()
        self.show()
 
    def clickedBtn(self):
        self.combo.setCurrentText(self.textedit.text());
    
    def clickedBtnC(self):
        self.prof[self.combo.currentText()] = self.ora
        self.oreResidue[self.combo.currentText()] -= self.ora
        self.profStudente[self.combo.currentText()] = self.comboS.currentText()
        print(self.prof)
        print(self.profStudente)
        print(self.oreResidue)
        
    def impostaOra(self):
        self.oreProf.setText(str(self.oreResidue[self.combo.currentText()]))
        
app = QApplication(sys.argv)
window = UI()
app.exec_()