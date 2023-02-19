# Ping-Sweeper

## Bash Ping Sweeper
This Bash script performs a ping sweep of a target IP address range and prints the IP addresses of any valid responses.

### Usage
To use this script, run the following command:

`./ping_sweeper.sh <ip_address_prefix> <start_octet> <end_octet>`

Replace `<ip_address_prefix>` with the first three octets of the IP address you want to sweep, and replace `<start_octet>` and `<end_octet>` with the range of the last octet that you want to sweep.

For example, to sweep the IP addresses from 192.168.1.1 to 192.168.1.255, you would run:

`./ping_sweeper.sh 192.168.1 1 255`

The script will only print the IP addresses of any valid responses (one IP address per line) and nothing else.

## Disclaimer
This script is provided for educational purposes only. Please ensure that you have permission from the target system's owner before running this script.
