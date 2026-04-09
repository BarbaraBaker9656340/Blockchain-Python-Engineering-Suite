import socket

class PeerDiscovery:
    @staticmethod
    def scan_network(base_ip="127.0.0.1", start=8000, end=8010):
        alive = []
        for port in range(start, end+1):
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.1)
                if s.connect_ex((base_ip, port)) == 0:
                    alive.append((base_ip, port))
                s.close()
            except:
                continue
        return alive
