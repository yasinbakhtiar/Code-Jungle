from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import platform
import sqlite3
from playsound import playsound

class setting:
    def sound_slider_cv(self):
        self.conn = sqlite3.connect('files/Game_info.db') #connect to database
        self.cur = self.conn.cursor()
        self.cur.execute("UPDATE info_setting SET sound = " + str(self.Sound_slider.value()) +" WHERE rowid=1;")
        self.conn.commit()
        self.conn.close()

    def music_slider_cv(self):
        self.conn = sqlite3.connect('files/Game_info.db') #connect to database
        self.cur = self.conn.cursor()
        self.cur.execute("UPDATE info_setting SET music = " + str(self.Music_slider_2.value()) +" WHERE rowid=1;")
        self.conn.commit()
        self.conn.close()

    def boy_1_tc(self):
        self.conn = sqlite3.connect('files/Game_info.db') #connect to database
        self.cur = self.conn.cursor()
        self.cur.execute("UPDATE info_setting SET character = 1 WHERE rowid=1;")
        self.conn.commit()
        self.conn.close()
    def boy_2_tc(self):
        self.conn = sqlite3.connect('files/Game_info.db') #connect to database
        self.cur = self.conn.cursor()
        self.cur.execute("UPDATE info_setting SET character = 2 WHERE rowid=1;")
        self.conn.commit()
        self.conn.close()
    def boy_3_tc(self):
        self.conn = sqlite3.connect('files/Game_info.db') #connect to database
        self.cur = self.conn.cursor()
        self.cur.execute("UPDATE info_setting SET character = 3 WHERE rowid=1;")
        self.conn.commit()
        self.conn.close()
