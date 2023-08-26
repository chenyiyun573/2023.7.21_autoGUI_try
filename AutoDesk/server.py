# server.py

import socket
from PIL import Image, ImageShow
import io

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def receive_screenshot1(self, conn):
        data_len = int.from_bytes(conn.recv(4), byteorder='big')  # Read the length of the image data
        data = conn.recv(data_len)  # Receive the image data based on the length
        image = Image.open(io.BytesIO(data))
        image.show()

    def receive_screenshot(self, conn):
        data_length = int.from_bytes(conn.recv(4), byteorder='big')
        data = b''
        print('data_length '+str(data_length))
        while len(data) < data_length:
            packet = conn.recv(data_length - len(data))
            if not packet:
                break
            data += packet

        # Convert bytes to Image and show
        image = Image.open(io.BytesIO(data))
        image.show()

    def send_command(self, conn):
        try:
            command = input("Enter command (e.g., 'move 100 100', 'click', 'write Hello', 'press esc'): ")
            conn.sendall(command.encode('utf-8'))
        except Exception as e:
            # Handle exceptions here
            print(f"Error: {e}")


    def send_command1(self, conn):
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
                    print('one photo received')
                    self.send_command(conn)
                    print('one command sent')


if __name__ == "__main__":
    server = Server('0.0.0.0', 65432)
    server.run()
