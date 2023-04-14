import socket
import threading



clients = {}
def handle_client(client_socket):
    nickName = client_socket.recv(1024)
    clients[nickName.decode()] = client_socket
    print(clients)
    connexion = False
    while True:
        try:
            # Receive data from the client socket
            message = client_socket.recv(1024)
            message = message.decode()

            if message.startswith("!connect_to"):
                destinationCall = message.split()[1]
                if destinationCall not in clients.keys():
                    client_socket.send(f"{destinationCall} not connected !".encode())
                else:
                    clients[destinationCall].send(f"{nickName} wants to connect! Accept (Yes/No)?: ".encode())



        except:
            break
    # Close the client socket
    client_socket.close()

def start_server():
    # Create a server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 0))
    server_socket.listen(5)
    host, port = server_socket.getsockname()
    print(f"Server listening on {host}:{port}")
    while True:
        # Accept a client connection
        client_socket, _ = server_socket.accept()
        # Start a new thread to handle the client connection
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

if __name__ == "__main__":
    start_server()
