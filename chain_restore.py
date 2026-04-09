import json
from block_core import Block

class ChainRestore:
    @staticmethod
    def load_chain(filepath="chain_backup.json"):
        with open(filepath, "r") as f:
            data = json.load(f)
        chain = []
        for item in data:
            block = Block(
                index=item["index"],
                previous_hash=item["prev"],
                transactions=item["txs"],
                timestamp=item["time"]
            )
            block.block_hash = item["hash"]
            chain.append(block)
        return chain
