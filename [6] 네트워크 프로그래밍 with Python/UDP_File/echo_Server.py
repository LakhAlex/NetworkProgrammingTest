# UDP 실습1 #

import socket
port = 2500
buffsize = 1024
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("", port))

while True:
    data, addr = sock.recvfrom(buffsize)
    print("Received message: ", data.decode())
    resp = input(":")
    sock.sendto(resp.encode(), addr)