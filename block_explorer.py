class BlockExplorer:
    def __init__(self, blockchain):
        self.chain = blockchain

    def get_block_by_height(self, height):
        if 0 <= height < len(self.chain.chain):
            return self.chain.chain[height]
        return None

    def search_transaction(self, tx_id):
        from tx_tracing import TransactionTracing
        return TransactionTracing.trace_tx(self.chain, tx_id)

    def get_chain_info(self):
        return {
            "height": len(self.chain.chain)-1,
            "last_hash": self.chain.chain[-1].block_hash
        }
