import subprocess
from art import *
import optparse
import re

tprint("Mac-Changer",font="graffiti")

def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--interface",dest="interface", help="change interface")
    parse_object.add_option("-m","--mac",dest="mac_addr",help="manual mac address")
    
    return parse_object.parse_args()

def mac_addr_changer(user_interface, user_mac_addr): 
    subprocess.call(["ifconfig",user_interface, "down" ])
    subprocess.call(["ifconfig",user_interface, "hw" , "ether" , user_mac_addr])
    subprocess.call(["ifconfig",user_interface, "up" ])

def control_new_mac(interface):
    ifconfig = subprocess.check_output(["ifconfig", interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig))
    
    if new_mac:
        return new_mac.group(0)
    else:
        return None

print("Mac-Changer Started")

(user_input,arguments) = get_user_input()
mac_addr_changer(user_input.interface, user_input.mac_addr)
final_mac = control_new_mac(str(user_input.interface))

if final_mac == user_input.mac_addr:
    print("Success!")
else:
    print("Error")

