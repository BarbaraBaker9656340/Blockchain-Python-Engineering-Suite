class CrossChainProxy:
    def __init__(self):
        self.bridge_records = {}

    def lock_asset(self, source_chain, address, amount, lock_id):
        self.bridge_records[lock_id] = {
            "chain": source_chain,
            "address": address,
            "amount": amount,
            "status": "locked"
        }

    def mint_asset(self, lock_id, target_chain):
        if lock_id in self.bridge_records:
            self.bridge_records[lock_id]["status"] = "minted"
            self.bridge_records[lock_id]["target_chain"] = target_chain
            return True
        return False
