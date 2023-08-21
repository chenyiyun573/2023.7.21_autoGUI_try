# client.py

import socket
import pyautogui
import io
from PIL import Image

class Client:
    def __init__(self, host, port):
        self.server_host = host
        self.server_port = port

    def send_screenshot(self, conn):
        screenshot = pyautogui.screenshot()
        screenshot_bytes = io.BytesIO()
        screenshot.save(screenshot_bytes, format="PNG")
        screenshot_data = screenshot_bytes.getvalue()

        conn.sendall(len(screenshot_data).to_bytes(4, byteorder='big'))
        conn.sendall(screenshot_data)

    def receive_command(self, conn):
        command = conn.recv(1024).decode('utf-8')
        return command

    def execute_command(self, command):
        action, *args = command.split()

        if action == "move":
            x, y = map(int, args)
            pyautogui.moveTo(x, y)
        elif action == "click":
            pyautogui.click()
        elif action == "write":
            pyautogui.write(" ".join(args))
        elif action == "press":
            pyautogui.press(args[0])

    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.server_host, self.server_port))

            while True:
                self.send_screenshot(s)
                command = self.receive_command(s)
                self.execute_command(command)


if __name__ == "__main__":
    client = Client('127.0.0.1', 65432)
    client.run()
