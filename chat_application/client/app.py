import threading
from network import ChatClient


client = ChatClient()


def receive_messages():
    while True:
        try:
            message = client.receive_message()

            if message is None:
                break

            print(f"\n{message}")
            print("You: ", end="", flush=True)

        except OSError:
            break


def send_request(request):
    client.send_message(request)

    response = client.receive_message()

    return response


try:
    client.connect()

    print("\n=== Chat Application ===")
    print("1. Register")
    print("2. Login")

    choice = input("Choose: ")

    username = input("Username: ")
    password = input("Password: ")

    if choice == "1":

        response = send_request(
            f"REGISTER|{username}|{password}"
        )

        print(f"Server: {response}")

        if response != "REGISTER_SUCCESS":
            client.close()
            exit()

        print("Registration successful. Please login.")

        response = send_request(
            f"LOGIN|{username}|{password}"
        )

        print(f"Server: {response}")

        if response != "LOGIN_SUCCESS":
            client.close()
            exit()

    elif choice == "2":

        response = send_request(
            f"LOGIN|{username}|{password}"
        )

        print(f"Server: {response}")

        if response != "LOGIN_SUCCESS":
            client.close()
            exit()

    else:
        print("Invalid choice.")
        client.close()
        exit()

    print("\nLogin successful!")
    print("You can start chatting.")
    print("Type /quit to exit.\n")

    receiver_thread = threading.Thread(
        target=receive_messages,
        daemon=True
    )

    receiver_thread.start()

    while True:
        message = input("You: ")

        if message.strip().lower() == "/quit":
            break

        if message.strip():
            client.send_message(
                f"CHAT|{message}"
            )

finally:
    client.close()
    print("Client stopped.")