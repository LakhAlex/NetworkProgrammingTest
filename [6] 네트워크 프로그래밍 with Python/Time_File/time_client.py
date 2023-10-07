#time_client.py

import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ("localhost", 5000)
sock.connect(address) # 서버에 연결
while True:
    time.sleep(1)
    print("현재시각: ", sock.recv(1024).decode()) # 수신 내용을 문자열로 변환하여 출력

'''
server측에서 data 전송을 1초다가 진행하므로, client도 1초 마다 받아야
오류가 발생하지 않는다.

1초 동안의 대기를 만드는 것은 time.sleep()라는 메소드를 사용한다.
'''