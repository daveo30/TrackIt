#!C:\Python35-32\python.exe
import cgi, cgitb, sqlite3

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

conn = sqlite3.connect('trackit.db')
#conn.execute("CREATE TABLE IF NOT EXISTS GOAL(ID INTEGER PRIMARY KEY AUTOINCREMENT ,GNAME TEXT NOT NULL,"+
					#"GTIME INTEGER NOT NULL, GSTATUS INTEGER NOT NULL DEFAULT 0, GST TEXT, T1NAME TEXT NOT NULL, T1TIME INTEGER NOT NULL, T1STATUS INTEGER NOT NULL  DEFAULT 0,T1FT TEXT, T2NAME TEXT NOT NULL,"
					#+"T2TIME INTEGER NOT NULL,T2STATUS INTEGER NOT NULL  DEFAULT 0, T2FT TEXT, T3NAME TEXT NOT NULL, "
					#+"T3TIME INTEGER NOT NULL, T3STATUS INTEGER NOT NULL  DEFAULT 0, T3FT TEXT);")


gname= form.getvalue('g1name')

t1check= form.getvalue('target11')
#t2check= form.getvalue('target21')
#t3check= form.getvalue('target31')


tftval = form.getvalue('targtime')

print("Content-type:text/html\n\n")
print('<html>')
print('<head>')
print('<title>Result</title>')
print ('</head>')
print ('<body>')

try:
	
	if t1check is not None:
		print(tftval)
		conn.execute("UPDATE GOAL SET T1FT = '"+tftval+"' WHERE GNAME= '"+gname+"';")

		conn.commit()
		print ("Done!!")
	
except:
	print ("Error!")

print ('</body>')
print ('</html>')