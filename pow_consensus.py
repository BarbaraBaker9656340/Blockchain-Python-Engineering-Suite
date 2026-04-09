class PoWConsensus:
    def __init__(self, difficulty=4):
        self.difficulty = difficulty

    def mine_block(self, block):
        target = "0" * self.difficulty
        while block.block_hash[:self.difficulty] != target:
            block.nonce += 1
            block.block_hash = block.calculate_hash()
        return block

    def adjust_difficulty(self, last_block_time, current_time):
        if current_time - last_block_time < 10:
            self.difficulty += 1
        elif current_time - last_block_time > 20:
            self.difficulty = max(1, self.difficulty - 1)
