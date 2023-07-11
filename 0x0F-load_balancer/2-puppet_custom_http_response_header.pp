# Update package manager's repository metadata
exec { 'update':
  command => 'apt-get -y update',
  path    => '/usr/bin',
}

# Install Nginx server
package { 'nginx':
  ensure => installed,
  before => Exec['add_header'],
}

# Modify Nginx configuration to add custom HTTP header
exec { 'add_header':
  command     => 'sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By \"$hostname\";/" /etc/nginx/nginx.conf',
  path        => '/bin',
  refreshonly => true,
  subscribe   => Package['nginx'],
  notify      => Service['nginx'],
}

# Restart Nginx service
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
}
