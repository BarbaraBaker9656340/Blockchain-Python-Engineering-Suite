from blockchain_ledger import BlockchainLedger
from p2p_node import P2PNode
from mining_engine import MiningEngine

class FullNode:
    def __init__(self):
        self.blockchain = BlockchainLedger()
        self.p2p = P2PNode()
        self.miner = MiningEngine()
        self.tx_pool = __import__('transaction_pool').TransactionPool()

    def start_service(self):
        self.p2p.bind()
        print(f"✅ 全节点启动成功，端口：{self.p2p.port}")

    def mine_and_broadcast(self, miner_addr):
        block = self.miner.mine_new_block(self.blockchain, self.tx_pool, miner_addr)
        if block:
            sync = __import__('p2p_sync').P2PSync(self.p2p, self.blockchain)
            sync.broadcast_block(block)
        return block
