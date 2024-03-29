"""
This script is use to retrieve data from a certain base using python codes in the place of wrinting mysql queries 
"""
import MySQLdb
import sys
def lists_states(username,password, database_name):
    """
    this is the function that list all the states in a database
    
    """
    my_connect = MySQLdb.connect(host="localhost",user=username,port=3306,passwd=password,db=database_name)
    cursor= my_connect.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    data_selected = cursor.fetchall()
    for row in data_selected:
        print(row)

    cursor.close()
    my_connect.close()

if __name__== "__main__":
    if len(sys.argv) !=4:
        sys.exit(1)
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    lists_states(username,password,database_name)
