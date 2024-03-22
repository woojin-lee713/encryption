def encrypt_code(source, key, shift):
    source = source.lower()  # Assuming case insensitivity

    while len(source) > 10:
        raise ValueError("Source too long")

    if key == 0:
        return source

    elif -10 <= key <= 10:
        if shift == "right":
            shifted_code = ""
            for char in source:
                shifted_char = chr(((ord(char) - 97 + key) % 26) + 97) if char.isalpha() else char
                shifted_code += shifted_char
            return shifted_code
        elif shift == "left":
            shifted_code = ""
            for char in source:
                shifted_char = chr(((ord(char) - 97 - key) % 26) + 97) if char.isalpha() else char
                shifted_code += shifted_char
            return shifted_code
        else:
            raise ValueError("Invalid shift")

    else:
        raise ValueError("Key exceeds length")
