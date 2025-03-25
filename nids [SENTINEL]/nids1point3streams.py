from scapy.all import TCP,Raw

class StreamId:
    def __init__(self,src_ip,src_port,dst_ip,dst_port):
        self.src_ip=src_ip
        self.src_port=src_port
        self.dst_ip=dst_ip
        self.dst_port=dst_port

    def __hash__(self):
        return hash((self.src_ip,self.src_port,self.dst_ip,self.dst_port))

    def __eq__(self,other):
        return self.__hash__()==other.__hash__()

    def __str__(self):
        return f"{self.src_ip}:{self.src_port} -> {self.dst_ip}:{self.dst_port}"

class Stream:
    def __init__(self):
        self.data=b''

    def process_p(self,p):
        if not p.haslayer(TCP):
            return False
        if p.haslayer(Raw):
            self.data += bytes(p[Raw].load)
        if p[TCP].flags.F or p[TCP].flags.R:
            return True
        return False