class BlockIndexer:
    def __init__(self, blockchain):
        self.blockchain = blockchain
        self.index_map = {}
        self.build_index()

    def build_index(self):
        for block in self.blockchain.chain:
            self.index_map[block.index] = block.block_hash
            self.index_map[block.block_hash] = block.index

    def get_block_hash(self, height):
        return self.index_map.get(height)

    def get_block_height(self, block_hash):
        return self.index_map.get(block_hash)
