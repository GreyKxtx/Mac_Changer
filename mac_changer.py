#!/usr/bin/env python
import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()  # экземпляр класса OptionParser
    parser.add_option("-i", "--interface", dest='interface', help="Interface to change its Mac address")
    parser.add_option("-m", "--mac", dest='new_mac', help="New MAC address")
    (options, arguments) = parser.parse_args()
    if  not options.interface:
        parser.error("[-] Please specify an interface, use --help to more inrfo")
    elif not options.new_mac:
        parser.error("[-] Please specify a new MAC, use --help to more inrfo")
    return options
def change_mac(interface, new_mac):
    print("\n[+] Changing MAC addres for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    ifconfig_result = ifconfig_result.decode()  # convert from bytes to string
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-]Could not find MAC address.")

options = get_arguments()

current_mac = get_current_mac(options.interface)
print("Current MAC :" + str(current_mac))

change_mac(options.interface,options.new_mac)

current_mac = get_current_mac(options.interface)

if current_mac == options.new_mac:
    print("[+] Mac address was successfully changed to " + current_mac)
else:
    print("[-] Mac address did not get chenged")






