# 0x0F-load_balancer

This directory contains the source code for the "Load Balancer" project. The project focuses on configuring load balancers and web servers to distribute traffic and handle HTTP requests efficiently.

## Table of Contents
1. [Learning Objectives](#learning-objectives)
2. [Tasks](#tasks)

## Learning Objectives

The main objective of this project is to understand the concept of load balancers and their role in distributing traffic among multiple servers. By the end of this project, you should be able to:
- Configure Nginx to add custom HTTP response headers
- Install and configure HAProxy as a load balancer
- Automate server configuration using Bash and Puppet

## Tasks

### 0. Double the number of webservers
**File:** [0-custom_http_response_header](./0-custom_http_response_header)

In this task, the goal is to configure the web-02 server to be identical to web-01 and add a custom Nginx response header. The custom header, named "X-Served-By," should contain the hostname of the server Nginx is running on.

To complete this task, follow the steps below:
1. Configure Nginx on both web-01 and web-02 to add the custom header with the appropriate value.
2. Write a Bash script, `0-custom_http_response_header`, that automates the configuration of a new Ubuntu machine to meet the requirements mentioned above.

Please refer to the actual source code file [0-custom_http_response_header](./0-custom_http_response_header) for the specific solution.

### 1. Install your load balancer
**File:** [1-install_load_balancer](./1-install_load_balancer)

In this task, you need to install and configure HAProxy on the lb-01 server. HAProxy will be responsible for load balancing traffic between web-01 and web-02 using a round-robin algorithm.

To accomplish this task, follow the steps below:
1. Install HAProxy on the lb-01 server.
2. Configure HAProxy to distribute requests evenly between web-01 and web-02.
3. Ensure that HAProxy can be managed using an init script.
4. Write a Bash script, `1-install_load_balancer`, that configures a new Ubuntu machine to meet the requirements mentioned above.

Please refer to the actual source code file [1-install_load_balancer](./1-install_load_balancer) for the specific solution.

### 2. Add a custom HTTP header with Puppet
**File:** [2-puppet_custom_http_response_header.pp](./2-puppet_custom_http_response_header.pp)

In this advanced task, you need to automate the creation of a custom HTTP header response using Puppet. The header, named "X-Served-By," should contain the hostname of the server Nginx is running on.

To complete this task, follow the steps below:
1. Write a Puppet manifest, `2-puppet_custom_http_response_header.pp`, that configures a new Ubuntu machine to add the custom header with the appropriate value.

Please refer to the actual source code file [2-puppet_custom_http_response_header.pp](./2-puppet_custom_http_response_header.pp) for the specific solution.

Remember to document your progress and any troubleshooting steps taken during the configuration process.


