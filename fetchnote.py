#!C:\Python35-32\python.exe
import cgi, cgitb, sqlite3

form = cgi.FieldStorage() 
conn = sqlite3.connect('trackit.db')

cursor = conn.execute("SELECT NOTE FROM NOTES where ID=(SELECT MAX(ID)  FROM NOTES);")
data = cursor.fetchall();



print ("Content-Type:text/html \r\n\r\n")
print (data[0][0])

