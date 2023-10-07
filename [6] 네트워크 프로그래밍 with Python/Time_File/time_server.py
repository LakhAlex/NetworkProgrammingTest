# time_server.py #
import socket # socket 모듈을 불러온다.
import time

'''
 timeserver에 client가 접속한 이후 server에서 client의 접속을 끊지 않는다.
 server는 client에 1초당 한번 메시지를 보내고, client는 1초당 한번 메시지를 출력한다.
'''

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('', 5000) # '' = 임의 주소, 포트번호=5000
s.bind(address)
s.listen(5)

client, addr = s.accept()  # 클라이언트와의 연결을 한번 진행한다.

while True:
    print("Connnection requested from ", addr)
    if client:
        time.sleep(1)
        client.send(time.ctime(time.time()).encode())
    # client.close # 클라이언트와의 연결을 종료하지 않으면, 계속 실행된다.

"""
import socket # socket 모듈을 불러온다.
import time

# TCP 소켓 생성
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('', 5000) # '' => 임의 주소, 포트번호=5000
s.bind(address) # 소캣과 주소 결합
s.listen(5) # 클라이언트가 연결하길 기다림, 5개 까지 동시 수용가능


while True:
    client, addr = s.accept() # 연결 허용. (client socket, rem_addr) 반환
    print("Connnection requested from ", addr)
    client.send(time.ctime(time.time()).encode()) # 현재 시간을 전송
    client.close # 소켓 종료

"""