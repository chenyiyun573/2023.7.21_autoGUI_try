# server.py

import socket
from PIL import Image, ImageShow
import io

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def receive_screenshot(self, conn):
        data_length = int.from_bytes(conn.recv(4), byteorder='big')
        data = b''
        while len(data) < data_length:
            packet = conn.recv(data_length - len(data))
            if not packet:
                break
            data += packet

        # Convert bytes to Image and show
        image = Image.open(io.BytesIO(data))
        image.show()

    def send_command(self, conn):
        command = input("Enter command (e.g., 'move 100 100', 'click', 'write Hello', 'press esc'): ")
        conn.sendall(command.encode('utf-8'))

    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    self.receive_screenshot(conn)
                    self.send_command(conn)


if __name__ == "__main__":
    server = Server('0.0.0.0', 65432)
    server.run()
