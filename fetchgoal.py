#!C:\Python35-32\python.exe
import cgi, cgitb, sqlite3

form = cgi.FieldStorage() 
conn = sqlite3.connect('trackit.db')

cursor = conn.execute("SELECT GNAME, GTIME, T1NAME, T1TIME, T2NAME, T2TIME, T3NAME, T3TIME FROM GOAL where ID=(SELECT MAX(ID)  FROM GOAL);")
data = cursor.fetchall();
cursor1 = conn.execute("SELECT GNAME, GTIME, T1NAME, T1TIME, T2NAME, T2TIME, T3NAME, T3TIME FROM GOAL where ID=(SELECT MAX(ID)-1  FROM GOAL);")
data1 =cursor1.fetchall();
cursor2 = conn.execute("SELECT GNAME, GTIME, T1NAME, T1TIME, T2NAME, T2TIME, T3NAME, T3TIME FROM GOAL where ID=(SELECT MAX(ID)-2  FROM GOAL);")
data2 =cursor2.fetchall();

print ("Content-Type:text/html \r\n\r\n")
for i in range(0,7):
	print (data[0][i])
	print (",")

for i in range(0,7):
	print (data1[0][i])
	print (",")
	
for i in range(0,7):
	print (data2[0][i])
	print (",")