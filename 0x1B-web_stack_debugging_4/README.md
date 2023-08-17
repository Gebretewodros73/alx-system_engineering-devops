# Web Stack Debugging Tasks

This directory contains solutions to web stack debugging tasks. Each task involves diagnosing and resolving issues related to web server setup and configuration.

## Task 0: Sky is the Limit, Let's Bring That Limit Higher

**Objective:** Fix the Nginx web server setup under pressure to eliminate failed requests.

- Simulated benchmarking using ApacheBench.
- Detected failed requests and server software details.
- Applied a Puppet script to fix the issue and improve performance.

[Task 0 Puppet Script (0-the_sky_is_the_limit_not.pp)](./0-the_sky_is_the_limit_not.pp)

## Task 1: User Limit

**Objective:** Adjust the OS configuration to enable login for the "holberton" user and open files without error messages.

- Demonstrated error message caused by too many open files.
- Applied a Puppet script to modify the OS configuration and address the issue.

[Task 1 Puppet Script (1-user_limit.pp)](./1-user_limit.pp)

## Repository Information

- GitHub Repository: [alx-system_engineering-devops](https://github.com/gebretewodros73/alx-system_engineering-devops)
- Directory: 0x1B-web_stack_debugging_4

Each task's solution can be found in the corresponding `.pp` file within the directory.
