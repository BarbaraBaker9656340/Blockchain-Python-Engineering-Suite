class DPoSConsensus:
    def __init__(self, delegate_count=5):
        self.delegate_count = delegate_count
        self.votes = {}
        self.delegates = []

    def vote(self, voter_address, candidate_address):
        self.votes[candidate_address] = self.votes.get(candidate_address, 0) + 1

    def elect_delegates(self):
        sorted_candidates = sorted(self.votes.items(), key=lambda x: x[1], reverse=True)
        self.delegates = [addr for addr, _ in sorted_candidates[:self.delegate_count]]
        return self.delegates

    def get_active_delegates(self):
        return self.delegates
