# Puppet manifest to execute a command to kill a process

exec { 'killmenow':
  command => '/usr/bin/pkill killmenow',
}
