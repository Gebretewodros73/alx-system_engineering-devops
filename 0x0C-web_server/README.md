# 0x0C-web_server

This directory contains the solutions for the web server project in the ALX System Engineering & DevOps curriculum.

## Table of Contents
- [Introduction](#introduction)
- [Learning Objectives](#learning-objectives)
- [Tasks](#tasks)

## Introduction
The web server project focuses on configuring and setting up a web server using Nginx. It covers various aspects of web servers, including file transfer, installation, domain setup, redirection, and error handling.

## Learning Objectives
By completing the tasks in this project, you will gain knowledge and skills in the following areas:
- Understanding the main role of a web server
- Explaining the concept of a child process
- Configuring Nginx web server according to requirements
- Setting up domain names and DNS records
- Implementing URL redirection and error handling

## Tasks
The project consists of multiple tasks, each addressing specific objectives and requirements. Here are the tasks included in this project:

1. [Transfer a file to your server](./0-transfer_file)
   - Write a Bash script to transfer a file from the client to the server using scp.
   - Usage: `0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY`

2. [Install nginx web server](./1-install_nginx_web_server)
   - Install Nginx on your web-01 server and configure it to listen on port 80.
   - Verify the installation by querying Nginx and checking for the expected response.

3. [Setup a domain name](./2-setup_a_domain_name)
   - Configure DNS records for a domain name to point to your web-01 server.
   - Ensure proper propagation of DNS records.

4. [Redirection](./3-redirection)
   - Configure Nginx to redirect requests to the "/redirect_me" path to another page using a 301 redirection.

5. [Not found page 404](./4-not_found_page_404)
   - Customize the Nginx 404 error page to display the message "Ceci n'est pas une page" (This is not a page).

6. [Install Nginx web server (w/ Puppet)](./7-puppet_install_nginx_web_server.pp)
   - Use Puppet to install and configure Nginx server, including a 301 redirection and the expected response on the root path.

Please refer to the individual task files for more details and instructions.
