import secrets
import string


AMBIGUOUS_CHARACTERS = "0Ol1I"


def generate_password(
    length,
    use_uppercase=True,
    use_lowercase=True,
    use_numbers=True,
    use_symbols=True,
    exclude_ambiguous=False
):
    character_pools = []

    if use_uppercase:
        character_pools.append(string.ascii_uppercase)

    if use_lowercase:
        character_pools.append(string.ascii_lowercase)

    if use_numbers:
        character_pools.append(string.digits)

    if use_symbols:
        character_pools.append(string.punctuation)

    if not character_pools:
        raise ValueError("Select at least one character type.")

    if length < 8:
        raise ValueError("Password length must be at least 8 characters.")

    if exclude_ambiguous:
        character_pools = [
            "".join(
                character
                for character in pool
                if character not in AMBIGUOUS_CHARACTERS
            )
            for pool in character_pools
        ]

    character_pools = [
        pool for pool in character_pools if pool
    ]

    if not character_pools:
        raise ValueError("No usable characters are available.")

    password_characters = []

    for pool in character_pools:
        password_characters.append(secrets.choice(pool))

    all_characters = "".join(character_pools)

    while len(password_characters) < length:
        password_characters.append(
            secrets.choice(all_characters)
        )

    secrets.SystemRandom().shuffle(password_characters)

    return "".join(password_characters)