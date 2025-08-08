# external imports
import os
import zmq
from dotenv import load_dotenv

import helpers
import user

success = "success"
invalid_input = "invalid input"
invalid_login = "invalid login"

def get_env_variables():
    load_dotenv()
    socket_number = os.getenv("PORT_B")
    return socket_number

def set_up_server(socket_number):
    context = zmq.Context()
    socket = context.socket(zmq.REP)  # REP is the reply socket
    socket.bind(f"tcp://*:{socket_number}")
    print(f"User Service listening on tcp://*:{socket_number}...")
    return socket
    
def parse_message(message, users):
    if message["action"] == "new":
        users.addUser(message["username"], message["password"])
        status = success
    elif message["action"] == "login":
        if users.login(message["username"], message["password"]):
            status = success
        else: 
            status = invalid_login
    elif message["action"] == "logout":
        status = success
    else:
        status = invalid_input
    return status, users.active


if __name__ == "__main__":
    socket_number, api_key = get_env_variables()
    socket = set_up_server(socket_number)
    users = helpers.unpickle_users()
    if not users:
        users = user.Users()

    while True:
        # get and parse message
        message = socket.recv_pyobj()
        status, current_user = parse_message(message, users)
        socket.send_pyobj({"status": status, "current_user": current_user})