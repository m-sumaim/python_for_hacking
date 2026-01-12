#!/usr/bin/env python

import subprocess
import optparse

# MANUAL UPDATION OF MAC ADDRESS
subprocess.call("ifconfig wlan0 down", shell=True)
subprocess.call("ifconfig wlan0 hw ether 00:11:22:33:44:55", shell=True)
subprocess.call("ifconfig wlan0 up", shell=True)

# UPDATION WITHOUT HARD CODING
interface = input("interface > ")
new_mac = input("new MAC address > ")                               
print("[+] Chaning MAC addr for " + interface + "to" + new_mac)

subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)

# UPDATION WITH SECURE INPUT PROCESSING
subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])

#-------------------------------------------------------------------------------
# USING PARSER AGRUMENTS PASSED DURING CODE EXECUTION

parser = optparse.OptionParser()           #parser to hadle user input

parser.add_option("-i", "--interfaces", dest="interface", help="Interface to change its MAC address")
parser.add_option("-m", "--mac", dest="new_mac", help="New mac address")
(options, arguments) = parser.parse_args()                       # allows the object to understand what the user has wriiten and how to handle it"

interface = options.interface
new_mac = options.new_mac
print("[+] Chaning MAC addr for " + interface + "to" + new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])


# USING FUNCTIONS
#!/usr/bin/env python

import subprocess
import optparse

def get_arguments():
		parser = optparse.OptionParser()           #parser to hadle user input
		parser.add_option("-i", "--interfaces", dest="interface", help="Interface to change its MAC address")
		parser.add_option("-m", "--mac", dest="new_mac", help="New mac address")
		(options, arguments) = parser.parse_args()    
		if not options.interface:
				parser.error("[-] Please specify an interface, use --help for more info.")
		elif not options.new_mac:
				parser.error("[-] Please specify a new mac, use --help for more info.")
		return options
		
def change_mac(interface, new_mac):
		print("[+] Chaning MAC addr for " + interface + "to" + new_mac)
		subprocess.call(["ifconfig", interface, "down"])
		subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
		subprocess.call(["ifconfig", interface, "up"])

options = get_arguments()
change_mac(options.interface, options.new_mac)




