# Task 1: User Limit

# Define an `exec` resource to modify the OS configuration for the holberton user
exec { 'modify-os-configuration-for-holberton-user':
  environment => ['DIR=/etc/security/limits.conf',  # Specify the directory of the limits.conf file
                  'OLD=hard nofile 5',              # Define the old limit setting for hard nofile
                  'NEW=hard nofile 50000',          # Define the new limit setting for hard nofile
                  'OLD2=soft nofile 4',             # Define the old limit setting for soft nofile
                  'NEW2=soft nofile 40000'],       # Define the new limit setting for soft nofile
  command     => "sudo sed -i 's|$OLD|$NEW|' $DIR; sudo sed -i 's|$OLD2|$NEW2|' $DIR",  # Command to replace
  path        => ['/usr/bin', '/bin'],             # Set the search path for the command execution
  returns     => [0, 1]                            # Specify the expected return codes (0: success, 1: no changes)
}
