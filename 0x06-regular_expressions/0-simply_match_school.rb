#!/usr/bin/env ruby

# Define the regular expression
pattern = /School/

# Get the argument from the command line
input_string = ARGV[0]

# Find all matches using the scan method
matches = input_string.scan(pattern)

# Print the matches
puts matches.join

