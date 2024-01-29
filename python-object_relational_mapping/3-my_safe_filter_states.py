"""
 in this script we are retrieving the values of a state safe from mysql injections"""
import MySQLdb
import sys
def display_state_nameI(username,password,database,state_name_searched):
    """
    this the fuction that retrieve the values of states from a given database
    """
    myconnect = MySQLdb.connect(host = "localhost", port = 3306,user= username,passwd=password)
    cursor = myconnect.cursor()
    querry = " SELECT * FROM states WHERE BINARY name = '{}'ORDER BY id ASC".format(state_name_searched)
    cursor.execute(querry)
    myrows = cursor.fetchall()
    for row in myrows:
        print(row)
        cursor.close()
        myconnect.close()

if __name__ == "__main__":
    if len(sys.argv)!= 5:
        sys.exit(1)
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name_searched = sys.argv[4]
    display_state_nameI(username,password,database,state_name_searched)