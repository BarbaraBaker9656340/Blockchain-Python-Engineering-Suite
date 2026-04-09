import json
from cryptography.fernet import Fernet

class KeyManager:
    def __init__(self, password):
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)
        self.password = password

    def save_private_key(self, wallet, path="key.encrypted"):
        data = {"priv": wallet.private_key.to_string().hex(), "addr": wallet.address}
        encrypted = self.cipher.encrypt(json.dumps(data).encode())
        with open(path, "wb") as f:
            f.write(encrypted)

    def load_private_key(self, path="key.encrypted"):
        with open(path, "rb") as f:
            encrypted = f.read()
        raw = self.cipher.decrypt(encrypted)
        return json.loads(raw)
