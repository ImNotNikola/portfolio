import tkinter
from socket import socket
import socket
from tkinter import *
from threading import Thread

def recieve():
    while True:
        try:
            msg = s.recv(1024).decode("utf8")
            msg_listBox.insert(tkinter.END, msg)
        except:
            print("Error recieveing the message.")

def send():
    msg = message.get()
    message.set("")
    s.send(bytes(msg, "utf8"))
    if msg == '#quit':
        s.close()
        window.close()

window = Tk()
window.title("Chat")
window.configure(bg="black")
message_frame = Frame(window, height = 100, width = 100, bg = "black")
message_frame.pack()

message = StringVar()
message.set("")

scroll_bar = Scrollbar(message_frame)
msg_listBox = Listbox(message_frame, height = 15, width = 100, yscrollcommand=scroll_bar.set)
scroll_bar.pack(side = RIGHT, fill = Y)
msg_listBox.pack(side = LEFT, fill = BOTH)
msg_listBox.pack()

entry_field = Entry(window, textvariable = message, width = 50)
entry_field.pack()

send_button = Button(window, text = "Send", font = 'Aerial', command = send)
send_button.pack()

host = 'localhost'
port = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host,port))

recieve_thread = Thread(target=recieve)
recieve_thread.start()

mainloop()
