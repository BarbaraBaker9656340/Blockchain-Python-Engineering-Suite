from ecdsa_wallet import ECDSAWallet

class TransactionSigner:
    @staticmethod
    def sign_transaction(wallet: ECDSAWallet, transaction):
        tx_data = str(transaction.to_dict())
        signature = wallet.sign_data(tx_data)
        transaction.sign_transaction(signature)
        return signature
