from strength_checker import calculate_strength


print("=== Password Strength Test ===")

test_passwords = [
    "abc",
    "abcdefgh",
    "abcdef12",
    "Abcdef12",
    "Abcdef12!",
    "Abcdefgh1234!"
]

for password in test_passwords:
    strength = calculate_strength(password)

    print(
        f"Password: {password:<20} "
        f"Strength: {strength}"
    )