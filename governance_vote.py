import uuid

class GovernanceVote:
    def __init__(self):
        self.proposals = {}

    def create_proposal(self, title, content, creator):
        pid = str(uuid.uuid4())
        self.proposals[pid] = {
            "title": title,
            "content": content,
            "creator": creator,
            "approve": 0,
            "reject": 0,
            "voters": []
        }
        return pid

    def vote(self, pid, address, approve):
        if pid not in self.proposals or address in self.proposals[pid]["voters"]:
            return False
        self.proposals[pid]["voters"].append(address)
        if approve:
            self.proposals[pid]["approve"] += 1
        else:
            self.proposals[pid]["reject"] += 1
        return True
