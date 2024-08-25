import socket
from _thread import *

server = "ipv4 address"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as msg:
    str(msg)

s.listen(2)
print("Server initiated, waiting for connection")

def threaded_client(conn):
    conn.send(str.encode("Connected"))
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Connection closed")
                break
            else:
                print("Received: " + reply)
                print("Sending " + reply)
            conn.sendall(str.encode(reply))

        except:
            break

    print("Connection closed")
    conn.close()

while True:
    conn, addr = s.accept()
    print("Connection established: " + addr)
    start_new_thread(threaded_client, (conn,))