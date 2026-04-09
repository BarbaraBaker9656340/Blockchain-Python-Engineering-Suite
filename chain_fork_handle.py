class ChainForkHandler:
    @staticmethod
    def select_main_chain(chains):
        if not chains:
            return None
        return max(chains, key=lambda c: len(c.chain))

    @staticmethod
    def clean_orphan_blocks(orphan_blocks):
        valid = []
        for orphan in orphan_blocks:
            if orphan.previous_hash == __import__('hashlib').sha256(str(orphan.transactions).encode()).hexdigest():
                valid.append(orphan)
        return valid
