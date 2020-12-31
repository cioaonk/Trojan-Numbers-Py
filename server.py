import socket

HOST = '192.168.0.15'
PORT = 8999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()

client, address = server.accept()

while True:

    print(f"Connected to {address}")
    cmd_input = input("Enter a Command:")
    client.send(cmd_input.encode('utf-8'))
    print(client.recv(1024).decode('utf-8'))