import socket
# import server
import threading


SERVER_HOST = "127.0.0.1"  # The server's hostname or IP address
SERVER_PORT = 65432  # The port used by the server


# define sender() and receiver() to be used locally in client_main() where we can pass s obj
def sender(s):
    while True:
        message = input("Enter message: ")
        s.sendall(message.encode("utf-32"))
        if message.lower() == "bye":
            break
def receiver(s):
    while True:
        data = s.recv(1024)
        if not data:
            break
        print(f"Recieved: {data.decode("utf-32")}")

def client_main(SERVER_HOST, SERVER_PORT):
    # creating client socket as s to connect to server, using TCP/IP -- IP = (AF_INET) via TCP = (SOCK_STREAM))
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((SERVER_HOST, SERVER_PORT))
        # data = s.recv(1024)

#maintaining server connection while messages are sent "bye" to exit the loop
 # create 2 thread instances to run the sender + receiver functions concurrently
        sender_thread = threading.Thread(target=sender, args=(s,))
        receiver_thread = threading.Thread(target=receiver, args=(s,))

        # .start calls the functions on respective threads
        sender_thread.start()
        receiver_thread.start()

        # .join breaks and rejoins the threads, code now runs sequentially
        sender_thread.join()
        receiver_thread.join()



if __name__ == "__main__":
    client_main(SERVER_HOST, SERVER_PORT)

