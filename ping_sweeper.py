#!/usr/bin/env python3

import subprocess
import sys

def ping(ip):
    """Ping an IP address and return True if it responds, False otherwise."""
    ping_cmd = ["ping", "-c", "1", "-W", "1", ip]
    return subprocess.call(ping_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <ip_address_prefix> <start_value> <end_value>".format(sys.argv[0]))
        sys.exit(1)

    prefix = sys.argv[1]
    start = int(sys.argv[2])
    end = int(sys.argv[3])

    for i in range(start, end+1):
        ip = "{}.{}".format(prefix, i)
        if ping(ip):
            print(ip)
