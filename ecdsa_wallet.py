import ecdsa
import hashlib

class ECDSAWallet:
    def __init__(self):
        self.private_key = self.generate_private_key()
        self.public_key = self.get_public_key()
        self.address = self.get_wallet_address()

    def generate_private_key(self):
        return ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)

    def get_public_key(self):
        return self.private_key.get_verifying_key()

    def get_wallet_address(self):
        pub_key_bytes = self.public_key.to_string()
        return hashlib.sha256(pub_key_bytes).hexdigest()[-40:]

    def sign_data(self, data):
        return self.private_key.sign(data.encode('utf-8')).hex()
