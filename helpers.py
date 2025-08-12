import os
import pickle
import sys

def exit_program():
    """
    exits the program with a code of 0 (success)
    """
    sys.exit(0)

def pickle_users(users):
    """
    takes a python object and saves it as a pickled file
    """

    file_path = "./users.pickle"

    with open(file_path, 'wb') as file:
        pickle.dump(users, file)
    
    print("users pickled")

def unpickle_users():
    """
    takes a pickled file for a particular list name
    and returns the unpickled python object
    """
    file_path = "./users.pickle"

    if not os.path.exists(file_path):
        return None
    
    with open(file_path, 'rb') as file:
        users = pickle.load(file)
    
    print("users unpickled")
    return users
