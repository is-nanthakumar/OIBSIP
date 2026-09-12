import tkinter as tk
from tkinter import messagebox
import threading


class ChatWindow:

    def __init__(self, client, username):
        self.client = client
        self.username = username

        self.window = tk.Tk()
        self.window.title(f"Chat Application - {username}")
        self.window.geometry("600x500")

        self.create_widgets()

        self.receiver_thread = threading.Thread(
            target=self.receive_messages,
            daemon=True
        )
        self.receiver_thread.start()

        self.window.protocol(
            "WM_DELETE_WINDOW",
            self.close
        )

        self.window.mainloop()

    def create_widgets(self):

        # ---------- TITLE ----------
        title = tk.Label(
            self.window,
            text=f"Welcome, {self.username}",
            font=("Arial", 16, "bold")
        )
        title.pack(pady=10)

        # ---------- ROOM ----------
        room_frame = tk.Frame(self.window)
        room_frame.pack(pady=5)

        room_label = tk.Label(
            room_frame,
            text="Room:"
        )
        room_label.pack(side="left")

        self.room_entry = tk.Entry(
            room_frame,
            width=20
        )
        self.room_entry.pack(
            side="left",
            padx=5
        )

        join_button = tk.Button(
            room_frame,
            text="Join Room",
            command=self.join_room
        )
        join_button.pack(side="left")

        # ---------- CHAT AREA ----------
        self.chat_area = tk.Text(
            self.window,
            height=20,
            width=70,
            state="disabled"
        )
        self.chat_area.pack(
            padx=10,
            pady=10
        )

        # ---------- MESSAGE AREA ----------
        bottom_frame = tk.Frame(self.window)
        bottom_frame.pack(
            fill="x",
            padx=10,
            pady=10
        )

        self.message_entry = tk.Entry(
            bottom_frame
        )
        self.message_entry.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(0, 10)
        )
        
        emoji_button = tk.Button(
            bottom_frame,
            text="😊",
            command=self.insert_emoji
        )
        emoji_button.pack(side="right", padx=5)

        send_button = tk.Button(
            bottom_frame,
            text="Send",
            command=self.send_message
        )
        send_button.pack(side="right")

        self.message_entry.bind(
            "<Return>",
            lambda event: self.send_message()
        )

    # ---------- JOIN ROOM ----------
    
    def join_room(self):

        room_name = self.room_entry.get().strip()

        if not room_name:
            messagebox.showwarning(
                "Room",
                "Please enter a room name."
            )
            return

        try:

            self.client.join_room(room_name)

            self.display_message(
                f"[SYSTEM] Joining room: {room_name}"
            )

            self.room_entry.delete(
                0,
                tk.END
            )

        except OSError:

            messagebox.showerror(
                "Connection Error",
                "Connection to server lost."
            )

            self.close()


    # ---------- SEND MESSAGE ----------
    def send_message(self):

        message = self.message_entry.get().strip()

        if not message:
            return

        if message.lower() == "/quit":
            self.close()
            return

        try:

            self.client.send_message(
                f"CHAT|{message}"
            )

            self.display_message(
                f"You: {message}"
            )

            self.message_entry.delete(
                0,
                tk.END
            )

        except OSError:

            messagebox.showerror(
                "Connection Error",
                "Connection to server lost."
            )

            self.close()

    
    def insert_emoji(self):

        emoji_window = tk.Toplevel(self.window)

        emoji_window.title("Choose Emoji")
        emoji_window.geometry("300x120")

        emojis = [
            "😊",
            "😂",
            "❤️",
            "👍",
            "🔥",
            "🎉",
            "😎",
            "😢",
            "😡",
            "🙏"
        ]

        for index, emoji in enumerate(emojis):
            
            button = tk.Button(
                emoji_window,
                text=emoji,
                font=("Arial", 16),
                command=lambda e=emoji: self.add_emoji(
                    e,
                    emoji_window
                )
            )

            button.grid(
                row=index // 5,
                column=index % 5,
                padx=5,
                pady=5
            )
    
    
    def add_emoji(self, emoji, emoji_window):

        self.message_entry.insert(
            tk.END,
            emoji
        )

        self.message_entry.focus()
        emoji_window.destroy()        

    # ---------- RECEIVE MESSAGE ----------
    def receive_messages(self):
        
        while True:
            
            try:
                
                message = self.client.receive_message()

                if message is None:
                    break

                if message.startswith("ROOM|JOINED|"):
                    
                    parts = message.split("|", 3)

                    room_name = parts[2]

                    history = ""

                    if len(parts) == 4:
                        
                        history = parts[3]

                    self.window.after(
                        0,
                        self.display_room_history,
                        room_name,
                        history
                    )

                elif message.startswith("CHAT|ERROR|"):
                    error_message = message.split("|", 2)[2]

                    self.window.after(
                        0,
                        self.display_message,
                        f"[ERROR] {error_message}"
                    )


                elif message.startswith("ROOM|ERROR|"):
                    error_message = message.split("|", 2)[2]

                    self.window.after(
                        0,
                        self.display_message,
                        f"[ERROR] {error_message}"
                    )


                elif message.startswith("SYSTEM|"):
                    
                    system_message = message.split(
                        "|",
                         1
                    )[1]


                    room_name = message.split("|", 1)[1].strip()

                    self.window.after(
                        0,
                        self.display_message,
                        f"[SYSTEM] {system_message}"
                    )

                else:
                    
                    self.window.after(
                        0,
                        self.display_message,
                        message
                    )

            except OSError:
                break

    # ---------- DISPLAY MESSAGE ----------
    def display_message(self, message):

        self.chat_area.config(
            state="normal"
        )

        self.chat_area.insert(
            tk.END,
            message + "\n"
        )

        self.chat_area.config(
            state="disabled"
        )

        self.chat_area.see(
            tk.END
        )




    def display_room_history(self, room_name, history):
        
        self.display_message(
            f"[SYSTEM] Joined room: {room_name}"
        )

        if history.strip():
            
            self.display_message(
                "[MESSAGE HISTORY]"
            )

            for line in history.strip().splitlines():
                
                self.display_message(line)

        else:
            
            self.display_message(
                "[No previous messages]"
            )


    # ---------- CLOSE ----------
    def close(self):

        try:
            self.client.close()

        except OSError:
            pass

        self.window.destroy()