import MySQLdb as mdb
import getpass
con = mdb.connect(host="localhost", user="root",
					 passwd="root", db="python")

user = raw_input("Username: ")
passwd = getpass.getpass("passwd:")
cur = con.cursor()
cur.execute("select * from users")
rows = cur.fetchall()
	
for row in rows:
	if user==row[1] and passwd==row[2]:
		print "Welcome to Python!!!"
		break
	else:
		print "Your username or password you enter incorrect"
		break
con.close()
