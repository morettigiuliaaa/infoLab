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
        uic.loadUi(r"C:\Users\federicomazzetti\Desktop\infoLab\mainwindow.ui", self)
 
        # find the widgets in the xml file
        #prima riepi cobo 
        #riempi oreresidue
        
        self.combo = self.findChild(QComboBox, "comboBoxInsegnante")
        self.comboS = self.findChild(QComboBox, "comboBoxStudente")
        
        self.prof=[{"nome":"Samuele","cognome":"Maranghi","oreResidue":18,"studente":""},{"nome":"Paola","cognome":"Pallucca","oreResidue":18,"studente":""},{"nome":"David","cognome":"Stocchi","oreResidue":18,"studente":""},{"nome":"Valeria","cognome":"Giovannini","oreResidue":18,"studente":""},{"nome":"Matteo","cognome":"Picciolini","oreResidue":18,"studente":""}]
        self.studenti=[{"nome":"Federico","cognome":"Mazzetti"},{"nome":"Giacomo","cognome":"Poldi"},{"nome":"Alejandro","cognome":"Ordonez"},{"nome":"Anwar","cognome":"Belkheir"},{"nome":"Ludovico","cognome":"Mischianti"},{"nome":"Leonardo","cognome":"Ramacci"},{"nome":"Andrea","cognome":"Ricci"}]
        
        for prof in self.prof:
            self.combo.addItem(prof["nome"] + " " + prof["cognome"])
        
        for studente in self.studenti:
            self.comboS.addItem(studente["nome"] + " " + studente["cognome"])
        
        self.oreProf = self.findChild(QLabel, "labelOre")
        self.textedit = self.findChild(QLineEdit, "lineEditInsegnanti")
        self.button = self.findChild(QPushButton, "pushButtonInsegnante")
        self.texteditStud = self.findChild(QLineEdit, "lineEditStudente")
        self.buttonStud = self.findChild(QPushButton, "pushButtonStudente")
        self.bCarica = self.findChild(QPushButton, "pushButtonYes")
        self.textOre = self.findChild(QLineEdit, "lineEditOre")
        self.button.clicked.connect(self.clickedBtn)
        self.buttonStud.clicked.connect(self.clickedBtnStud)
        self.bCarica.clicked.connect(self.clickedBtnC)
        self.combo.currentTextChanged.connect(self.impostaOra)
        self.combo.children()
        self.show()
 
    def clickedBtn(self):
        self.combo.setCurrentText(self.textedit.text());
    def clickedBtnStud(self):
        self.comboS.setCurrentText(self.texteditStud.text());
    
    def clickedBtnC(self):
        self.prof[self.combo.currentText()] = self.textOre.text()
        self.oreResidue[self.combo.currentText()] -= int(self.textOre.text())
        self.profStudente[self.combo.currentText()] = self.comboS.currentText()
        print(self.prof)
        print(self.profStudente)
        print(self.oreResidue)
        
    def impostaOra(self):
        for insegnante in self.prof:
            if(self.combo.currentText() == insegnante["nome"] + " " insegnante["cognome"]):
                self.oreProf.setText(str(self.insegnante["oreResidue"]))
        
app = QApplication(sys.argv)
window = UI()
app.exec_()