from scapy.all import sniff, TCP, IP
from nids2point2thresholds import Threshold

tcp_threshold = Threshold(
    count=10,  
    window=5,  
    group_key=lambda p: p[IP].src,  
    unique_key=lambda p: p[TCP].dport  
)

def detect_tcp_scan(packet):
    if packet.haslayer(TCP) and packet[TCP].flags == 2:  
        if tcp_threshold.is_exceeded(packet):
            print(f"*ALERT* TCP scan detected from {packet[IP].src}")

sniff(filter="tcp", prn=detect_tcp_scan, store=0)