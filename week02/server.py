import socket
import os

HOST = 'localhost'
PORT = 8888


def echo_server():
    # 创建socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    sock.bind((HOST, PORT))# 绑定地址和端口号
    sock.listen(1)  # 监听连接数
    
        
    while True:
        # 等待请求并接受
        conn, addr = sock.accept()
        # 输出客户端地址
        print(f'Connected by {addr}')
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(data)
            conn.sendall(data)
        conn.close()
    s.close()


if __name__ == '__main__':
    echo_server()
       