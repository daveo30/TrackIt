#!C:\Python35-32\python.exe
import cgi, cgitb, sqlite3

form = cgi.FieldStorage() 
conn = sqlite3.connect('trackit.db')

cursor = conn.execute("SELECT GNAME, GTIME, GST, T1NAME, T1TIME, T2NAME, T2TIME, T3NAME, T3TIME FROM GOAL where ID=(SELECT MAX(ID)  FROM GOAL);")
data = cursor.fetchall();



print ("Content-Type:text/html \r\n\r\n")
for i in range(0,7):
	print (data[0][i])
	print (",")

