#!/usr/bin/python 
import sqlite3 
conn = sqlite3.connect('test.db')
print ("Opened database successfully");
conn.execute('''CREATE TABLE NOTES
 (ID INT PRIMARY KEY     NOT NULL, 
  NOTE   TEXT    NOT NULL);''')
print ("Table created successfully"); 
conn.close()    