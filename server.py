import socket
# import client
import threading


# sock = socket.sock_STREAM

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

# define sender() + reciever() to be called locally in server_main where we can pass conn obj
def sender(conn):
     while True:
        message = input("Enter message: ")
        conn.sendall(message.encode("utf-32"))
        if message.lower() == "bye":
            break

def receiver(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(f"Received: {data.decode("utf-32")}")


def server_main(HOST, PORT):
    # creating server socket as s via TCP/IP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # binds the socket to the specified port and IP
        s.bind((HOST, PORT))

        # instructing the server to listen for connection requests (breaks if no connection)
        s.listen()

        # assigns the server socket to conn and client IP + Port to addr. s.accept() completes the handshake
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            print(f"let's see what conn is:  {conn}")

            # create 2 thread instances to run the sender + receiver functions concurrently
            sender_thread = threading.Thread(target=sender, args=(conn,))
            receiver_thread = threading.Thread(target=receiver, args=(conn,))

            # .start calls the functions on respective threads
            sender_thread.start()
            receiver_thread.start()

            # .join breaks and rejoins the threads, code now runs sequentially
            sender_thread.join()
            receiver_thread.join()




if __name__ == "__main__":
    server_main(HOST, PORT)