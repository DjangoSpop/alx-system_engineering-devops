#!/usr/bin/env bash


# Server details
server_ip="54.237.98.62"
user="ubuntu"
private_key="~/.ssh/school"

# SSH connection using single-character flags
ssh -i "$private_key" "$user@$server_ip"

# Connects to server 54.237.98.62 with key in ~/.ssh/schoossh -i ~/.ssh/school ubuntu@54.237.98.62