#-*- coding: utf-8 -*-

import socket
import sys
import threading


def receive_messages(client):
    while True:
        try:            
            message = client.recv(1024).decode("utf-8")
            print(message)
        except:
            print("Невозможно установить соединение с сервером\n")

def send_messages(client):
    client.send(name.encode("utf-8"))    

    while True:
        message = input()
        client.send(message.encode("utf-8"))
        if message == "/exit":
            break
        
    client.close()

def run_client(host, port):
    client = socket.socket()
    try:
        client.connect((host, port))
    except:
        print("Невозможно установить соединение с сервером\n")
        sys.exit()
    
    threading.Thread(target=receive_messages, args=(client,)).start()
    threading.Thread(target=send_messages, args=(client,)).start()

    

hostname = socket.gethostname()     

print(" _____  _____    _____    _____ _           _   \n|  __ \|  __ \  | ____|  / ____| |         | |  \n| |__) | |__) | | |__   | |    | |__   __ _| |_\n|  ___/|  _  /  |___ \  | |    | '_ \ / _` | __|\n| |    | | \ \   ___) | | |____| | | | (_| | |_\n|_|    |_|  \_\ |____/   \_____|_| |_|\__,_|\__|\n\n")

name = "<" + input("Введите имя\n") + ">"

run_client(hostname, 10666)