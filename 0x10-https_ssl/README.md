# 0x10-https_ssl

This directory contains scripts and configuration files related to setting up HTTPS and SSL/TLS termination using HAProxy.

## Table of Contents
1. [Tasks](#Tasks)
2. [Files](#Files)

## Tasks

### 0. World wide web

Configure your domain zone and subdomains to point to the respective IP addresses using DNS. Use a Bash script to display information about the subdomains.

Requirements:

- Add the subdomain www to your domain and point it to your lb-01 IP.
- Add the subdomain lb-01 to your domain and point it to your lb-01 IP.
- Add the subdomain web-01 to your domain and point it to your web-01 IP.
- Add the subdomain web-02 to your domain and point it to your web-02 IP.
- The Bash script should accept two arguments: `domain` (mandatory) and `subdomain` (optional).
- When only the `domain` parameter is provided, the script should display information for the subdomains www, lb-01, web-01, and web-02 in that order.
- When both `domain` and `subdomain` parameters are provided, the script should display information for the specified subdomain.

### 1. HAproxy SSL termination

Configure HAProxy to handle encrypted traffic by terminating SSL and forwarding it to the web server.

Requirements:

- HAProxy should listen on TCP port 443.
- HAProxy should accept SSL traffic.
- HAProxy should serve encrypted traffic that returns the root (/) of the web server.
- The web server response should contain "Holberton School" when querying the root of the domain.

### 2. No loophole in your website traffic

Configure HAProxy to automatically redirect HTTP traffic to HTTPS.

Requirements:

- The redirection should be transparent to the user.
- HAProxy should return a 301 status code for HTTP traffic.
- HAProxy should redirect HTTP traffic to HTTPS.

## Files

- [0-world_wide_web](./0-world_wide_web): Bash script to display information about domain subdomains.
- [1-haproxy_ssl_termination](./1-haproxy_ssl_termination) : HAProxy configuration file for SSL termination.
- [100-redirect_http_to_https](./100-redirect_http_to_https) : HAProxy configuration file for HTTP to HTTPS redirection.
