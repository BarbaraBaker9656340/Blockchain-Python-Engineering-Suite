import uuid

class NFTContract(SmartContractBase):
    def __init__(self, address, creator, nft_name):
        super().__init__(address, creator)
        self.nft_name = nft_name
        self.set_state("nfts", {})
        self.set_state("owners", {})

    def mint_nft(self, owner, metadata):
        token_id = str(uuid.uuid4())
        nfts = self.get_state("nfts")
        owners = self.get_state("owners")
        nfts[token_id] = metadata
        owners[token_id] = owner
        return token_id

    def transfer_nft(self, token_id, from_addr, to_addr):
        owners = self.get_state("owners")
        if owners.get(token_id) == from_addr:
            owners[token_id] = to_addr
            return True
        return False
