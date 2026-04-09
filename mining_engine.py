from pow_consensus import PoWConsensus

class MiningEngine:
    def __init__(self):
        self.pow = PoWConsensus()
        self.miner_reward = 10.0

    def mine_new_block(self, blockchain, tx_pool, miner_address):
        if tx_pool.get_pending_count() == 0:
            return None
        reward_tx = [{"from": "MINING_REWARD", "to": miner_address, "amount": self.miner_reward}]
        new_block = type('Block', (), {})()
        new_block.index = len(blockchain.chain)
        new_block.transactions = tx_pool.pending_transactions + reward_tx
        new_block.previous_hash = blockchain.chain[-1].block_hash
        new_block.timestamp = __import__('time').time()
        new_block.nonce = 0
        new_block.calculate_hash = lambda: __import__('hashlib').sha256(f"{new_block.index}{new_block.previous_hash}{new_block.transactions}{new_block.timestamp}{new_block.nonce}".encode()).hexdigest()
        new_block.block_hash = new_block.calculate_hash()
        mined_block = self.pow.mine_block(new_block)
        blockchain.add_block(mined_block)
        tx_pool.clear_pool()
        return mined_block
