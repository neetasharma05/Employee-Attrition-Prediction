from cryptography.fernet import Fernet


# ── Generate & Save Key ─────────────────────────────
def generate_key(path='leaderboard/secret.key'):
    key = Fernet.generate_key()

    with open(path, 'wb') as kf:
        kf.write(key)

    return key


# ── Load Existing Key ──────────────────────────────
def load_key(path='leaderboard/secret.key'):
    with open(path, 'rb') as kf:
        return kf.read()


# ── Encrypt Function ───────────────────────────────
def encrypt_file(input_path, output_path, key):
    cipher = Fernet(key)

    with open(input_path, 'rb') as f:
        data = f.read()

    encrypted = cipher.encrypt(data)

    with open(output_path, 'wb') as f:
        f.write(encrypted)


# ── Decrypt Function ───────────────────────────────
def decrypt_file(input_path, output_path, key):
    cipher = Fernet(key)

    with open(input_path, 'rb') as f:
        data = f.read()

    decrypted = cipher.decrypt(data)

    with open(output_path, 'wb') as f:
        f.write(decrypted)
