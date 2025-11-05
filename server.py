import socket

HOST = '127.0.0.1'
PORT = 9999

# socket create
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
print(f"[*] Server started on {HOST}:{PORT}")
conn, addr = s.accept()
print(f"[+] Connected by {addr}")

while True:
    # receive from client
    data = conn.recv(1024).decode()
    if not data:
        break
    print(f"Client: {data}")

    # send reply to client
    msg = input("Server: ")
    conn.send(msg.encode())

conn.close()
