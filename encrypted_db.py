from cryptography.fernet import Fernet
import json

class EncryptedDatabase:
    def __init__(self, key=None):
        self.key = key or Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def save(self, data, path="encrypted_chain.db"):
        raw = json.dumps(data).encode()
        encrypted = self.cipher.encrypt(raw)
        with open(path, "wb") as f:
            f.write(encrypted)

    def load(self, path="encrypted_chain.db"):
        with open(path, "rb") as f:
            encrypted = f.read()
        raw = self.cipher.decrypt(encrypted)
        return json.loads(raw)
