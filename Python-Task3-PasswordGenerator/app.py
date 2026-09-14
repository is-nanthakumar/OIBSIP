import tkinter as tk
from tkinter import ttk, messagebox

from password_generator import generate_password
from strength_checker import calculate_strength
from clipboard_manager import copy_to_clipboard


class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root

        self.root.title("Advanced Password Generator")
        self.root.geometry("650x700")
        self.root.resizable(False, False)

        self.password_history = []

        self.create_widgets()

    def create_widgets(self):
        # Main title
        title_label = ttk.Label(
            self.root,
            text="Advanced Password Generator",
            font=("Segoe UI", 20, "bold")
        )
        title_label.pack(pady=(20, 5))

        subtitle_label = ttk.Label(
            self.root,
            text="Generate secure passwords using Python secrets",
            font=("Segoe UI", 10)
        )
        subtitle_label.pack(pady=(0, 20))

        # Password length
        length_frame = ttk.LabelFrame(
            self.root,
            text="Password Length",
            padding=15
        )
        length_frame.pack(
            fill="x",
            padx=30,
            pady=10
        )

        self.length_var = tk.IntVar(value=16)

        self.length_value_label = ttk.Label(
            length_frame,
            text="16"
        )
        self.length_value_label.pack()

        self.length_scale = ttk.Scale(
            length_frame,
            from_=8,
            to=64,
            orient="horizontal",
            command=self.update_length
        )
        self.length_scale.set(16)
        self.length_scale.pack(
            fill="x",
            pady=10
        )

        # Character types
        character_frame = ttk.LabelFrame(
            self.root,
            text="Character Types",
            padding=15
        )
        character_frame.pack(
            fill="x",
            padx=30,
            pady=10
        )

        self.uppercase_var = tk.BooleanVar(value=True)
        self.lowercase_var = tk.BooleanVar(value=True)
        self.numbers_var = tk.BooleanVar(value=True)
        self.symbols_var = tk.BooleanVar(value=True)
        self.ambiguous_var = tk.BooleanVar(value=True)

        ttk.Checkbutton(
            character_frame,
            text="Uppercase (A-Z)",
            variable=self.uppercase_var
        ).grid(row=0, column=0, sticky="w", padx=10, pady=5)

        ttk.Checkbutton(
            character_frame,
            text="Lowercase (a-z)",
            variable=self.lowercase_var
        ).grid(row=0, column=1, sticky="w", padx=10, pady=5)

        ttk.Checkbutton(
            character_frame,
            text="Numbers (0-9)",
            variable=self.numbers_var
        ).grid(row=1, column=0, sticky="w", padx=10, pady=5)

        ttk.Checkbutton(
            character_frame,
            text="Symbols",
            variable=self.symbols_var
        ).grid(row=1, column=1, sticky="w", padx=10, pady=5)

        ttk.Checkbutton(
            character_frame,
            text="Exclude ambiguous characters (0, O, l, 1, I)",
            variable=self.ambiguous_var
        ).grid(
            row=2,
            column=0,
            columnspan=2,
            sticky="w",
            padx=10,
            pady=5
        )

        # Generate button
        generate_button = ttk.Button(
            self.root,
            text="Generate Password",
            command=self.generate_password
        )
        generate_button.pack(
            pady=15,
            ipadx=20,
            ipady=5
        )
        
        
        # Bottom section        
        bottom_frame = ttk.Frame(self.root)
        bottom_frame.pack(
            fill="x",
            padx=30,
            pady=10
        )

        # Password output
        output_frame = ttk.LabelFrame(
            bottom_frame,
            text="Generated Password",
            padding=15
        )

        output_frame.grid(
            row=0,
            column=0,
            padx=(0, 10),
            sticky="nsew"
        )

        self.password_var = tk.StringVar()

        self.password_entry = ttk.Entry(
            output_frame,
            textvariable=self.password_var,
            font=("Consolas", 12),
            justify="center",
            width=28
        )

        self.password_entry.pack(
            fill="x",
            pady=5
        )

        # Strength
        self.strength_label = ttk.Label(
            output_frame,
            text="Strength: -",
            font=("Segoe UI", 11, "bold")
        )

        self.strength_label.pack(pady=5)

        # Copy button
        copy_button = ttk.Button(
            output_frame,
            text="Copy to Clipboard",
            command=self.copy_password
        )

        copy_button.pack(pady=5)


        # History
        history_frame = ttk.LabelFrame(
            bottom_frame,
            text="Recent Passwords (Session Only)",
            padding=10
        )

        history_frame.grid(
            row=0,
            column=1,
            padx=(10, 0),
            sticky="nsew"
        )

        self.history_listbox = tk.Listbox(
            history_frame,
            height=7,
            width=30,
            font=("Consolas", 10)
        )

        self.history_listbox.pack(
            fill="both",
            expand=True
        )

        bottom_frame.columnconfigure(0, weight=1)
        bottom_frame.columnconfigure(1, weight=1)

    def update_length(self, value):
        length = int(float(value))
        self.length_var.set(length)
        self.length_value_label.config(text=str(length))

    def generate_password(self):
        try:
            password = generate_password(
                length=self.length_var.get(),
                use_uppercase=self.uppercase_var.get(),
                use_lowercase=self.lowercase_var.get(),
                use_numbers=self.numbers_var.get(),
                use_symbols=self.symbols_var.get(),
                exclude_ambiguous=self.ambiguous_var.get()
            )

            self.password_var.set(password)

            strength = calculate_strength(password)
            self.strength_label.config(
                text=f"Strength: {strength}"
            )

            self.add_to_history(password)

        except ValueError as error:
            messagebox.showerror(
                "Invalid Selection",
                str(error)
            )

    def copy_password(self):
        password = self.password_var.get()

        if not password:
            messagebox.showwarning(
                "No Password",
                "Generate a password first."
            )
            return

        try:
            copy_to_clipboard(password)

            messagebox.showinfo(
                "Copied",
                "Password copied to clipboard."
            )

        except Exception as error:
            messagebox.showerror(
                "Clipboard Error",
                f"Could not copy password.\n\n{error}"
            )

    def add_to_history(self, password):
        self.password_history.insert(0, password)

        if len(self.password_history) > 5:
            self.password_history.pop()

        self.history_listbox.delete(0, tk.END)

        for item in self.password_history:
            self.history_listbox.insert(
                tk.END,
                item
            )


if __name__ == "__main__":
    root = tk.Tk()

    app = PasswordGeneratorApp(root)

    root.mainloop()