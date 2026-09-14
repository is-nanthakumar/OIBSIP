# Advanced Real-Time Chat Application

A multi-user real-time chat application built using Python TCP sockets, Tkinter GUI, SQLite, and threading.

The application supports user authentication, multiple chat rooms, real-time messaging, persistent message history, emoji support, notifications, input validation, and secure password storage.

---

## Features

- User registration and login
- Secure password hashing
- Server-side authentication
- Real-time multi-user messaging
- Multiple chat rooms
- Create and join named rooms
- Room-based message isolation
- Persistent message history
- Message timestamps
- Join and leave notifications
- New-message notification when the chat window is not focused
- Unicode emoji support
- Emoji shortcode support
- Input validation
- Connection error handling
- SQLite database persistence
- Graceful client disconnection

---

## Technologies Used

- Python
- TCP Socket Programming
- Tkinter
- SQLite
- Threading
- hashlib
- Regular Expressions

---

## Project Structure

```text
chat_application/
│
├── server/
│   ├── server.py
│   └── room_manager.py
│
├── client/
│   ├── app.py
│   ├── login.py
│   ├── chat_window.py
│   └── network.py
│
├── database/
│   ├── database.py
│   └── schema.sql
│
├── utils/
│   ├── security.py
│   └── validators.py
│
├── tests/
├── README.md
├── requirements.txt
└── .gitignore


How to Run
1. Open the Project Folder

Open a terminal and navigate to the project folder:

cd C:\Users\ELCOT\Desktop\OIBSIP\chat_application

2. Start the Server

From the project root:

python -m server.server

Expected output:

Database initialized successfully.
Server started on 127.0.0.1:5000
Waiting for clients...

3. Start the Client

Open another terminal:

cd C:\Users\ELCOT\Desktop\OIBSIP\chat_application\client
python login.py

Multiple clients can be started using separate terminals to test multi-user communication.

Example:

Terminal 1 -> Server
Terminal 2 -> User 1
Terminal 3 -> User 2
User Authentication

Users can:

Register a new account
Login using their username and password
Receive validation errors for invalid input
Receive an error when attempting to register an existing username

User credentials are stored in the SQLite database.

Passwords are not stored as plain text. They are stored as salted password hashes.

Chat Rooms

After successful login, users can join named chat rooms.

Example room names:

General
Python
Technology
Friends

If a requested room does not already exist in the server's active room manager, it is created automatically when the user joins it.

Users connected to the same room can communicate with each other.

Messages are isolated by room, so users in different rooms do not receive each other's chat messages.

Message History

When a user joins a room, previously stored messages from that room are loaded from SQLite.

History includes:

Username
Message
Timestamp

Example:

nantha: Hello! (2026-09-13 18:20:10)
arun: Hi! (2026-09-13 18:21:05)
Real-Time Messaging

Messages are transmitted using TCP sockets.

When a user sends a message:

The client sends the message to the server.
The server validates the message.
The message is stored in SQLite.
The server broadcasts the message to other users in the same room.
Clients display the message with username and timestamp.

Example:

[18:25] nantha: Hello everyone!

* Emoji Support

The application supports Unicode emojis directly.

Examples:

😄 ❤️ 😂 👍 🔥 🎉 🚀

It also supports emoji shortcodes.

Examples:

:smile:   -> 😄
:heart:   -> ❤️
:laugh:   -> 😂
:thumbsup: -> 👍
:fire:    -> 🔥
:party:   -> 🎉
:rocket:  -> 🚀

The client converts supported emoji shortcodes into their corresponding Unicode emojis before sending the message.

* Notifications

The application provides notifications for new messages.

When a new message is received while the chat window is not focused, a notification popup is displayed.

The notification includes:

Username
Timestamp
Message content

Join and leave notifications are also displayed inside the chat.

Example:

SYSTEM|arun joined General
Input Validation

The server validates user input before processing requests.

Validation is performed for:

Username
Password
Room name
Chat message

Examples of validation rules include:

Username length restrictions
Password length restrictions
Valid characters for usernames
Valid characters for room names
Empty message prevention
Maximum message length

Server-side validation helps prevent malformed requests and invalid data from being processed.

* Database

SQLite is used for persistent data storage.

The database contains the following tables.

Users

Stores:

User ID
Username
Password hash
Account creation time
Rooms

Stores:

Room ID
Room name
Room creation time
Messages

Stores:

Message ID
Username
Room name
Message content
Message timestamp

The SQLite database file is generated automatically when the server initializes the database.

* Security

The application includes basic security mechanisms suitable for an internship and learning project.

Password Security

Passwords are not stored as plain text.

The application uses:

PBKDF2-HMAC-SHA256

with a randomly generated salt.

The stored password format is:

salt:password_hash

The password hash is generated using 100,000 PBKDF2 iterations.

This provides significantly better password protection than storing raw passwords.

* Authentication

Users must successfully authenticate before accessing chat functionality.

Unauthenticated users cannot:

Join rooms
Send chat messages

Authentication is performed on the server.

Input Validation

User input is validated on the server before processing.

This helps prevent invalid usernames, room names, and messages from being accepted by the application.

* Data Storage

The following information is stored in SQLite:

Usernames
Password hashes
Room names
Chat messages
Message timestamps

Passwords are stored as hashes rather than plain-text passwords.

Communication Security

The current implementation uses standard TCP sockets over localhost.

The application does not currently use TLS encryption.

Therefore:

TCP communication is not encrypted using TLS.
Chat messages are not end-to-end encrypted.
SQLite database contents are not encrypted.

This project is intended for internship, demonstration, and learning purposes and is not production-grade secure messaging software.

* Error Handling

The application handles common errors such as:

Server connection failure
Invalid login credentials
Duplicate username registration
Invalid room names
Empty messages
Messages exceeding the allowed length
Attempting to chat before joining a room
Attempting to use chat functionality before login
Client disconnection
Unknown server requests

* Testing

The application can be tested using multiple clients.

Example:

Terminal 1 -> Server
Terminal 2 -> User 1
Terminal 3 -> User 2

Testing includes:

User registration
User login
Invalid login
Duplicate registration
Multiple users
Room creation/joining
Room isolation
Real-time messaging
Message history
Message timestamps
Join notifications
Leave notifications
Emoji support
Emoji shortcodes
Unfocused-window notifications
Invalid input handling
Client disconnection
Server connection failure
Example Workflow
Start Server
     |
     v
Open Client
     |
     v
Register / Login
     |
     v
Join Chat Room
     |
     v
Load Message History
     |
     v
Send / Receive Messages
     |
     v
Messages Saved in SQLite

* Project Objective

The objective of this project is to demonstrate practical knowledge of:

Python networking
TCP socket programming
Multi-threaded server design
GUI application development
User authentication
SQLite database integration
Real-time communication
Chat room management
Persistent message storage
Input validation
Basic application security
Future Improvements

Possible future enhancements include:

TLS/SSL encrypted communication
End-to-end encryption
File sharing
Image sharing
Private messaging
Online/offline user status
Message deletion
Message reactions
Improved notification system
Production-ready database architecture

* Internship Project

This project was developed as part of the Oasis Infobyte Python Programming Internship.

The implementation covers the advanced requirements of the Real-Time Chat Application project, including:

User registration and login
SQLite-based authentication
Multiple chat rooms
Room-based messaging
Persistent message history
Message timestamps
Notifications
Unicode emoji support
Emoji shortcodes
Server-side input validation
Password hashing
Security transparency and limitations