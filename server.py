import socket
import threading

from tkinter import *

# gui code shtolen  from https://www.geeksforgeeks.org/gui-chat-application-using-tkinter-in-python/

# GUI
root = Tk()
root.title("server")

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"


lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, pady=10, width=20, height=1).grid(
	row=0)

txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row=1, column=0, columnspan=2)

scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)

e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
e.grid(row=2, column=0)



# sock = socket.sock_STREAM

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

# define sender() + reciever() to be called locally in server_main where we can pass conn obj
# def sender(conn):
#     while True:
#         message = input("Enter message: ")
#         conn.sendall(message.encode("utf-32"))
#
#         if message.lower() == "bye":
#             break
#         return conn.sendall(message.encode("utf-32"))





def receiver(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        txt.insert(END, "\n" + f"Received: {data.decode("utf-32")}")


def server_main(HOST, PORT):
    # creating server socket as s via TCP/IP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # binds the socket to the specified port and IP
        s.bind((HOST, PORT))

        # instructing the server to listen for connection requests (breaks if no connection)
        s.listen()



        #assigns the server socket to conn and client IP + Port to addr. s.accept() completes the handshake
        conn, addr = s.accept()



        with conn:
            print(f"Connected by {addr}")
            print(f"let's see what conn is:  {conn}")

            def sender():
                if conn:
                    message = "Sent: " + e.get()
                    txt.insert(END, "\n" + message)
                    conn.sendall(e.get().encode("utf-32"))
                    e.delete(0, END)


            # create 2 thread instances to run the sender + receiver functions concurrently
            Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,
                          command=sender).grid(row=2, column=1)
            # sender_thread = threading.Thread(target=sender, args=(conn,))
            receiver_thread = threading.Thread(target=receiver, args=(conn,))

            # .start calls the functions on respective threads
            # sender_thread.start()
            receiver_thread.start()

            # receiver_thread.join()

            # opens chat window, closing window ends program
            root.mainloop()





if __name__ == "__main__":
    server_main(HOST, PORT)