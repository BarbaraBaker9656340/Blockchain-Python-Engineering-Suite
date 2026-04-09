class TransactionVerifier:
    @staticmethod
    def verify_signature(public_key, transaction, signature):
        try:
            public_key.verify(bytes.fromhex(signature), str(transaction.to_dict()).encode('utf-8'))
            return True
        except:
            return False

    @staticmethod
    def verify_balance(transaction, balance):
        return balance >= transaction.amount
