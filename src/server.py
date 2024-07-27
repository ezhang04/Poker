import socket
from _thread import *
import sys

'''Server IP address is the IP address of the server that is hosting the game.'''
server = "192.168.1.185"
port = 5555

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    socket.bind((server, port))
except socket.error as msg:
    print("Socket creation error: " + str(msg))

socket.listen(2)
print("Waiting for a connection, Server Started")

def threaded_client(connection):
    reply = ""
    while True:
        try:
            data = connection.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", reply)
                print("Sending: ", reply)
            connection.sendall(str.encode(reply))
        except:
            break

while True:
    conn, addr = socket.accept()
    print("Connected to: ", addr)
    start_new_thread(threaded_client, (conn, ))