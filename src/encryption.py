from cryptography.fernet import Fernet

# Generate key and save it
def generate_key(path="leaderboard/secret.key"):
    key = Fernet.generate_key()
    with open(path, "wb") as f:
        f.write(key)
    return key

# Load key
def load_key(path="leaderboard/secret.key"):
    with open(path, "rb") as f:
        return f.read()

# Encrypt file
def encrypt_file(input_path, output_path, key):
    cipher = Fernet(key)
    with open(input_path, "rb") as f:
        data = f.read()

    encrypted_data = cipher.encrypt(data)

    with open(output_path, "wb") as f:
        f.write(encrypted_data)

# Decrypt file
def decrypt_file(input_path, output_path, key):
    cipher = Fernet(key)
    with open(input_path, "rb") as f:
        data = f.read()

    decrypted_data = cipher.decrypt(data)

    with open(output_path, "wb") as f:
        f.write(decrypted_data)
