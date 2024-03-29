#!/usr/bin/env bash

if [ $# -lt 4 ]; then
  echo "Usage: $0 PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY"
  exit 1
fi

FILE_PATH=$1
SERVER_IP=$2 
USERNAME=$3
SSH_KEY=$4

scp -o StrictHostKeyChecking=no "$FILE_PATH" "$USERNAME@$SERVER_IP:~/" -i "$SSH_KEY"
