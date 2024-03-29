"""
This script retrieves the list of all cities in a database
"""
import MySQLdb
import sys
def list_cities(username,password,database):
    """
    This function retrieves a list of all cities in a database
    """
    myconnect = MySQLdb.connect(host ="localhost",port =3306,user =username,passwd=password,db=database)
    cursor = myconnect.cursor()
    cursor.execute("""
            SELECT cities.id, cities.name, states.name
            FROM cities
            INNER JOIN states ON cities.state_id = states.id
            ORDER BY cities.id ASC
        """)
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
