"""a script that takes in the name of a state
 as an argument and lists all cities of that state, using the database hbtn_0e_4_usa"""
import MySQLdb
import sys
def all_cities(username,password,database,state_name):
    """
    a function that takes in the name of a state as an argument and lists all cities of that state, 
    using the database hbtn_0e_4_usa
    """
    connection =MySQLdb.connect(host="localhost",port = 3306,user=username,passwd =password,db=database)
    cursor =connection.cursor()
    querry=     """
                SELECT cities.name,cities.id,states.name
                FROM cities
                JOIN states ON cities.state_id = states.id
                WHERE states.name = %s
                ORDER BY cities.id ASC

                """
    cursor.execute(querry,(state_name,))
    myrows = cursor.fetchall()
    for rows in myrows:
        print(rows)
    cursor.close()
    connection.close()
if __name__ == "__main__":
    if len(sys.argv)!=5:
        sys.exit(1)
    username = sys.argv[1]
    password= sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
    all_cities(username,password,database,state_name)    
    
    