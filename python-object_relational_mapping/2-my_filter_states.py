"""
A script that returns the values of a an imputed states from a database
"""
import MySQLdb
import sys
def list_states_Name(username,password,database,state_name_searched):
    """
    A function that retrieve the list of values of a certain states
    """
    myconnect = MySQLdb.connect(host ="localhost",port = 3306,user =username,passwd =password,database=database)
    cursor = myconnect.cursor()
    cursor.execute("SELECT * FROM states WHERE BINARY name = '{}'ORDER BY id ASC".format(state_name_searched))
    myrows = cursor.fetchall()
    for rows in myrows:
        print(rows)
    cursor.close
    myconnect.close

if __name__ == "__main__":
    if len(sys.argv) != 5:
        exit(1)
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name_searched = sys.argv[4]
    list_states_Name(password,username,database,state_name_searched)