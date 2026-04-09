class TxFeeCalculator:
    def __init__(self, fee_per_byte=0.0001):
        self.fee_rate = fee_per_byte

    def calculate_fee(self, transaction):
        tx_str = str(transaction.to_dict())
        size = len(tx_str.encode('utf-8'))
        return size * self.fee_rate
