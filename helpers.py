import os
import pickle

def pickle_users(users):
    """
    takes a python object and saves it as a pickled file
    """

    file_path = "./users.pickle"

    with open(file_path, 'wb') as file:
        pickle.dump(users, file)

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
    
    return users
