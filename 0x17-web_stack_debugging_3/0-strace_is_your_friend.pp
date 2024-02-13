# FILEPATH: /c:/Users/ahmed el bahi/alx-system_engineering-devops/0x17-web_stack_debugging_3/0-strace_is_your_friend.pp

# Install Apache package
package { 'apache2':
  ensure => installed,
}

# Configure Apache
file { '/etc/apache2/sites-available/000-default.conf':
  ensure  => file,
  content => '
    <VirtualHost *:80>
      ServerAdmin webmaster@localhost
      DocumentRoot /var/www/html
      ErrorLog ${APACHE_LOG_DIR}/error.log
      CustomLog ${APACHE_LOG_DIR}/access.log combined
    </VirtualHost>
  ',
  require => Package['apache2'],
}

# Restart Apache service
service { 'apache2':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/apache2/sites-available/000-default.conf'],
}
