import socket


class ChatClient:

    def __init__(self, host="127.0.0.1", port=5000):
        self.host = host
        self.port = port
        self.socket = None

    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))

    def send_message(self, message):
        self.socket.sendall(message.encode("utf-8"))

    def receive_message(self):
        data = self.socket.recv(1024)

        if not data:
            return None

        return data.decode("utf-8")

    def join_room(self, room_name):
        self.send_message(f"JOIN_ROOM|{room_name}")

    def close(self):
        if self.socket:
            try:
                self.socket.close()
            except OSError:
                pass

            self.socket = None