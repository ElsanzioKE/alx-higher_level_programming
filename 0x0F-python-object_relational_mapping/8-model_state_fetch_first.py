#!/usr/bin/python3
"""
Script that prints the first sate object from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # DAtabase connection params 
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    # Connection to MySQL server running on localhost at port 3306
    engine = create_engine('mysql+mysql://{}:{}@localhost:3306/{}'.format(username, password, database_name), pool_pre_ping=True)

    # Create a configured session class
    Session = Session()

    # Query the database fot the first state object
    first_state = session.query(State).order_by(State.id).first()

    # Check if the result is None
    if first_state is None:
        print("Nothing/n")
    else:
        print("{}: {}".format(first_state.id, first_state.name))

    # close the session 
    session.close()
