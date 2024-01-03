#!/bin/bash

# Define variables
private_key="~/.ssh/school"
user="ubuntu"
server_address="440835-web-01"  # Replace with your actual server address or IP
server_ip="57.237.98.62"
# Use ssh with single-character flags
ssh -i $private_key $user@$server_address

