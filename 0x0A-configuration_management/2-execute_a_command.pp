# site.pp

exec { 'start_killmenow_process':
  command     => '/path/to/your/start_killmenow_script', # Replace this with the actual command to start your process
  path        => ['/bin', '/usr/bin'],
  onlyif      => 'pgrep -f "killmenow"',
  refreshonly => true,
}

exec { 'killmenow_process':
  command     => 'pkill -f "killmenow"',
  path        => ['/bin', '/usr/bin'],
  onlyif      => 'pgrep -f "killmenow"',
  refreshonly => true,
  subscribe   => Exec['start_killmenow_process'],
}

