# python for hacking
## To Run


# 🛡️ Python for Hacking

A small collection of Python scripts to demonstrate basic offensive security techniques such as MAC spoofing, network discovery, and ARP poisoning. Intended for learning and hands-on practice.

> ⚠️ For educational use only. Run these scripts only on systems and networks you own or have permission to test.

## Requirements
- Python 3  
- Linux (Kali Linux recommended)  
- Root privileges  
- `scapy` (`pip3 install scapy`)

## Usage
### 1. Basic Mac Address Changer
python3 1_basic_mac_address_changer.py -i eth0 -m 00:11:22:33:44:89

### 2. Network Scanner:
python3 2_Network_Scanner.py -t 192.168.111.0/24             

### 3. ARP Spoofer
python3 3_arpspoof.py -t 192.168.111.135 -g 192.168.111.2
