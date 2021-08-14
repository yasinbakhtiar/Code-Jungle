from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox ,QFileDialog
from gui_main import *
import os
import platform
import sqlite3
import datetime
from playsound import playsound
import timer_charge
from store import *
from setting import *

class Main(Ui_MainWindow,store,setting):
    
    #teach 1
    def get_teach1(self):
        self.conn = sqlite3.connect('files/Game_info.db') #connect to database
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT * FROM info_play WHERE rowid=1") #for sql codes : SELECT user 's level 
        self.level = self.cur.fetchall()
        if self.level[0][0] == 1:
            #check charge
            self.cur.execute("SELECT * FROM info_cc WHERE rowid=1")
            self.coin = self.cur.fetchall()
            if self.coin[0][1] == 0:
                self.conn.commit()
                self.conn.close()
                self.msgBox = QMessageBox()
                self.msgBox.setIcon(QMessageBox.Warning)
                self.msgBox.setText("شارژ شما کافي نيست")
                self.msgBox.setWindowTitle("خطا")
                self.msgBox.exec()
                return 0
            os.system("start files/teach/install_python.mp4")
            self.cur.execute("UPDATE info_play SET level=2 WHERE rowid=1")
            #add coin
            self.cur.execute("SELECT * FROM info_cc WHERE rowid=1")
            self.coin = self.cur.fetchall()
            self.cur.execute("UPDATE info_cc SET Coin=" + str(self.coin[0][0] + 1) + " WHERE rowid=1;")
            #sub charge
            self.cur.execute("UPDATE info_cc SET charge=" + str(self.coin[0][1] - 1) + " WHERE rowid=1;")
            playsound('Sounds/add_charge.wav')
            
        elif self.level[0][0] > 1:
            os.system("start files/teach/install_python.mp4")
        elif self.level[0][0] < 1:
            self.msgBox = QMessageBox()
            self.msgBox.setIcon(QMessageBox.Warning)
            self.msgBox.setText("شما اجازه ورود به اين مرحله را نداريد.")
            self.msgBox.setWindowTitle("خطا")
            self.msgBox.exec()
        
        self.conn.commit()
        self.conn.close()#close database
        
    #python installer  
    def get_pythoninstaller(self):
        os.system("start files/python_64.exe")

    #teach 3
    def get_teach2(self):
        
        self.conn = sqlite3.connect('files/Game_info.db') #connect to database
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT * FROM info_play WHERE rowid=1") #for sql codes : SELECT user 's level 
        self.level = self.cur.fetchall()
        if self.level[0][0] == 2:
            #check charge
            self.cur.execute("SELECT * FROM info_cc WHERE rowid=1")
            self.coin = self.cur.fetchall()
            if self.coin[0][1] == 0:
                self.conn.commit()
                self.conn.close()
                self.msgBox = QMessageBox()
                self.msgBox.setIcon(QMessageBox.Warning)
                self.msgBox.setText("شارژ شما کافي نيست")
                self.msgBox.setWindowTitle("خطا")
                self.msgBox.exec()
                return 0
            os.system("start files/teach/1.mp4")
            self.cur.execute("UPDATE info_play SET level=3 WHERE rowid=1")
            #add coin
            self.cur.execute("SELECT * FROM info_cc WHERE rowid=1")
            self.coin = self.cur.fetchall()
            self.cur.execute("UPDATE info_cc SET Coin=" + str(self.coin[0][0] + 1) + " WHERE rowid=1;")
            #sub charge
            self.cur.execute("UPDATE info_cc SET charge=" + str(self.coin[0][1] - 1) + " WHERE rowid=1;")
            playsound('Sounds/add_charge.wav')
            
        elif self.level[0][0] > 2:
            os.system("start files/teach/1.mp4")
        elif self.level[0][0] < 2:
            self.msgBox = QMessageBox()
            self.msgBox.setIcon(QMessageBox.Warning)
            self.msgBox.setText("شما اجازه ورود به اين مرحله را نداريد.")
            self.msgBox.setWindowTitle("خطا")
            self.msgBox.exec()
        
        self.conn.commit()
        self.conn.close()#close database
        
    def get_level1(self):
        self.conn = sqlite3.connect('files/Game_info.db') #connect to database
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT * FROM info_play WHERE rowid=1") #for sql codes : SELECT user 's level 
        self.level = self.cur.fetchall()
        if self.level[0][0] == 3:
            #check charge
            self.cur.execute("SELECT * FROM info_cc WHERE rowid=1")
            self.coin = self.cur.fetchall()
            if self.coin[0][1] == 0:
                self.conn.commit()
                self.conn.close()
                self.msgBox = QMessageBox()
                self.msgBox.setIcon(QMessageBox.Warning)
                self.msgBox.setText("شارژ شما کافي نيست")
                self.msgBox.setWindowTitle("خطا")
                self.msgBox.exec()
                return 0
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            self.file = QFileDialog.getOpenFileName(None,"بارگذاري فايل", "","Python Files (*.py)", options=options)
            #open file
            if self.file[0] == '':
                return 0
            self.open_file = open(str(self.file[0]))
            self.text = "from Game import *" + '\n' + "main()" + '\n' + self.open_file.read() + '\n' + "check()"
            self.new_file = open("Games/1/play.py","w")
            self.new_file.write(self.text)
            self.new_file.close()
            os.system("1.cmd")
            #sub charge
            self.cur.execute("UPDATE info_cc SET charge=" + str(self.coin[0][1] - 1) + " WHERE rowid=1;")
            playsound('Sounds/add_charge.wav')
            self.conn.commit()
            self.conn.close()
        
        elif self.level[0][0] > 3:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            self.file = QFileDialog.getOpenFileName(None,"بارگذاري فايل", "","Python Files (*.py)", options=options)
            #open file
            if self.file[0] == '':
                return 0
            self.open_file = open(str(self.file[0]))
            self.text = "from Game import *" + '\n' + "main()" + '\n' + self.open_file.read() + '\n' + "check()"
            self.new_file = open("Games/1/play.py","w")
            self.new_file.write(self.text)
            self.new_file.close()
            os.system("1.cmd")
        
        elif self.level[0][0] < 3:
            self.msgBox = QMessageBox()
            self.msgBox.setIcon(QMessageBox.Warning)
            self.msgBox.setText("شما اجازه ورود به اين مرحله را نداريد.")
            self.msgBox.setWindowTitle("خطا")
            self.msgBox.exec()
            
            



            
    def get_picture_1(self):
        self.conn = sqlite3.connect('files/Game_info.db') #connect to database
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT * FROM info_play WHERE rowid=1") #for sql codes : SELECT user 's level 
        self.level = self.cur.fetchall()
        if self.level[0][0] >= 3:
            self.cur.execute("SELECT * FROM info_cc WHERE rowid=1")
            self.coin = self.cur.fetchall()
            if self.coin[0][1] == 0:
                self.conn.commit()
                self.conn.close()
                self.msgBox = QMessageBox()
                self.msgBox.setIcon(QMessageBox.Warning)
                self.msgBox.setText("شارژ شما کافي نيست")
                self.msgBox.setWindowTitle("خطا")
                self.msgBox.exec()
                return 0
            else:
                os.system("start Games/1/about_1.png")
        else:
            self.msgBox = QMessageBox()
            self.msgBox.setIcon(QMessageBox.Warning)
            self.msgBox.setText("شما اجازه ورود به اين عکس را نداريد")
            self.msgBox.setWindowTitle("خطا")
            self.msgBox.exec()






    def get_teach3(self):        
        self.conn = sqlite3.connect('files/Game_info.db') #connect to database
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT * FROM info_play WHERE rowid=1") #for sql codes : SELECT user 's level 
        self.level = self.cur.fetchall()
        if self.level[0][0] == 4:
            #check charge
            self.cur.execute("SELECT * FROM info_cc WHERE rowid=1")
            self.coin = self.cur.fetchall()
            if self.coin[0][1] == 0:
                self.conn.commit()
                self.conn.close()
                self.msgBox = QMessageBox()
                self.msgBox.setIcon(QMessageBox.Warning)
                self.msgBox.setText("شارژ شما کافي نيست")
                self.msgBox.setWindowTitle("خطا")
                self.msgBox.exec()
                return 0
            os.system("start files/teach/2.mp4")
            self.cur.execute("UPDATE info_play SET level=5 WHERE rowid=1")
            #add coin
            self.cur.execute("SELECT * FROM info_cc WHERE rowid=1")
            self.coin = self.cur.fetchall()
            self.cur.execute("UPDATE info_cc SET Coin=" + str(self.coin[0][0] + 1) + " WHERE rowid=1;")
            #sub charge
            self.cur.execute("UPDATE info_cc SET charge=" + str(self.coin[0][1] - 1) + " WHERE rowid=1;")
            playsound('Sounds/add_charge.wav')
            
        elif self.level[0][0] > 4:
            os.system("start files/teach/2.mp4")
        elif self.level[0][0] < 4:
            self.msgBox = QMessageBox()
            self.msgBox.setIcon(QMessageBox.Warning)
            self.msgBox.setText("شما اجازه ورود به اين مرحله را نداريد.")
            self.msgBox.setWindowTitle("خطا")
            self.msgBox.exec()
        
        self.conn.commit()
        self.conn.close()#close database


    def get_picture_2(self):
        self.conn = sqlite3.connect('files/Game_info.db') #connect to database
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT * FROM info_play WHERE rowid=1") #for sql codes : SELECT user 's level 
        self.level = self.cur.fetchall()
        if self.level[0][0] >= 5:
            self.cur.execute("SELECT * FROM info_cc WHERE rowid=1")
            self.coin = self.cur.fetchall()
            if self.coin[0][1] == 0:
                self.conn.commit()
                self.conn.close()
                self.msgBox = QMessageBox()
                self.msgBox.setIcon(QMessageBox.Warning)
                self.msgBox.setText("شارژ شما کافي نيست")
                self.msgBox.setWindowTitle("خطا")
                self.msgBox.exec()
                return 0
            else:
                os.system("start Games/2/about_2.png")
        else:
            self.msgBox = QMessageBox()
            self.msgBox.setIcon(QMessageBox.Warning)
            self.msgBox.setText("شما اجازه ورود به اين عکس را نداريد")
            self.msgBox.setWindowTitle("خطا")
            self.msgBox.exec()

    def get_level2(self):
        self.conn = sqlite3.connect('files/Game_info.db') #connect to database
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT * FROM info_play WHERE rowid=1") #for sql codes : SELECT user 's level 
        self.level = self.cur.fetchall()
        if self.level[0][0] == 5:
            #check charge
            self.cur.execute("SELECT * FROM info_cc WHERE rowid=1")
            self.coin = self.cur.fetchall()
            if self.coin[0][1] == 0:
                self.conn.commit()
                self.conn.close()
                self.msgBox = QMessageBox()
                self.msgBox.setIcon(QMessageBox.Warning)
                self.msgBox.setText("شارژ شما کافي نيست")
                self.msgBox.setWindowTitle("خطا")
                self.msgBox.exec()
                return 0
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            self.file = QFileDialog.getOpenFileName(None,"بارگذاري فايل", "","Python Files (*.py)", options=options)
            #open file
            if self.file[0] == '':
                return 0
            self.open_file = open(str(self.file[0]))
            self.text = "from Game import *" + '\n' + "main()" + '\n' + self.open_file.read() + '\n' + "check()"
            self.new_file = open("Games/2/play.py","w")
            self.new_file.write(self.text)
            self.new_file.close()
            os.system("2.cmd")
            #sub charge
            self.cur.execute("UPDATE info_cc SET charge=" + str(self.coin[0][1] - 1) + " WHERE rowid=1;")
            playsound('Sounds/add_charge.wav')
            self.conn.commit()
            self.conn.close()
        
        elif self.level[0][0] > 5:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            self.file = QFileDialog.getOpenFileName(None,"بارگذاري فايل", "","Python Files (*.py)", options=options)
            #open file
            if self.file[0] == '':
                return 0
            self.open_file = open(str(self.file[0]))
            self.text = "from Game import *" + '\n' + "main()" + '\n' + self.open_file.read() + '\n' + "check()"
            self.new_file = open("Games/2/play.py","w")
            self.new_file.write(self.text)
            self.new_file.close()
            os.system("2.cmd")
        
        elif self.level[0][0] < 5:
            self.msgBox = QMessageBox()
            self.msgBox.setIcon(QMessageBox.Warning)
            self.msgBox.setText("شما اجازه ورود به اين مرحله را نداريد.")
            self.msgBox.setWindowTitle("خطا")
            self.msgBox.exec()
            
    def get_picture_3(self):
        self.conn = sqlite3.connect('files/Game_info.db') #connect to database
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT * FROM info_play WHERE rowid=1") #for sql codes : SELECT user 's level 
        self.level = self.cur.fetchall()
        if self.level[0][0] >= 7:
            self.cur.execute("SELECT * FROM info_cc WHERE rowid=1")
            self.coin = self.cur.fetchall()
            if self.coin[0][1] == 0:
                self.conn.commit()
                self.conn.close()
                self.msgBox = QMessageBox()
                self.msgBox.setIcon(QMessageBox.Warning)
                self.msgBox.setText("شارژ شما کافي نيست")
                self.msgBox.setWindowTitle("خطا")
                self.msgBox.exec()
                return 0
            else:
                os.system("start Games/3/about_3.png")
        else:
            self.msgBox = QMessageBox()
            self.msgBox.setIcon(QMessageBox.Warning)
            self.msgBox.setText("شما اجازه ورود به اين عکس را نداريد")
            self.msgBox.setWindowTitle("خطا")
            self.msgBox.exec()
            
    def get_level3(self):
          self.conn = sqlite3.connect('files/Game_info.db') #connect to database
          self.cur = self.conn.cursor()
          self.cur.execute("SELECT * FROM info_play WHERE rowid=1") #for sql codes : SELECT user 's level 
          self.level = self.cur.fetchall()
          if self.level[0][0] == 7:
              #check charge
              self.cur.execute("SELECT * FROM info_cc WHERE rowid=1")
              self.coin = self.cur.fetchall()
              if self.coin[0][1] == 0:
                  self.conn.commit()
                  self.conn.close()
                  self.msgBox = QMessageBox()
                  self.msgBox.setIcon(QMessageBox.Warning)
                  self.msgBox.setText("شارژ شما کافي نيست")
                  self.msgBox.setWindowTitle("خطا")
                  self.msgBox.exec()
                  return 0
              options = QFileDialog.Options()
              options |= QFileDialog.DontUseNativeDialog
              self.file = QFileDialog.getOpenFileName(None,"بارگذاري فايل", "","Python Files (*.py)", options=options)
              #open file
              if self.file[0] == '':
                  return 0
              self.open_file = open(str(self.file[0]))
              self.text = "from Game import *" + '\n' + "main()" + '\n' + self.open_file.read() + '\n' + "check()"
              self.new_file = open("Games/3/play.py","w")
              self.new_file.write(self.text)
              self.new_file.close()
              os.system("3.cmd")
              #sub charge
              self.cur.execute("UPDATE info_cc SET charge=" + str(self.coin[0][1] - 1) + " WHERE rowid=1;")
              playsound('Sounds/add_charge.wav')
              self.conn.commit()
              self.conn.close()
        
          elif self.level[0][0] > 7:
              options = QFileDialog.Options()
              options |= QFileDialog.DontUseNativeDialog
              self.file = QFileDialog.getOpenFileName(None,"بارگذاري فايل", "","Python Files (*.py)", options=options)
              #open file
              if self.file[0] == '':
                  return 0
              self.open_file = open(str(self.file[0]))
              self.text = "from Game import *" + '\n' + "main()" + '\n' + self.open_file.read() + '\n' + "check()"
              self.new_file = open("Games/3/play.py","w")
              self.new_file.write(self.text)
              self.new_file.close()
              os.system("3.cmd")
         
          elif self.level[0][0] < 7:
              self.msgBox = QMessageBox()
              self.msgBox.setIcon(QMessageBox.Warning)
              self.msgBox.setText("شما اجازه ورود به اين مرحله را نداريد.")
              self.msgBox.setWindowTitle("خطا")
              self.msgBox.exec()
            

    def get_picture_4(self):
        self.conn = sqlite3.connect('files/Game_info.db') #connect to database
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT * FROM info_play WHERE rowid=1") #for sql codes : SELECT user 's level 
        self.level = self.cur.fetchall()
        if self.level[0][0] >= 9:
            self.cur.execute("SELECT * FROM info_cc WHERE rowid=1")
            self.coin = self.cur.fetchall()
            if self.coin[0][1] == 0:
                self.conn.commit()
                self.conn.close()
                self.msgBox = QMessageBox()
                self.msgBox.setIcon(QMessageBox.Warning)
                self.msgBox.setText("شارژ شما کافي نيست")
                self.msgBox.setWindowTitle("خطا")
                self.msgBox.exec()
                return 0
            else:
                os.system("start Games/4/about_4.png")
        else:
            self.msgBox = QMessageBox()
            self.msgBox.setIcon(QMessageBox.Warning)
            self.msgBox.setText("شما اجازه ورود به اين عکس را نداريد")
            self.msgBox.setWindowTitle("خطا")
            self.msgBox.exec()
            



    def get_teach4(self):        
        self.conn = sqlite3.connect('files/Game_info.db') #connect to database
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT * FROM info_play WHERE rowid=1") #for sql codes : SELECT user 's level 
        self.level = self.cur.fetchall()
        if self.level[0][0] == 6:
            #check charge
            self.cur.execute("SELECT * FROM info_cc WHERE rowid=1")
            self.coin = self.cur.fetchall()
            if self.coin[0][1] == 0:
                self.conn.commit()
                self.conn.close()
                self.msgBox = QMessageBox()
                self.msgBox.setIcon(QMessageBox.Warning)
                self.msgBox.setText("شارژ شما کافي نيست")
                self.msgBox.setWindowTitle("خطا")
                self.msgBox.exec()
                return 0
            os.system("start files/teach/3.mp4")
            self.cur.execute("UPDATE info_play SET level=7 WHERE rowid=1")
            #add coin
            self.cur.execute("SELECT * FROM info_cc WHERE rowid=1")
            self.coin = self.cur.fetchall()
            self.cur.execute("UPDATE info_cc SET Coin=" + str(self.coin[0][0] + 1) + " WHERE rowid=1;")
            #sub charge
            self.cur.execute("UPDATE info_cc SET charge=" + str(self.coin[0][1] - 1) + " WHERE rowid=1;")
            playsound('Sounds/add_charge.wav')
            
        elif self.level[0][0] > 6:
            os.system("start files/teach/3.mp4")
        elif self.level[0][0] < 6:
            self.msgBox = QMessageBox()
            self.msgBox.setIcon(QMessageBox.Warning)
            self.msgBox.setText("شما اجازه ورود به اين مرحله را نداريد.")
            self.msgBox.setWindowTitle("خطا")
            self.msgBox.exec()
        
        self.conn.commit()
        self.conn.close()#close database


    def get_teach5(self):        
        self.conn = sqlite3.connect('files/Game_info.db') #connect to database
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT * FROM info_play WHERE rowid=1") #for sql codes : SELECT user 's level 
        self.level = self.cur.fetchall()
        if self.level[0][0] == 8:
            #check charge
            self.cur.execute("SELECT * FROM info_cc WHERE rowid=1")
            self.coin = self.cur.fetchall()
            if self.coin[0][1] == 0:
                self.conn.commit()
                self.conn.close()
                self.msgBox = QMessageBox()
                self.msgBox.setIcon(QMessageBox.Warning)
                self.msgBox.setText("شارژ شما کافي نيست")
                self.msgBox.setWindowTitle("خطا")
                self.msgBox.exec()
                return 0
            os.system("start files/teach/3.mp4")
            self.cur.execute("UPDATE info_play SET level=9 WHERE rowid=1")
            #add coin
            self.cur.execute("SELECT * FROM info_cc WHERE rowid=1")
            self.coin = self.cur.fetchall()
            self.cur.execute("UPDATE info_cc SET Coin=" + str(self.coin[0][0] + 1) + " WHERE rowid=1;")
            #sub charge
            self.cur.execute("UPDATE info_cc SET charge=" + str(self.coin[0][1] - 1) + " WHERE rowid=1;")
            playsound('Sounds/add_charge.wav')
            
        elif self.level[0][0] > 8:
            os.system("start files/teach/4.mp4")
        elif self.level[0][0] < 8:
            self.msgBox = QMessageBox()
            self.msgBox.setIcon(QMessageBox.Warning)
            self.msgBox.setText("شما اجازه ورود به اين مرحله را نداريد.")
            self.msgBox.setWindowTitle("خطا")
            self.msgBox.exec()
        
        self.conn.commit()
        self.conn.close()#close database


    def get_level4(self):
          self.conn = sqlite3.connect('files/Game_info.db') #connect to database
          self.cur = self.conn.cursor()
          self.cur.execute("SELECT * FROM info_play WHERE rowid=1") #for sql codes : SELECT user 's level 
          self.level = self.cur.fetchall()
          if self.level[0][0] == 9:
              #check charge
              self.cur.execute("SELECT * FROM info_cc WHERE rowid=1")
              self.coin = self.cur.fetchall()
              if self.coin[0][1] == 0:
                  self.conn.commit()
                  self.conn.close()
                  self.msgBox = QMessageBox()
                  self.msgBox.setIcon(QMessageBox.Warning)
                  self.msgBox.setText("شارژ شما کافي نيست")
                  self.msgBox.setWindowTitle("خطا")
                  self.msgBox.exec()
                  return 0
              options = QFileDialog.Options()
              options |= QFileDialog.DontUseNativeDialog
              self.file = QFileDialog.getOpenFileName(None,"بارگذاري فايل", "","Python Files (*.py)", options=options)
              #open file
              if self.file[0] == '':
                  return 0
              self.open_file = open(str(self.file[0]))
              self.text = "from Game import *" + '\n' + "main()" + '\n' + self.open_file.read() + '\n' + "check()"
              self.new_file = open("Games/4/play.py","w")
              self.new_file.write(self.text)
              self.new_file.close()
              os.system("4.cmd")
              #sub charge
              self.cur.execute("UPDATE info_cc SET charge=" + str(self.coin[0][1] - 1) + " WHERE rowid=1;")
              playsound('Sounds/add_charge.wav')
              self.conn.commit()
              self.conn.close()
        
          elif self.level[0][0] > 9:
              options = QFileDialog.Options()
              options |= QFileDialog.DontUseNativeDialog
              self.file = QFileDialog.getOpenFileName(None,"بارگذاري فايل", "","Python Files (*.py)", options=options)
              #open file
              if self.file[0] == '':
                  return 0
              self.open_file = open(str(self.file[0]))
              self.text = "from Game import *" + '\n' + "main()" + '\n' + self.open_file.read() + '\n' + "check()"
              self.new_file = open("Games/4/play.py","w")
              self.new_file.write(self.text)
              self.new_file.close()
              os.system("4.cmd")
         
          elif self.level[0][0] < 9:
              self.msgBox = QMessageBox()
              self.msgBox.setIcon(QMessageBox.Warning)
              self.msgBox.setText("شما اجازه ورود به اين مرحله را نداريد.")
              self.msgBox.setWindowTitle("خطا")
              self.msgBox.exec()

    def get_teach6(self):
        self.msgBox = QMessageBox()
        self.msgBox.setIcon(QMessageBox.Warning)
        self.msgBox.setText("منتظر بروزرساني هاي جديد باشيد")
        self.msgBox.setWindowTitle("خبر مهم")
        self.msgBox.exec()
        




        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Main()
    ui.setupUi(MainWindow)
    MainWindow.show()
    #start
    a = timer_charge.start()
    if a is None:
        a = 0    
    #for update charge
    def update_charge():
        conn = sqlite3.connect('files/Game_info.db') #connect to database
        cur = conn.cursor()
        cur.execute("SELECT * FROM info_cc WHERE rowid=1") #for sql codes : SELECT user 's level 
        cc = cur.fetchall()
        ui.charge_label_store.setText(str(cc[0][1]))
        ui.charge_label_home.setText(str(cc[0][1]))
        ui.coin_label_store.setText(str(cc[0][0]))
        ui.coin_label_home.setText(str(cc[0][0]))
    def add_charge():
        global a
        timer_charge.main()
        a = 0
    
    timer = QtCore.QTimer()
    timer.timeout.connect(update_charge)
    timer.start(1000)  # every
    
    timer_2 = QtCore.QTimer()
    timer_2.timeout.connect(add_charge)
    timer_2.start(1200000 - (a * 1000))  # every
    
    sys.exit(app.exec_())
    
