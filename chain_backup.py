import json

class ChainBackup:
    @staticmethod
    def export_chain(blockchain, filepath="chain_backup.json"):
        chain_data = []
        for block in blockchain.chain:
            chain_data.append({
                "index": block.index,
                "hash": block.block_hash,
                "prev": block.previous_hash,
                "txs": block.transactions,
                "time": block.timestamp
            })
        with open(filepath, "w") as f:
            json.dump(chain_data, f, indent=2)
        return filepath
