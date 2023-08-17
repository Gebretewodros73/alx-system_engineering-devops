# File: nginx.conf.erb

user www-data;
worker_processes 4;  # Increase this value based on your server's resources
error_log /var/log/nginx/error.log;
pid /run/nginx.pid;

events {
  worker_connections 1024;  # Increase this value based on your server's resources
}

http {
  # Other Nginx configuration settings...
}

