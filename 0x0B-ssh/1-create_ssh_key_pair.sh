#!/bin/bash

# Define variables
key_name="school"
key_bits=4096
passphrase="betty"

# Generate RSA key pair
ssh-keygen -t rsa -b $key_bits -f ~/.ssh/$key_name -N $passphrase

echo "RSA key pair created successfully!"
echo "Private key saved as ~/.ssh/$key_name"
echo "Public key saved as ~/.ssh/$key_name.pub"
