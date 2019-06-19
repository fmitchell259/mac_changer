#!/usr/bin/env python

import subprocess
import random


def create_mac():

    new_mac = " "
    for x in range(5):
        rand_int = random.randint(10, 99)
        int_string = str(rand_int)
        if x == 4:
            new_mac += int_string
        else:
            new_mac += int_string + ":"
    print(new_mac)
    return new_mac


def change_mac(interface):

    n_mac = create_mac()

    print("New Mac Address randomly created is: " + str(n_mac))

    subprocess.call(["sudo", "ifconfig", interface, "ether", n_mac])
    subprocess.call(["sudo", "ifconfig", interface, "up"])
    print("[+] MAC address changed.")
    subprocess.call(["sudo", "ifconfig", interface])


if __name__ == '__main__':
    i_face = input("Please enter your interface name.")
    change_mac(i_face)
    

