#-*- coding: utf-8 -*-

import socket
import threading

 
def handle_client(client, address):
    try:
        name = client.recv(1024).decode()
    
        while True:
            message = name + "\t" + client.recv(1024).decode()
            if message == "/exit":
                break
            print(f"Получено сообщение {address[0]}:{address[1]}: {message}")
            
            for c in clients:
                if c != client:
                    c.send(message.encode())
    except:
        print(f"Клиент {address[0]}:{address[1]} разорвал соединение")
    finally:
        client.close()
        clients.remove(client)
    
def run_server(host, port):
    server = socket.socket()
    server.bind((host, port))
    server.listen(5)

    print(f"Сервер запущен\nИмя хоста: {hostname}\nпорт: {port}\n\n")

    while True:
        client, address = server.accept()
        print(f"Подключение {address[0]}:{address[1]}")
        clients.append(client)
        threading.Thread(target=handle_client, args=(client, address)).start()

    server_socket.close()


hostname = socket.gethostname()  

print(" _____  _____    _____    _____ \n|  __ \|  __ \  | ____|  / ____|\n| |__) | |__) | | |__   | (___   ___ _ ____   _____ _ __ \n|  ___/|  _  /  |___ \   \___ \ / _ \ '__\ \ / / _ \ '__|\n| |    | | \ \   ___) |  ____) |  __/ |   \ V /  __/ | \n|_|    |_|  \_\ |____/  |_____/ \___|_|    \_/ \___|_|   \n") 

clients = []
run_server(hostname, 10666)