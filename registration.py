#!C:\Python35-32\python.exe
import cgi, cgitb, sqlite3

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

conn = sqlite3.connect('trackit.db')
conn.execute("CREATE TABLE IF NOT EXISTS NOTES(ID INTEGER PRIMARY KEY AUTOINCREMENT , NOTE   TEXT    NOT NULL);")

note=form.getvalue('note_data') 


print("Content-type:text/html\n\n")
print('<html>')
print('<head>')
print('<title>Result</title>')
print ('</head>')
print ('<body>')

try:
	conn.execute("INSERT INTO NOTES (NOTE) VALUES ( '"+note+"');")	
	conn.commit()
	
except:
	print ("Error!")

print ('</body>')
print ('</html>')
