#!/usr/bin/python 
import sqlite3
conn = sqlite3.connect('trackittest1.db')
print ("Opened database successfully") 
conn.execute("INSERT INTO GOAL (ID,NAME,TIMELIMIT,COMPLETE) \VALUES (1, 'Finsih Project', 5, 0 )");
conn.execute("INSERT INTO GOAL (ID,NAME,TIMELIMIT,COMPLETE) \VALUES (2, 'Study OS', 3, 0 )");
conn.commit()
print ("Records created successfully")
conn.close()  