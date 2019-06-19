#!/usr/bin/env python

import subprocess
import random


def create_mac():

    new_mac = " "
    for x in range(6):
        rand_int = random.randint(10, 99)
        int_string = str(rand_int)
        if x == 5:
            new_mac += int_string
        else:
            new_mac += int_string + ":"

    return new_mac


def change_mac():

    n_mac = create_mac()

    print("New Mac Address randomly created is: " + str(n_mac))

    subprocess.call(["sudo", "ifconfig", "en0", "down"])
    subprocess.call(["sudo", "ifconfig", "en0", "ether", n_mac])
    subprocess.call(["sudo", "ifconfig", "en0", "up"])
    print("[+] MAC address changed.")
    subprocess.call(["sudo", "ifconfig", "en0"])


if __name__ == '__main__':
    change_mac()


