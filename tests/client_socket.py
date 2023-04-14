import socket

def client_script():
    # Connect to the server socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("localhost", port))
    nickName = input("Please enter your nickname: ")
    client_socket.send(nickName.encode())

    while True:
        # Send a message to the server
        message = input("Enter a message to send to the server (q to quit): ")
        if message == 'q':
            break
        client_socket.send(message.encode())
        # Receive a message from the server
        data = client_socket.recv(1024)
        print("Received message from server:", data.decode())

    # Close the client socket
    client_socket.close()

if __name__ == "__main__":
    port = int(input("Enter the server port: "))
    client_script()
