# Login

import tkinter
import sqlite3

from sqlite3.dbapi2 import Cursor
# from tkinter import *
# import tkinter as tk
from tkinter import messagebox

def login() :
    i = en_id.get()
    p = en_pw.get()

    conn = sqlite3.connect('test.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM member')
    rows = cur.fetchall()
    #print(rows)

    for row in rows :
        if row[0] == i and row[1] == p :
            messagebox.showinfo(row[0] + '님 안녕하세요', '로그인 성공')
            break
        else :
            messagebox.showerror('ID/PW를 확인하세요', '로그인 실패')
            break

    conn.commit()
    conn.close()

# UI
#1) 위젯 생성   2) 위젯 레이아웃 배치
w = tkinter.Tk()
w.title('로그인 실습 v0.5')

lbl_id = tkinter.Label(w, text='ID: ')
lbl_pw = tkinter.Label(w, text='PW: ')
en_id = tkinter.Entry(w)
en_pw = tkinter.Entry(w)
btn_login = tkinter.Button(w, text='LOGIN', command=login)

lbl_id.grid(row=0, column=0)
lbl_pw.grid(row=1, column=0)
en_id.grid(row=0, column=1)
en_pw.grid(row=1, column=1)
btn_login.grid(row=2, column=0, columnspan=2, sticky='nswe')

w.mainloop()



# DB
#1) DB 생성   2) 테이블 생성   3) DML INSERT

#--CREATE TABLE member (
#--id text PRIMARY KEY,
#--pw text NOT NULL,
#--)
#
#--SELECT * FROM member;
#
#--INSERT INTO member (id, pw) VALUES ('alpba', 'bravo');
#--INSERT INTO member (id, pw) VALUES ('charlie', 'delta');
#--INSERT INTO member (id, pw) VALUES ('echo', 'foxtrot');



# BACKEND
#1) 
