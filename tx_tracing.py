class TransactionTracing:
    @staticmethod
    def trace_tx(blockchain, tx_id):
        for block in blockchain.chain:
            for tx in block.transactions:
                if hasattr(tx, "tx_id") and tx.tx_id == tx_id:
                    return {"block_height": block.index, "tx": tx.to_dict()}
                elif isinstance(tx, dict) and tx.get("tx_id") == tx_id:
                    return {"block_height": block.index, "tx": tx}
        return None
