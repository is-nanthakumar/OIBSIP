import re


def validate_username(username):
    if not username:
        return False, "Username cannot be empty."

    if len(username) < 3 or len(username) > 20:
        return False, "Username must be 3-20 characters."

    if not re.fullmatch(r"[A-Za-z0-9_]+", username):
        return False, "Username can contain only letters, numbers and underscore."

    return True, ""


def validate_password(password):
    if not password:
        return False, "Password cannot be empty."

    if len(password) < 4 or len(password) > 100:
        return False, "Password must be 4-100 characters."

    return True, ""


def validate_room_name(room_name):
    if not room_name:
        return False, "Room name cannot be empty."

    if len(room_name) < 1 or len(room_name) > 30:
        return False, "Room name must be 1-30 characters."

    if not re.fullmatch(r"[A-Za-z0-9 _-]+", room_name):
        return False, "Room name contains invalid characters."

    return True, ""


def validate_message(message):
    if not message:
        return False, "Message cannot be empty."

    if len(message) > 1000:
        return False, "Message cannot exceed 1000 characters."

    return True, ""