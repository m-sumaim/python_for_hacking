# 🛡️ Python for Hacking

A small collection of Python scripts to demonstrate basic offensive security techniques. Intended for learning and hands-on practice.

> ⚠️ For educational use only. Run these scripts only on systems and networks you own or have permission to test.

## Requirements
- Python 3  
- Linux (Kali Linux recommended)  
- Root privileges  
- `scapy` (`pip3 install scapy`)

## Usage
### 1. Basic Mac Address Changer
> python3 1_basic_mac_address_changer.py -i eth0 -m 00:11:22:33:44:89
#### *i - network interface, m - new MAC address*

### 2. Network Scanner:
> python3 2_Network_Scanner.py -t 192.168.111.0/24             
#### *t - target IP address*

### 3. ARP Spoofer (MITM)
> python3 3_arpspoof.py -t 192.168.111.135 -g 192.168.111.2
#### *t - victim's IP address, g - gateway's IP address*

### 4. Packet Sniffer (MITM)
> python3 4_packet_sniffer.py
#### *to sniff packets on a victim machine, run 3_arp_spoof.py to create an MITM first*

### 5. DNS Spoofer (MITM)
> python3 3_arpspoof.py -t 192.168.111.135 -g 192.168.111.2<br>
> iptables -I FORWARD -j NFQUEUE --queue-num 0 <br>
> python3 5_dns_spoofer.py 
##### *step-1 : run 3_arp_spoof.py to create an MITM<br> step-2: modify iptables to create queues for storing incoming packets<br> step-3: run 5_dns_spoofer.py to create spoofing <br> You need to run another server hosting malicious website*