#!/usr/bin/env python

import scapy.all as scapy
import optparse

# since optparse is deprecated so we can use argparse instead
# import argparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="ip", help="IP Address range for ARP broadcasting")
    (options, arguments) = parser.parse_args()
    if not options.ip:
        parser.error("[-] Please specify an IP Address range, use --help for more information")
    return options    

# def get_arguments():
#     parser = argparse.ArgumentParser()
#     parser.add_argument("-t", "--target", dest="ip", help="IP Address range for ARP broadcasting")
#     options= parser.parse_args()
#     if not options.ip:
#         parser.error("[-] Please specify an IP Address range, use --help for more information")
#     return options

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)  # this will create a packet for arp request
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")  # create an ethernet packet for boradcasting
    arp_request_broadcast = broadcast / arp_request  # / is used to combine two packets/variables
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[
        0]  # only get first element, which is the answered element

    clients_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)

    return clients_list


def print_result(results_list):
    print("IP\t\t\tMAC Address\n-----------------------------")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])

options = get_arguments()
scan_result = scan(options.ip)
print_result(scan_result)
