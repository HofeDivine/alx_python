"""
A script that list the name of states that starts with N in a certain database 
Its takes username ,password, database as arguments
"""
import MySQLdb
import sys

def list_N_states(username,password,database):
    """
    A function that list the states starting with N
    It uses .connect() method of MYSQLdb module to connect python script to mysql
    """
    myconnect = MySQLdb.connect(host ="localhost",port =3306,user =username,passwd =password,database =database)
    cursor1 = myconnect.cursor()
    cursor1.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    myrows = cursor1.fetchall()
    for rows in myrows:
         
            print(rows)
    cursor1.close
    myconnect.close

if __name__ == "__main__":
        if len(sys.argv) != 4:
            sys.exit(1)
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        list_N_states(username,password,database)
