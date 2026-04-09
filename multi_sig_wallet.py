class MultiSigWallet:
    def __init__(self, required_signatures, owner_addresses):
        self.required = required_signatures
        self.owners = owner_addresses
        self.signatures = {}

    def add_signature(self, tx_id, address):
        if address not in self.owners:
            return False
        if tx_id not in self.signatures:
            self.signatures[tx_id] = []
        if address not in self.signatures[tx_id]:
            self.signatures[tx_id].append(address)
        return True

    def is_tx_approved(self, tx_id):
        return len(self.signatures.get(tx_id, [])) >= self.required
