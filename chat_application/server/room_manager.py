class RoomManager:

    def __init__(self):
        self.rooms = {}

    def create_room(self, room_name):
        if room_name not in self.rooms:
            self.rooms[room_name] = set()
            return True

        return False

    def join_room(self, room_name, client_socket):
        if room_name not in self.rooms:
            self.create_room(room_name)

        self.rooms[room_name].add(client_socket)

    def leave_room(self, room_name, client_socket):
        if room_name in self.rooms:
            self.rooms[room_name].discard(client_socket)

            if not self.rooms[room_name]:
                del self.rooms[room_name]

    def get_room_clients(self, room_name):
        return self.rooms.get(room_name, set())