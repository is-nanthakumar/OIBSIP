import tkinter as tk
from tkinter import messagebox

from network import ChatClient


class LoginWindow:

    def __init__(self):
        self.client = ChatClient()

        self.window = tk.Tk()
        self.window.title("Chat Application - Login")
        self.window.geometry("400x350")
        self.window.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):

        title = tk.Label(
            self.window,
            text="Chat Application",
            font=("Arial", 20, "bold")
        )
        title.pack(pady=25)

        username_label = tk.Label(
            self.window,
            text="Username"
        )
        username_label.pack()

        self.username_entry = tk.Entry(
            self.window,
            width=30
        )
        self.username_entry.pack(pady=5)

        password_label = tk.Label(
            self.window,
            text="Password"
        )
        password_label.pack()

        self.password_entry = tk.Entry(
            self.window,
            width=30,
            show="*"
        )
        self.password_entry.pack(pady=5)

        login_button = tk.Button(
            self.window,
            text="Login",
            width=15,
            command=self.login
        )
        login_button.pack(pady=15)

        register_button = tk.Button(
            self.window,
            text="Register",
            width=15,
            command=self.register
        )
        register_button.pack()

    def connect_to_server(self):

        try:
            self.client.connect()
            return True

        except OSError:
            messagebox.showerror(
                "Connection Error",
                "Could not connect to server."
            )
            return False

    def login(self):

        username = self.username_entry.get().strip()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showwarning(
                "Missing Information",
                "Please enter username and password."
            )
            return

        if not self.connect_to_server():
            return

        self.client.send_message(
            f"LOGIN|{username}|{password}"
        )

        response = self.client.receive_message()

        if response == "AUTH|LOGIN_SUCCESS":

            messagebox.showinfo(
                "Success",
                "Login successful!"
            )

            self.window.destroy()

            from chat_window import ChatWindow

            ChatWindow(
                self.client,
                username
            )

        else:

            messagebox.showerror(
                "Login Failed",
                response
            )

            self.client.close()

    def register(self):

        username = self.username_entry.get().strip()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showwarning(
                "Missing Information",
                "Please enter username and password."
            )
            return

        if not self.connect_to_server():
            return

        self.client.send_message(
            f"REGISTER|{username}|{password}"
        )

        response = self.client.receive_message()
        print("SERVER RESPONSE:", response)

        if response == "AUTH|REGISTER_SUCCESS":

            messagebox.showinfo(
                "Success",
                "Registration successful! Please login."
            )

        else:

            messagebox.showerror(
                "Registration Failed",
                response
            )

        self.client.close()

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = LoginWindow()
    app.run()