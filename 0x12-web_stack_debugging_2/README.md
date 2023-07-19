# Web Stack Debugging 2

This repository contains solutions to the debugging tasks related to web stack configuration and user privilege management. Each task focuses on fixing specific issues and improving the security and functionality of the system. Below are the details of each task:

## Task 0: Run software as another user
In this task, the goal is to write a Bash script that accepts a username as an argument and runs the `whoami` command under the specified user. The script should be tested with different users to ensure proper functionality.

- Script File: [0-iamsomeoneelse](./0x12-web_stack_debugging_2/0-iamsomeoneelse)

## Task 1: Run Nginx as Nginx
The objective of this task is to configure the Nginx web server to run as the `nginx` user instead of the default `root` user. This helps to limit the potential impact of security breaches. The Nginx server should also be set to listen on all active IPs on port 8080.

- Script File: [1-run_nginx_as_nginx](./1-run_nginx_as_nginx)

## Task 2: 7 lines or less (advanced)
Building upon the previous task, this advanced task requires fixing the Nginx configuration in a more concise manner. The Bash script should be limited to 7 lines or less, adhering to additional restrictions mentioned in the task description.

- Script File: [100-fix_in_7_lines_or_less](./100-fix_in_7_lines_or_less)

## Repository Details

- GitHub repository: [alx-system_engineering-devops](https://github.com/gebretewodros73/alx-system_engineering-devops)
- Directory: 0x12-web_stack_debugging_2
