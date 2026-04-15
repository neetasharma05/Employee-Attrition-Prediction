from cryptography.fernet import Fernet

# Generate key
def generate_key():
    key = Fernet.generate_key()
    return key

# Save key to file
def save_key(key, path="secret.key"):
    with open(path, "wb") as f:
        f.write(key)

# Load key from file
def load_key(path="secret.key"):
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
        encrypted_data = f.read()

    decrypted_data = cipher.decrypt(encrypted_data)

    with open(output_path, "wb") as f:
        f.write(decrypted_data)
