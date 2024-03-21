import socket
# import server


SERVER_HOST = "127.0.0.1"  # The server's hostname or IP address
SERVER_PORT = 65432  # The port used by the server

def send(SERVER_HOST, SERVER_PORT):
    # creating client socket as s to connect to server, using TCP/IP -- IP = (AF_INET) via TCP = (SOCK_STREAM))
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((SERVER_HOST, SERVER_PORT))
        # data = s.recv(1024)

        #maintaining server connection while messages are sent "bye" to exit the loop
        while True:
            message = input("Enter message: ")
            s.sendall(message.encode("utf-32"))
            if message.lower() == "bye":
                break





if __name__ == "__main__":
    send(SERVER_HOST, SERVER_PORT)

