from scapy.all import sniff, ARP, Ether
from nids2point1thresholds import Threshold

arp_threshold = Threshold(
    count=5,  
    window=3,  
    group_key=lambda p: p[Ether].src,  
    unique_key=lambda p: p[ARP].pdst  
)

def detect_arp_scan(packet):
    if packet.haslayer(ARP) and packet.op == 1:  
        if arp_threshold.is_exceeded(packet):
            print(f"*ALERT* ARP scan from {packet[Ether].src}")

sniff(filter="arp", prn=detect_arp_scan, store=0)