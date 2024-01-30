"""
This script retrieves the list of all cities in a database
"""
import MySQLdb
import sys
def list_cities(username,password,database):
    """
    This function retrieves a list of all cities in a database
    """
    myconnect = MySQLdb.connect(host ="localhost",port =3306,user =database,passwd=password,db=database)
    cursor = myconnect.cursor()
    cursor.execute("SELECT * FROM cities ORDER BY id ASC")
    myrows = cursor.fetchall()
    for row in myrows:
        print(row)
    cursor.close()
    myconnect.close()
if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    list_cities(username,password,database)
