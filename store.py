import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from playsound import playsound
from PyQt5.QtWidgets import QMessageBox

class store:
    def get_store_1(self):
        self.conn = sqlite3.connect('files/Game_info.db') #connect to database
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT * FROM info_cc WHERE rowid=1") #for sql codes : SELECT user 's level 
        self.cc = self.cur.fetchall()
        if self.cc[0][0] >= 10:
            if self.cc[0][1] + 1 > 10:
                self.msgBox = QMessageBox()
                self.msgBox.setIcon(QMessageBox.Warning)
                self.msgBox.setText("شما نمي توانيد اين بسته را خريداري کنيد.")
                self.msgBox.setWindowTitle("خطا")
                self.msgBox.exec()
            else:
                self.cur.execute("UPDATE info_cc SET Coin=" + str(self.cc[0][0] - 10) + " WHERE rowid=1;")
                self.cur.execute("UPDATE info_cc SET charge=" + str(self.cc[0][1] + 1) + " WHERE rowid=1;")
                playsound('Sounds/buy_store.wav')
                self.conn.commit()
                self.conn.close()
        else:
            self.msgBox = QMessageBox()
            self.msgBox.setIcon(QMessageBox.Warning)
            self.msgBox.setText("پول شما کافي نيست")
            self.msgBox.setWindowTitle("خطا")
            self.msgBox.exec()
            
    def get_store_2(self):
        self.conn = sqlite3.connect('files/Game_info.db') #connect to database
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT * FROM info_cc WHERE rowid=1") #for sql codes : SELECT user 's level 
        self.cc = self.cur.fetchall()
        if self.cc[0][0] >= 25:
            if self.cc[0][1] + 3 > 10:
                self.msgBox = QMessageBox()
                self.msgBox.setIcon(QMessageBox.Warning)
                self.msgBox.setText("شما نمي توانيد اين بسته را خريداري کنيد.")
                self.msgBox.setWindowTitle("خطا")
                self.msgBox.exec()
            else:
                self.cur.execute("UPDATE info_cc SET Coin=" + str(self.cc[0][0] - 25) + " WHERE rowid=1;")
                self.cur.execute("UPDATE info_cc SET charge=" + str(self.cc[0][1] + 3) + " WHERE rowid=1;")
                playsound('Sounds/buy_store.wav')
                self.conn.commit()
                self.conn.close()
        else:
            self.msgBox = QMessageBox()
            self.msgBox.setIcon(QMessageBox.Warning)
            self.msgBox.setText("پول شما کافي نيست")
            self.msgBox.setWindowTitle("خطا")
            self.msgBox.exec()

    def get_store_3(self):
        self.conn = sqlite3.connect('files/Game_info.db') #connect to database
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT * FROM info_cc WHERE rowid=1") #for sql codes : SELECT user 's level 
        self.cc = self.cur.fetchall()
        if self.cc[0][0] >= 40:
            if self.cc[0][1] + 5 > 10:
                self.msgBox = QMessageBox()
                self.msgBox.setIcon(QMessageBox.Warning)
                self.msgBox.setText("شما نمي توانيد اين بسته را خريداري کنيد.")
                self.msgBox.setWindowTitle("خطا")
                self.msgBox.exec()
            else:
                self.cur.execute("UPDATE info_cc SET Coin=" + str(self.cc[0][0] - 40) + " WHERE rowid=1;")
                self.cur.execute("UPDATE info_cc SET charge=" + str(self.cc[0][1] + 5) + " WHERE rowid=1;")
                playsound('Sounds/buy_store.wav')
                self.conn.commit()
                self.conn.close()
        else:
            self.msgBox = QMessageBox()
            self.msgBox.setIcon(QMessageBox.Warning)
            self.msgBox.setText("پول شما کافي نيست")
            self.msgBox.setWindowTitle("خطا")
            self.msgBox.exec()

    def get_store_4(self):
        self.conn = sqlite3.connect('files/Game_info.db') #connect to database
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT * FROM info_cc WHERE rowid=1") #for sql codes : SELECT user 's level
        self.cc = self.cur.fetchall()
        if self.cc[0][0] >= 95:
            if self.cc[0][1] + 10 > 10:
                self.msgBox = QMessageBox()
                self.msgBox.setIcon(QMessageBox.Warning)
                self.msgBox.setText("شما نمي توانيد اين بسته را خريداري کنيد.")
                self.msgBox.setWindowTitle("خطا")
                self.msgBox.exec()
            else:
                self.cur.execute("UPDATE info_cc SET Coin=" + str(self.cc[0][0] - 95) + " WHERE rowid=1;")
                self.cur.execute("UPDATE info_cc SET charge=" + str(self.cc[0][1] + 10) + " WHERE rowid=1;")
                playsound('Sounds/buy_store.wav')
                self.conn.commit()
                self.conn.close()
        else:
            self.msgBox = QMessageBox()
            self.msgBox.setIcon(QMessageBox.Warning)
            self.msgBox.setText("پول شما کافي نيست")
            self.msgBox.setWindowTitle("خطا")
            self.msgBox.exec()    
