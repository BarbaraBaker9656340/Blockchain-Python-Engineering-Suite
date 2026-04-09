from block_core import Block

def create_genesis_block():
    genesis_transactions = [{"from": "GENESIS", "to": "SYSTEM", "amount": 0, "type": "genesis"}]
    genesis_block = Block(
        index=0,
        previous_hash="0" * 64,
        transactions=genesis_transactions
    )
    print("✅ 创世区块创建完成")
    return genesis_block

if __name__ == "__main__":
    create_genesis_block()
