# Web Stack debugging: Increase limit of open files per user

# Define an `exec` resource to fix the open files limit for Nginx
exec { 'fix--for-nginx':
  environment => ['DIR=/etc/default/nginx',         # Specify the directory of the nginx configuration file
                  'OLD=ULIMIT="-n 15"',            # Define the old ULIMIT setting to be replaced
                  'NEW=ULIMIT="-n 15000"'],        # Define the new ULIMIT setting
  command     => 'sudo sed -i "s/$OLD/$NEW/" $DIR; sudo service nginx restart',  # Command to replace and restart
  path        => ['/usr/bin', '/bin'],             # Set the search path for the command execution
  returns     => [0, 1]                            # Specify the expected return codes (0: success, 1: no changes)
}
