from encrypt import encrypt_code

# Function to encrypt until user wants to stop
def encrypt_until_stop():
    source_code = input("Enter the source code or type 'stop' to end: ")
    if source_code == "stop":
        return source_code
    key = int(input("Enter the key: "))
    shift_direction = input("Enter 'right' or 'left' for the shift: ")
    encrypted_code = encrypt_code(source_code, key, shift_direction)
    return encrypted_code

# Example usage:
if __name__ == "__main__":
    while True:
        stop_or_encrypt = encrypt_until_stop()
        if stop_or_encrypt == "stop":
            break
        print(stop_or_encrypt)
