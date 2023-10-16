import time
import tkinter as tk
from tkinter import *
import cv2
import socket
import struct
import pickle
import threading
from PIL import Image, ImageTk

# 전역변수
photo = None

def readCAM():
    global photo
    data = b""
    while True:
        payload_size = struct.calcsize("Q")
        try:
            while len(data) < payload_size:
                packet = sock.recv(4*1024)
                if not packet:
                    break
                data += packet
            packet_msg_size = data[:payload_size]
            data = data[payload_size:]
            msg_size = struct.unpack("Q", packet_msg_size)[0]
            while len(data) < msg_size:
                data += sock.recv(4*1024)
            frame_data = data[:msg_size]
            data = data[msg_size:]
            frame = pickle.loads(frame_data)

            # # OpenCV frame을 PIL 이미지로 변환
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(frame)
            photo = ImageTk.PhotoImage(image=image)

            vidLable.config(image=photo)
            vidLable.image = photo

        except Exception as e:
            print(e)
            break
        window.after(0.02, readCAM)

def updateGUI():
    window.update()
    time.sleep(0.03)


def send_message():
    message = chat_text.get()
    chatWin.config(state=NORMAL)
    chatWin.insert(END, "나: " + message + "\n")
    sock.send(message.encode())
    chatWin.config(state=DISABLED)
    chat_text.delete(0, END)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 12345))

window = tk.Tk()
window.title("Client")
window.geometry("1200x400")

vidLable = Label(window)
vidLable.grid(row=0, column=0, padx=5, pady=5, rowspan=2, sticky="nsew")
# vidLable.config(image=)

chatWin = Text(window)
chatWin.config(state = DISABLED) # 채팅창을 오직 읽기 전용으로만 하도록 설정!
chatWin.grid(row = 0, column = 1, padx = 20, pady = 20, sticky="nsew")

chat_text = Entry(window)
chat_text.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

sendBtn = Button(window, text="보내기", command=send_message)
sendBtn.grid(row=1, column=1, padx=10, pady=10, sticky="se")

window.grid_rowconfigure(0, weight=5)
window.grid_columnconfigure(0, weight=5) # 비디오 화면
window.grid_columnconfigure(1, weight=1) # 채팅창


read_cam_thread = threading.Thread(target=readCAM)
update_gui_thread = threading.Thread(target=updateGUI)

read_cam_thread.daemon = True
update_gui_thread.daemon = True

update_gui_thread.start()
read_cam_thread.start()

window.mainloop()

# while True:
#     read_cam = threading.Thread(target=readCAM)
#     gui = threading.Thread(target=updateGUI())
#
#     read_cam.daemon = True
#     gui.daemon = True
#
#     gui.start()
#     read_cam.start()

