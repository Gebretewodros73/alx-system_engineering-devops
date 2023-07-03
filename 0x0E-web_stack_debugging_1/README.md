# 0x0E-web_stack_debugging_1

This directory contains the source code for the "Web Stack Debugging 1" project. The project focuses on debugging and fixing issues related to web stack components, particularly Nginx.

## Table of Contents
1. [Learning Objectives](#learning-objectives)
2. [Tasks](#tasks)

## Learning Objectives

The main objective of this project is to enhance your debugging skills and gain a deeper understanding of web stack components. By the end of this project, you should be able to:
- Identify and troubleshoot issues related to web server configurations
- Analyze error messages and logs to pinpoint the root cause of the problem
- Write Bash scripts to automate fixes and configurations

## Tasks

### 0. Nginx likes port 80
**File:** [0-nginx_likes_port_80](./0-nginx_likes_port_80)

In this task, you need to find out why Nginx installation on an Ubuntu container is not listening on port 80. Using your debugging skills, investigate and resolve the issue. Then, write a Bash script with the minimum number of commands to automate the fix.

Requirements:
- Nginx must be running and listening on port 80 of all the server's active IPv4 IPs.
- Write a Bash script, `0-nginx_likes_port_80`, that configures a server to meet the above requirements.

Please refer to the actual source code file [0-nginx_likes_port_80](./0-nginx_likes_port_80) for the specific solution.

### 1. Make it sweet and short
**File:** [1-debugging_made_short](./1-debugging_made_short)

In this advanced task, you need to make your fix short and sweet based on the solution provided in task #0. The goal is to write a Bash script with a maximum of 5 lines (excluding the shebang) to achieve the same outcome.

Requirements:
- Your Bash script must be 5 lines long or less.
- The script should ensure that Nginx is running and listening on port 80 of all the server's active IPv4 IPs.
- The `service` command must correctly report that Nginx is not running.
- Do not use `;`, `&&`, or `wget` in the script.
- Do not execute your previous answer file (Do not include the name of the previous script in this one).

Please refer to the actual source code file [1-debugging_made_short](./1-debugging_made_short) for the specific solution.

Remember to document your progress, troubleshooting steps, and any additional findings during the debugging process.
