import pickle
import socket
import struct
import cv2
import threading

sendMsg = None

# 웹캠 캡처 및 영상 전송 스레드
def video_streaming():
    global sendMsg
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        # 프레임 처리 및 클라이언트에 전송
        a = pickle.dumps(frame)
        message = struct.pack("Q", len(a)) + a
        sendMsg = message
        # client_socket.sendall(message)
        cv2.imshow("TRANSMITTING VIDEO", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            client_socket.close()

# 클라이언트로부터 메시지를 받아 전송하는 스레드
def message_handling(client_socket):
    while True:
        message = client_socket.recv(1024).decode()
        if not message:
            break
        # 메시지 처리 및 클라이언트에 다시 전송
        print("Received Message: " + message)
        client_socket.send(message.encode())

# 추가 #
# 영상 전송 스레드
def send_frame():
    if sendMsg:
        while True:
            client_socket.sendall(sendMsg)

# 소켓 설정 및 연결 수락
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', 12345))
server_socket.listen(5)

while True:
    client_socket, addr = server_socket.accept()

    # 클라이언트 연결마다 스레드 생성
    video_thread = threading.Thread(target=video_streaming)
    message_thread = threading.Thread(target=message_handling, args=(client_socket,))
    send_frame_thread = threading.Thread(target=send_frame())

    video_thread.daemon = True
    message_thread.daemon = True
    send_frame_thread.daemon = True

    video_thread.start()
    message_thread.start()
    send_frame_thread.start()
