import socket

buffsize = 1024
port = 2500

# 서버와 통신 유형의 소켓 생성
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

msg = input() # 서버에 전송할 msg를 입력 받음
sock.sendto(msg.encode(), ('localhost', port)) # 메시지 송신
data, addr = sock.recvfrom(buffsize) # 메시지 수신
print("Server says: ", data.decode())