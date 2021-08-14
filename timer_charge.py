from datetime import datetime
import sqlite3
from playsound import playsound


def date_to_s(a): #example 2021-01-22,12:40:13
    year = int(a[0] + a[1] + a[2] + a[3]) * 31536000
    day = int(a[8] + a[9]) * 86400
    hour = int(a[11] + a[12]) * 3600
    minute = int(a[14]+a[15]) * 60
    s = int(a[17] + a[18])
    month = int(a[5] + a[6])
    if a == 1 or a == 3 or a == 5 or a == 7 or a == 8 or a == 10 or a == 12:
        month = month * 31 * 86400
    elif a == 2:
        month = month * 29 * 86400
    else:
        month = month * 30 * 86400
    b = year + day + hour + month + minute + s
    return b
     
    
    
    

def start():
    conn = sqlite3.connect('files/Game_info.db') #connect to database
    cur = conn.cursor()
    cur.execute("SELECT * FROM info_cc WHERE rowid=1") #for sql codes : SELECT user 's level 
    cc = cur.fetchall()

    if cc[0][2] is None:
        now = datetime.now()
        sd = now.strftime("%Y-%m-%d,%H:%M:%S")
        cur.execute("UPDATE info_cc SET time_charge='" + sd + "' WHERE rowid=1;")
        conn.commit()
        conn.close()
        return None
    
    else:
        now = datetime.now()
        sd = now.strftime("%Y-%m-%d,%H:%M:%S")

        
        sub_1 = (date_to_s(sd) - date_to_s(cc[0][2])) // 1200
        sub_2 = (date_to_s(sd) - date_to_s(cc[0][2])) % 1200

        if sub_1 != 0:
            cur.execute("UPDATE info_cc SET time_charge='" + sd + "' WHERE rowid=1;")
            conn.commit()
            conn.close()

        conn = sqlite3.connect('files/Game_info.db') #connect to database
        cur = conn.cursor()
        
        if cc[0][1] + sub_1 >= 10:
            cur.execute("UPDATE info_cc SET charge=10 WHERE rowid=1;")
            conn.commit()
            conn.close()
        else:
            cur.execute("UPDATE info_cc SET charge=" + str(cc[0][1] + sub_1) + " WHERE rowid=1;")
            conn.commit()
            conn.close()
        return sub_2

def main():
    conn = sqlite3.connect('files/Game_info.db') #connect to database
    cur = conn.cursor()
    cur.execute("SELECT * FROM info_cc WHERE rowid=1") #for sql codes : SELECT user 's level 
    cc = cur.fetchall()
    if cc[0][1] == 10:
        return 0
    else:
        now = datetime.now()
        sd = now.strftime("%Y-%m-%d,%H:%M:%S")
        
        cur.execute("UPDATE info_cc SET time_charge='" + sd + "' WHERE rowid=1;")
        cur.execute("UPDATE info_cc SET charge='" + str(cc[0][1] + 1) + "' WHERE rowid=1;")
        playsound('Sounds/add_charge.wav')

        conn.commit()
        conn.close()

        
        










    










