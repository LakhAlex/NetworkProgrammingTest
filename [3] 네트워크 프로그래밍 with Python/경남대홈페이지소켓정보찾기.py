import socket

def get_constants(prefix):
    """소켓의 {속성값: 속성} 딕셔너리"""
    return{
        # socket 속성  #prefix로 시작하는 속성 조사
        getattr(socket, n): n for n in dir(socket) if n.startswith(prefix)
    }

#'AF_', 'SOCK_', IPPROTO_'로 시작하는 속성 이름을 상수와 맵핑시키는 딕셔너리를 만든다.
failies = get_constants('AF_')
types = get_constants('SOCK_')
protocols = get_constants('IPPROTO_')

for response in socket.getaddrinfo('www.kyungnam.ac.kr', 'http'):
    # Unpack the response tuple
    faily, socktype, proto, canonname, sockaddr = response

    print('Family:         ', failies[faily])
    print('Type:           ', types[socktype])
    print('Protocol:       ', protocols[proto])
    print('Canonical name: ', canonname)
    print('Socket address: ', sockaddr)
    print()

"""
[결과]
Family:          AF_INET
Type:            SOCK_STREAM
Protocol:        IPPROTO_IP
Canonical name:  
Socket address:  ('223.194.236.178', 80)
-----------------------------------------
AF_INET : 가장 보편적인 주소유형, 4바이트 길이(192.168.0.1) / IP주소
SOCK_STREAM : 신뢰성 있느 전송을 보장하는 TCP 프로토콜 사용(HTTP)
IPPROTO_IP : IP Protocol의 옵션



SOL_SOCKET : 소켓에 대한 가장 일반적인 옵션
IPPROTO_TCP : TCP Protocol의 옵션
"""