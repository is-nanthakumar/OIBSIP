import socket
import threading

from database.database import (
    initialize_database,
    create_user,
    authenticate_user,
    save_message,
    get_room_messages
)

from server.room_manager import RoomManager

from utils.validators import (
    validate_username,
    validate_password,
    validate_room_name,
    validate_message
)


HOST = "127.0.0.1"
PORT = 5000

clients = []
clients_lock = threading.Lock()

room_manager = RoomManager()


def broadcast_to_room(message, room_name, sender_socket):
    room_clients = room_manager.get_room_clients(room_name)

    for client in room_clients:
        if client != sender_socket:
            try:
                client.sendall(message.encode("utf-8"))
            except OSError:
                pass


def handle_client(client_socket, client_address):
    print(f"[CONNECTED] {client_address}")

    authenticated = False
    username = None
    room_name = None

    with clients_lock:
        clients.append(client_socket)

    try:
        while True:
            data = client_socket.recv(1024)

            if not data:
                break

            message = data.decode("utf-8")

            if message.startswith("REGISTER|"):
                parts = message.split("|", 2)

                if len(parts) != 3:
                    client_socket.sendall(
                        b"REGISTER_FAILED|Invalid data"
                    )
                    continue

                username = parts[1]
                password = parts[2]


                username_valid, username_error = validate_username(username)

                if not username_valid:
                    client_socket.sendall(
                        f"AUTH|REGISTER_FAILED|{username_error}".encode("utf-8")
                    )
                    continue


                password_valid, password_error = validate_password(password)

                if not password_valid:
                    client_socket.sendall(
                        f"AUTH|REGISTER_FAILED|{password_error}".encode("utf-8")
                    )
                    continue

                success = create_user(username, password)

                if success:
                    client_socket.sendall(
                        b"AUTH|REGISTER_SUCCESS"
                    )
                else:
                    client_socket.sendall(
                        b"AUTH|REGISTER_FAILED|Username already exists"
                    )

            elif message.startswith("LOGIN|"):
                parts = message.split("|", 2)

                if len(parts) != 3:
                    client_socket.sendall(
                        b"AUTH|LOGIN_FAILED"
                    )
                    continue

                username = parts[1]
                password = parts[2]

                success = authenticate_user(username, password)

                if success:
                    authenticated = True
                    client_socket.sendall(b"AUTH|LOGIN_SUCCESS")
                    print(f"[LOGIN] {username} from {client_address}")

                else:
                    client_socket.sendall(
                        b"AUTH|LOGIN_FAILED|Invalid username or password"
                    )
            

            elif message.startswith("JOIN_ROOM|"):
                
                if not authenticated:                  
                    client_socket.sendall(
                        b"ERROR|Please login first"
                    )
                    continue

                room_name = message.split(
                    "|",
                    1
                )[1].strip()

                room_valid, room_error = validate_room_name(room_name)
                
                if not room_valid:
                    client_socket.sendall(
                        f"ROOM|ERROR|{room_error}".encode("utf-8")
                    )
                    continue

                room_manager.join_room(
                    room_name,
                    client_socket
                )

                broadcast_to_room(
                    f"SYSTEM|{username} joined {room_name}",
                    room_name,
                    client_socket
                )

                history = get_room_messages(room_name)

                history_text = ""

                for username_history, message_history, sent_at in history:
                    history_text += (
                        f"{username_history}: "
                        f"{message_history} "
                        f"({sent_at})\n"
                    )

                response = (
                    f"ROOM|JOINED|{room_name}|{history_text}"
                )

                client_socket.sendall(
                    response.encode("utf-8")
                )

                print(
                    f"[ROOM] {username} joined {room_name}"
                )
            
            elif message.startswith("CHAT|"):
                if not authenticated:
                    client_socket.sendall(b"ERROR|Please login first")
                    continue

                if room_name is None:
                    client_socket.sendall(b"ERROR|Please join a room first")
                    continue

                chat_message = message.split("|", 1)[1]

                message_valid, message_error = validate_message(chat_message)

                if not message_valid:
                    client_socket.sendall(
                        f"CHAT|ERROR|{message_error}".encode("utf-8")
                    )
                    continue

                save_message(
                    username,
                    room_name,
                    chat_message
                )

                print(f"[{room_name}] [{username}] {chat_message}")

                broadcast_to_room(
                    f"CHAT|{username}|{chat_message}",
                    room_name,
                    client_socket
                )

            else:
                client_socket.sendall(
                    b"ERROR|Unknown request"
                )

    except ConnectionResetError:
        print(f"[RESET] {client_address}")

    finally:
        
        if room_name is not None:
            
            broadcast_to_room(
                f"SYSTEM|{username} left {room_name}",
                room_name,
                client_socket
            )

            room_manager.leave_room(
                room_name,
                client_socket
            )

        with clients_lock:
            
            if client_socket in clients:
                clients.remove(client_socket)

        client_socket.close()

        print(
            f"[DISCONNECTED] {client_address}"
        )


server_socket = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

server_socket.setsockopt(
    socket.SOL_SOCKET,
    socket.SO_REUSEADDR,
    1
)

server_socket.bind((HOST, PORT))
server_socket.listen()

initialize_database()

print(f"Server started on {HOST}:{PORT}")
print("Waiting for clients...")


try:
    while True:
        client_socket, client_address = server_socket.accept()

        client_thread = threading.Thread(
            target=handle_client,
            args=(client_socket, client_address),
            daemon=True
        )

        client_thread.start()

except KeyboardInterrupt:
    print("\nServer shutting down...")

finally:
    with clients_lock:
        for client in clients:
            try:
                client.close()
            except OSError:
                pass

        clients.clear()

    server_socket.close()
    print("Server stopped.")