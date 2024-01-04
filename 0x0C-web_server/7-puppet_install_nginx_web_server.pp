package { 'nginx':
 ensure => installed,
}

file_line { 'install':
 ensure => 'present',
 path   => '/etc/nginx/sites-enabled/default',
 after => 'listen 80 default_server;',
 line   => 'rewrite ^/redirect_me http:https://github.com/DjangoSpop/alx-system_engineering-devops;',
}

file { '/var/www/html/index.html':
 content => 'Hello World!',
}

file { '/var/www/html/404.html':
 content => 'Error 404: Page not found!',
}
 service { 'nginx':
 ensure => running,
 require => Package['nginx'],
}

file { '/etc/nginx/sites-enabled/default':
 ensure => file,
 notify => Service['nginx'],
 content => "
 server {
     listen 80 default_server;
     listen [::]:80 default_server;

     root /var/www/html;
     index index.html index.htm index.nginx-debian.html;

     server_name _;

     location / {
       try_files $uri $uri/ =404;
     }

     error_page 404 /404.html;
     location = /404.html {
       internal;
     }
 }
 ",
}

