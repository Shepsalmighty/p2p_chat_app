import socket
import threading
from tkinter import *

# hardcoding server TCP/IP
SERVER_HOST = "127.0.0.1"  # The server's hostname or IP address
SERVER_PORT = 65432  # The port used by the server

# gui code shtolen  from https://www.geeksforgeeks.org/gui-chat-application-using-tkinter-in-python/

# GUI
root = Tk()
root.title("client")

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


# define receiver() to be used locally in client_main() where we can pass s obj
def receiver(s):
    while True:
        data = s.recv(1024)
        if not data:
            break
        txt.insert(END, "\n" + f"Received: {data.decode("utf-32")}")


def client_main(SERVER_HOST, SERVER_PORT):
    # creating client socket as s to connect to server, using TCP/IP -- IP = (AF_INET) via TCP = (SOCK_STREAM))
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((SERVER_HOST, SERVER_PORT))

        def sender():
            if s:
                message = "Sent: " + e.get()
                txt.insert(END, "\n" + message)
                s.sendall(e.get().encode("utf-32"))
                e.delete(0, END)

        Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,
               command=sender).grid(row=2, column=1)

        # create thread instance for reciever to run functions concurrently (sender thread handled in sender())
        receiver_thread = threading.Thread(target=receiver, args=(s,))

        # .start calls the function on it's own thread
        receiver_thread.start()

        # opens chat window and blocks until the window is closed
        root.mainloop()


if __name__ == "__main__":
    client_main(SERVER_HOST, SERVER_PORT)
