from password_generator import generate_password


print("=== Password Generator Test ===")

password = generate_password(
    length=16,
    use_uppercase=True,
    use_lowercase=True,
    use_numbers=True,
    use_symbols=True,
    exclude_ambiguous=True
)

print("Generated Password:", password)
print("Length:", len(password))

print("\nSecond Password:")

password_2 = generate_password(
    length=16,
    use_uppercase=True,
    use_lowercase=True,
    use_numbers=True,
    use_symbols=True,
    exclude_ambiguous=True
)

print("Generated Password:", password_2)
print("Length:", len(password_2))


print("\n=== Validation Tests ===")

# Test 1: No character type selected
try:
    generate_password(
        length=12,
        use_uppercase=False,
        use_lowercase=False,
        use_numbers=False,
        use_symbols=False
    )
except ValueError as error:
    print("No character type test: PASS")
    print("Message:", error)


# Test 2: Password length below 8
try:
    generate_password(
        length=7,
        use_uppercase=True,
        use_lowercase=True,
        use_numbers=True,
        use_symbols=True
    )
except ValueError as error:
    print("Minimum length test: PASS")
    print("Message:", error)


# Test 3: Only uppercase
password = generate_password(
    length=12,
    use_uppercase=True,
    use_lowercase=False,
    use_numbers=False,
    use_symbols=False
)

print("Uppercase-only test:", password)


# Test 4: Only numbers
password = generate_password(
    length=12,
    use_uppercase=False,
    use_lowercase=False,
    use_numbers=True,
    use_symbols=False
)

print("Numbers-only test:", password)


print("\n=== Ambiguous Character Test ===")

ambiguous_characters = "0Ol1I"

password = generate_password(
    length=30,
    use_uppercase=True,
    use_lowercase=True,
    use_numbers=True,
    use_symbols=True,
    exclude_ambiguous=True
)

print("Generated:", password)

if any(character in ambiguous_characters for character in password):
    print("Ambiguous character test: FAIL")
else:
    print("Ambiguous character test: PASS")


print("\n=== Character Guarantee Test ===")

password = generate_password(
    length=20,
    use_uppercase=True,
    use_lowercase=True,
    use_numbers=True,
    use_symbols=False,
    exclude_ambiguous=False
)

has_uppercase = any(character.isupper() for character in password)
has_lowercase = any(character.islower() for character in password)
has_number = any(character.isdigit() for character in password)

print("Password:", password)
print("Has uppercase:", has_uppercase)
print("Has lowercase:", has_lowercase)
print("Has number:", has_number)

if has_uppercase and has_lowercase and has_number:
    print("Character guarantee test: PASS")
else:
    print("Character guarantee test: FAIL")    