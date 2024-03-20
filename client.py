import socket


HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

def send(HOST, PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        message = input("Enter message: ")
        # s.sendall(message.encode("utf-32"))
        data = s.recv(1024)
        while data:
            s.sendall(message.encode("utf-32"))
            print(f"Received {data!r}")


# print(f"Received {data!r}")

if __name__ == "__main__":
    send(HOST, PORT)