import hashlib

class ContractDeployer:
    @staticmethod
    def deploy_contract(creator, contract_type, params):
        contract_address = hashlib.sha256(f"{creator}{str(params)}{__import__('time').time()}".encode()).hexdigest()[-40:]
        if contract_type == "token":
            from contract_token import TokenContract
            return TokenContract(contract_address, creator, params["total"], params["name"])
        elif contract_type == "nft":
            from contract_nft import NFTContract
            return NFTContract(contract_address, creator, params["name"])
        return None
