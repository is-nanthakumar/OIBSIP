import string


def calculate_strength(password):
    score = 0

    length = len(password)

    if length >= 12:
        score += 2
    elif length >= 8:
        score += 1

    if any(character.islower() for character in password):
        score += 1

    if any(character.isupper() for character in password):
        score += 1

    if any(character.isdigit() for character in password):
        score += 1

    if any(character in string.punctuation for character in password):
        score += 1

    if score <= 2:
        return "Weak"

    if score <= 4:
        return "Medium"

    return "Strong"