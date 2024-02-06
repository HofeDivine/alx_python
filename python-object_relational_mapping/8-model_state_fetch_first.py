"""
a script that prints the first State object from 
the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
def first_states(username,password,database):
    """
    a script that prints the first State object from the 
    database hbtn_0e_6_usa
    """
    path = "myqsl://{}:{}@localhost:3306/{}".format(username,password,database)
    engine = create_engine(path)
    Session = sessionmaker(bind=engine)
    session = Session()
    first_states = session.query(State).order_by(State.id).first()
    if first_states is None:
        print("Nothing")   
    else:
        print(f"{first_states.id}: {first_states.name}") 
if __name__ == "__main__":
    if len(sys.argv)!=4:
        sys.exit(1)
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    first_states(username,password,database)

