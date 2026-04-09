import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, transactions, timestamp=None):
        self.index = index
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.timestamp = timestamp or time.time()
        self.nonce = 0
        self.block_hash = self.calculate_hash()

    def calculate_hash(self):
        block_data = f"{self.index}{self.previous_hash}{self.transactions}{self.timestamp}{self.nonce}"
        return hashlib.sha256(block_data.encode('utf-8')).hexdigest()

    def __str__(self):
        return f"Block #{self.index} | Hash: {self.block_hash[:16]}..."
