package { 'nginx':
  ensure => installed,
}

service { 'nginx':
  ensure => running,
  enable => true,
}

file { '/var/www/html/index.html':
  ensure => file,
  content => 'Hello Holberton',
}

file_line { 'nginx_config':
  path => '/etc/nginx/sites-available/default',
  after => 'listen 80 default_server;',
  line => 'rewrite ^/redirect_me https://www.youtube.com/ permanent;'  
}

package { 'curl':
  ensure => installed,
}

cron { 'script':
  command => '/usr/bin/curl 0:80 > /tmp/proof',
  hour    => '*',
  minute  => '*/1',
}