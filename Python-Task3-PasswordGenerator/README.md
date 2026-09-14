# Advanced Random Password Generator

A secure and user-friendly desktop password generator built with Python and Tkinter.

The application generates strong random passwords using Python's `secrets` module and provides controls for password length, character types, ambiguous character exclusion, password strength, clipboard copying, and recent password history.

## Features

- Secure password generation using Python `secrets`
- Tkinter-based graphical user interface
- Password length control from 8 to 64 characters
- Uppercase character selection
- Lowercase character selection
- Number selection
- Symbol selection
- Guaranteed at least one character from every selected type
- Optional ambiguous character exclusion
- Password strength indicator:
  - Weak
  - Medium
  - Strong
- Copy generated password to clipboard
- Stores the last 5 generated passwords during the current session
- Password history is not persisted
- Input validation and error handling

## Project Structure

```text
Python-Task3-PasswordGenerator/
│
├── app.py
├── password_generator.py
├── strength_checker.py
├── clipboard_manager.py
├── test_password_generator.py
├── test_strength_checker.py
├── requirements.txt
├── README.md
└── .gitignore

Technologies Used
Python
Tkinter
secrets
string
pyperclip
Installation

Clone the repository and navigate to the project folder.

Install the required dependency:

pip install -r requirements.txt
Run the Application
python app.py
Testing

Test the password generation engine:

python test_password_generator.py

Test the password strength checker:

python test_strength_checker.py
Security

The application uses Python's secrets module instead of the standard random module for password generation.

Each selected character category contributes at least one character to the generated password.

Generated password history is maintained only in memory during the current application session and is not stored in a file or database.

Internship Task

Track: Python Programming

Task: Task 3 - Random Password Generator

Level: Advanced


### 8.3 — `.gitignore`

Already created. Keep:

```text
__pycache__/
*.pyc
.venv/
venv/
.env