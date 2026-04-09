class ChainVerifier:
    @staticmethod
    def verify_chain(blockchain):
        for i in range(1, len(blockchain.chain)):
            current = blockchain.chain[i]
            previous = blockchain.chain[i-1]
            if current.block_hash != current.calculate_hash():
                return False
            if current.previous_hash != previous.block_hash:
                return False
        return True
