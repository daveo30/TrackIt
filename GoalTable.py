#!C:\Python35-32\python.exe
import cgi, cgitb, sqlite3

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

conn = sqlite3.connect('trackit.db')
conn.execute("CREATE TABLE IF NOT EXISTS GOAL(ID INTEGER PRIMARY KEY AUTOINCREMENT ,GNAME TEXT NOT NULL,"+
					"GTIME INTEGER NOT NULL, GSTATUS INTEGER NOT NULL DEFAULT 0, GST TEXT, T1NAME TEXT NOT NULL, T1TIME INTEGER NOT NULL, T1STATUS INTEGER NOT NULL  DEFAULT 0, T2NAME TEXT NOT NULL,"
					+"T2TIME INTEGER NOT NULL,T2STATUS INTEGER NOT NULL  DEFAULT 0, T3NAME TEXT NOT NULL, "
					+"T3TIME INTEGER NOT NULL, T3STATUS INTEGER NOT NULL  DEFAULT 0);")


goalname = form.getvalue('gname')
goaltime = form.getvalue('gtime')


t1name = form.getvalue('t1name')
t1time = form.getvalue('t1time')


t2name = form.getvalue('t2name')
t2time = form.getvalue('t2time')

t3name = form.getvalue('t3name')
t3time = form.getvalue('t3time')
 
gstval = form.getvalue('t')
print("Content-type:text/html\n\n")
print('<html>')
print('<head>')
print('<title>Result</title>')
print ('</head>')
print ('<body>')

try:
	conn.execute("INSERT INTO GOAL(GNAME, GTIME, GST, T1NAME, T1TIME, T2NAME, T2TIME, T3NAME, T3TIME) VALUES('"+goalname+"', '"+goaltime+"', '"+gstval+"', '"+t1name+"', '"+t1time+"', '"+t2name+"', '"+t2time+"', '"+t3name+"', '"+t3time+"');")

	conn.commit()
	print ("Done!!")
except:
	print ("Error!")

print ('</body>')
print ('</html>')