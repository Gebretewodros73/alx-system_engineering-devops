# Puppet manifest to execute a command to kill a process

exec { 'killmenow':
  command => 'pkill killmenow',
  refreshonly => true,
}

notify { 'Process terminated':
  message => 'OK',
}
