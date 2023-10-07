import socket

port = 2500
buffsize = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("", port))

while True:
    data, addr = sock.recvfrom(buffsize)
    print("Reveived message: ", data.decode())
    sock.sendto(data, addr)
    