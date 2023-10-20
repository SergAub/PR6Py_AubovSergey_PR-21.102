#-*- coding: utf-8 -*-

import socket
import hashlib
from datetime import datetime
from _thread import *
import sys

def con():
    client = socket.socket()    

    try:
        client.connect((hostname, port))
    except ConnectionError:
        print("Невозможно установить соединение с сервером\n")
        sys.exit()


def account(reg):

    login = input("Введите логин:\n")

    password = input("Введите пароль:\n")
    h = hashlib.new('sha256')
    h.update(password)
    password = h.hexdigest()

    con();
    client.send(reg.encode())
    client.send(login.encode())
    client.send(password.encode())

    ans = client.recv(1024)

def input_tread():
    while True:
        clientInput = socket.socket()
        try:
            clientInput.connect((hostname, port))
        except ConnectionError:
            print("Невозможно установить соединение с сервером\n")
            sys.exit()
        
        key = "KeY$%^Give"
        clientInput.send(key.encode())
        clientImput.close()

def output():
    client = socket.socket()    

    try:
        client.connect((hostname, port))
    except ConnectionError:
        print("Невозможно установить соединение с сервером\n")
        sys.exit()
        
    client.send(message.encode())
    data = client.recv(1024)
    print(data.decode())
    client.close()
    message = "<" + name + "> " + input("<Вы>")
    

hostname = socket.gethostname()     
port = 10666

print(" _____  _____    _____    _____ _           _   \n|  __ \|  __ \  | ____|  / ____| |         | |  \n| |__) | |__) | | |__   | |    | |__   __ _| |_\n|  ___/|  _  /  |___ \  | |    | '_ \ / _` | __|\n| |    | | \ \   ___) | | |____| | | | (_| | |_\n|_|    |_|  \_\ |____/   \_____|_| |_|\__,_|\__|\n\n")

name = input("Введите имя\n")
