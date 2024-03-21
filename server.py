import socket
# import client


# sock = socket.sock_STREAM

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)


def recieve(HOST, PORT):
    # creating server socket as s via TCP/IP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # binds the socket to the specified port and IP
        s.bind((HOST, PORT))

        # instructing the server to listen for connection requests (breaks if no connection)
        s.listen()

        # assigns the server socket to conn and client IP and Port to addr. s.accept() completes the handshake
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            print(f"let's see what conn is:  {conn}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                data.decode("utf-32")
                # conn.sendall(data)
                print(data.decode('utf-32'))





if __name__ == "__main__":
    recieve(HOST, PORT)