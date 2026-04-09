class PBFTConsensus:
    def __init__(self, node_count=4):
        self.node_count = node_count
        self.max_faulty = (node_count - 1) // 3
        self.pre_prepare = {}
        self.prepare = {}
        self.commit = {}

    def pre_prepare_stage(self, block_hash, node_id):
        self.pre_prepare[block_hash] = node_id

    def prepare_stage(self, block_hash, node_id):
        if block_hash not in self.prepare:
            self.prepare[block_hash] = []
        self.prepare[block_hash].append(node_id)

    def commit_stage(self, block_hash, node_id):
        if block_hash not in self.commit:
            self.commit[block_hash] = []
        self.commit[block_hash].append(node_id)

    def is_consensus_reached(self, block_hash):
        prepare_ok = len(self.prepare.get(block_hash, [])) >= 2 * self.max_faulty
        commit_ok = len(self.commit.get(block_hash, [])) >= 2 * self.max_faulty
        return prepare_ok and commit_ok
