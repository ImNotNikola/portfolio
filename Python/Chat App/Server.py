import socket
from threading import Thread

host = 'localhost'
port = 8080
clients = {}
addresses = {}
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind((host,port))

def handle_clients(conn,address):
    name = conn.recv(512).decode()
    welcome = "Hello " + name + " type #quit to leave the chat."
    conn.send(bytes(welcome, "utf8"))
    msg = name + " Has joined the chat"
    broadcast(bytes(msg, "utf8"))
    clients[conn] = name

    while True:
        msg = conn.recv(1024)
        if msg != bytes("#quit", "utf8"):
            broadcast(msg, name)
        else:
            conn.send(bytes("#quit","utf8"))
            conn.close()
            del clients[conn]
            broadcast(bytes(f"{name} has left the chat.", "utf8"))


def broadcast(msg, prefix="", ):
    for client in clients:
        client.send(bytes(prefix, "utf8") + msg)


def accept_client_connections():
    while True:
        client_conn, client_address = sock.accept()
        print(f"{client_address} has connected!")
        client_conn.send("Welcome to the chat, please type your name: ".encode('utf8'))
        addresses[client_conn] = client_address

        Thread(target = handle_clients,args = (client_conn, client_address)).start()

if __name__ == "__main__":
    sock.listen(1)
    print(f"The server is running on port {port}")

    t1 = Thread(target=accept_client_connections)
    t1.start()
    t1.join()
