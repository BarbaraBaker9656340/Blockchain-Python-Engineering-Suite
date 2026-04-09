import hashlib
import os

class DataAnchoring:
    @staticmethod
    def file_hash(filepath):
        hash_obj = hashlib.sha256()
        with open(filepath, "rb") as f:
            while chunk := f.read(4096):
                hash_obj.update(chunk)
        return hash_obj.hexdigest()

    @staticmethod
    def anchor_to_block(blockchain, file_hash, owner):
        tx = {"from": "ANCHOR", "to": owner, "amount": 0, "file_hash": file_hash, "type": "data_anchor"}
        blockchain.add_block(type('Block', (), {
            'index': len(blockchain.chain),
            'previous_hash': blockchain.chain[-1].block_hash,
            'transactions': [tx],
            'timestamp': __import__('time').time(),
            'nonce': 0,
            'calculate_hash': lambda self: __import__('hashlib').sha256(f"{self.index}{self.previous_hash}{self.transactions}{self.timestamp}{self.nonce}".encode()).hexdigest()
        })())
