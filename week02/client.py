import socket
import sys

HOST = 'localhost'
PORT = 8888

def echo_client():
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    
            
    while True:
        #输入要传输的数据
        data = input("input data:")
        s.sendall(data.encode()) #编码发送
           
    s.close()

if __name__ == '__main__':
    echo_client()
