from scapy.all import sniff, IP
import time

MALICIOUS = {"4.2.2.2"}
alert_ts={}
timeout=10

def cb(p):
    if IP in p:
        srcip = p[IP].src
        dstip = p[IP].dst

        if srcip in MALICIOUS or dstip in MALICIOUS:
            a=(srcip,dstip)
            curr = time.time()
            if a not in alert_ts or (curr - alert_ts[a] > timeout):
                print(f"*ALERT* Communication between malicious IP {srcip} and {dstip}")
                alert_ts[a] = curr
    
def sniffH():
    interface = "vmenet3"
    print(f"starting NIDS on {interface}...")
    sniff(iface=interface, filter="ip", prn=cb, store=False)

if __name__ == "__main__":
    sniffH()