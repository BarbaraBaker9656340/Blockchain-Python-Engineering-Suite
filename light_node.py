class LightNode:
    def __init__(self):
        self.block_headers = []

    def sync_header(self, block_header):
        self.block_headers.append(block_header)

    def verify_block(self, block_hash):
        for header in self.block_headers:
            if header["hash"] == block_hash:
                return True
        return False
