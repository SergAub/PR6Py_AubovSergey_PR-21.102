#-*- coding: utf-8 -*-

import socket
import hashlib
from datetime import datetime
from _thread import *
messages = []
 

def client_thread (con):

    strMessages = ""    

    data = con.recv(1024)
    message = data.decode()
    if message != "KeY$%^Give":
        print(messages)
    else:
        print("Передача чата")
        messages.append(message)
    con.close()
 
server = socket.socket()
hostname = socket.gethostname()
port = 10666
server.bind((hostname, port))
server.listen(5)

print(" _____  _____    _____    _____ \n|  __ \|  __ \  | ____|  / ____|\n| |__) | |__) | | |__   | (___   ___ _ ____   _____ _ __ \n|  ___/|  _  /  |___ \   \___ \ / _ \ '__\ \ / / _ \ '__|\n| |    | | \ \   ___) |  ____) |  __/ |   \ V /  __/ | \n|_|    |_|  \_\ |____/  |_____/ \___|_|    \_/ \___|_|   \n") 
print("Сервер запущен\nИмя хоста: " + hostname + "\nпорт: " + str(port) + "\n\n")

while True:
    client, _ = server.accept()
    start_new_thread(client_thread, (client, ))
    messages.clear(
