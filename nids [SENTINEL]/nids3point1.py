from scapy.all import sniff, TCP, Raw, IP
import re

LOG4SHELL_PATTERN = re.compile(rb'\$\{jndi:ldap://', re.IGNORECASE)

def detect_log4shell(packet):
    if packet.haslayer(TCP) and packet[TCP].dport == 8080 and packet.haslayer(Raw):
        payload = packet[Raw].load
        if LOG4SHELL_PATTERN.search(payload):
            print(f"*ALERT* Log4Shell exploit attempt detected from {packet[IP].src}")

sniff(filter="tcp port 8080", prn=detect_log4shell, store=0)