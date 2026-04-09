import socket

class P2PNode:
    def __init__(self, host="127.0.0.1", port=0):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.peers = []

    def bind(self):
        self.socket.bind((self.host, self.port))
        self.port = self.socket.getsockname()[1]

    def add_peer(self, peer_addr):
        if peer_addr not in self.peers:
            self.peers.append(peer_addr)

    def get_peer_list(self):
        return self.peers
