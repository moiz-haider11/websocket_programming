import socket

HOST = '127.0.0.1'
PORT = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print("[+] Connected to server")

while True:
    # send message
    msg = input("You: ")
    s.send(msg.encode())

    # receive reply
    data = s.recv(1024).decode()
    print(f"Server: {data}")

s.close()
