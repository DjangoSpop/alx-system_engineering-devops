# 100-puppet_ssh_config.pp

file_line { 'Turn off passwd auth':
  path  => '/etc/ssh/sshd_config',  # Path to your SSH client configuration file
  line  => 'PasswordAuthentication no',
}

file_line { 'Declare identity file':
  path  => '/etc/ssh/sshd_config',  # Path to your SSH client configuration file
  line  => 'IdentityFile ~/.ssh/school',
}
