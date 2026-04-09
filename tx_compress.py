import zlib
import json

class TransactionCompressor:
    @staticmethod
    def compress_tx_list(tx_list):
        tx_json = json.dumps([tx.to_dict() for tx in tx_list]).encode()
        return zlib.compress(tx_json)

    @staticmethod
    def decompress_tx_list(compressed_data):
        raw = zlib.decompress(compressed_data)
        return json.loads(raw)
