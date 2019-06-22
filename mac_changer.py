#!/usr/bin/env python

import subprocess
import random
import re

def create_mac():

    new_mac = " "
    for x in range(5):
        rand_int = random.randint(10, 99)
        int_string = str(rand_int)
        if x == 4:
            new_mac += int_string
        else:
            new_mac += int_string + ":"
    return new_mac


def change_mac(interface):

    n_mac = create_mac()

    print("New Mac Address randomly created is: " + str(n_mac))

    subprocess.call(["sudo", "ifconfig", interface, "ether", n_mac])
    subprocess.call(["sudo", "ifconfig", interface, "up"])
    print("\n[+] MAC address changing...")


def get_current_mac(interface):
    
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))

    if mac_search_result:
        return mac_search_result.group(0)
    else:
        print("No MAC address found.")


if __name__ == '__main__':

    i_face = input("Please enter your interface name.")
    first_mac = get_current_mac(i_face)
    change_mac(i_face)
    current_mac = get_current_mac(i_face)
    if current_mac != first_mac:
        print("\n[+] MAC address succefully changed.\n")
    else:
        print("[-] MAC address could not be changed.")




