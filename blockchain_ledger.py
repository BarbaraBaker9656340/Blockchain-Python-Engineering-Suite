from genesis_block import create_genesis_block

class BlockchainLedger:
    def __init__(self):
        self.chain = [create_genesis_block()]

    def add_block(self, new_block):
        new_block.previous_hash = self.chain[-1].block_hash
        new_block.block_hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def get_chain_length(self):
        return len(self.chain)

    def list_all_blocks(self):
        return [{"index": b.index, "hash": b.block_hash} for b in self.chain]
