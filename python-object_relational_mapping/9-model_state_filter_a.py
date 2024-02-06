"""
 a script that lists all State objects that contain the letter a from 
 the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
def a_states(username,password,database):
    """
     a function that lists all State objects that 
     contain the letter a from the database hbtn_0e_6_usa
    """
    path = "mysql://{}:{}@localhost:3306/{}".format(username,password,database)
    engine = create_engine(path)
    Session = sessionmaker(bind=engine)
    session = Session()
    a_states = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()
    for state in a_states:
        print(f"{state.id}: {state.name}")

    
    session.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    a_states(username, password, database)