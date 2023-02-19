#!/bin/bash

# Check that all three arguments are provided
if [ $# -ne 3 ]; then
  echo "Usage: $0 <ip_prefix> <start> <end>"
  exit 1
fi

# Extract the arguments
ip_prefix=$1
start=$2
end=$3

# Loop over the IP addresses in the range
for i in $(seq $start $end); do
  # Build the IP address to ping
  ip_address="$ip_prefix.$i"
  # Ping the IP address once and discard the output
  ping -c 1 $ip_address >/dev/null 2>&1
  # If the ping succeeded, print the IP address
  if [ $? -eq 0 ]; then
    echo $ip_address
  fi
done
