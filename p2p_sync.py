class P2PSync:
    def __init__(self, node, blockchain):
        self.node = node
        self.blockchain = blockchain

    def sync_chain(self, peer_blockchain):
        if len(peer_blockchain.chain) > len(self.blockchain.chain):
            self.blockchain.chain = peer_blockchain.chain
            return True
        return False

    def broadcast_block(self, block):
        for peer in self.node.peers:
            print(f"📤 发送区块至节点 {peer}: {block.block_hash[:16]}")
