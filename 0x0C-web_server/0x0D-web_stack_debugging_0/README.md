# 0x0D-web_stack_debugging_0

This directory contains the source code for the "Web Stack Debugging" project, specifically for the first task, "Give me a page!"

## Table of Contents
1. [Learning Objectives](#learning-objectives)
2. [Tasks](#tasks)

## Learning Objectives

The main objective of this project is to learn the art of debugging web stacks. As a Full-Stack Software Engineer, it is essential to have the skill to debug and troubleshoot web applications. This project focuses on debugging issues related to web servers and fixing them.

Be able to:
- Understand the concept of Docker and its usage for web development
- Identify common issues in web stacks and troubleshoot them
- Fix web server conf iguration problems
- Gain experience in using command-line tools for debugging

## Tasks

### 0. Give me a page!
**File:** [0-give_me_a_page](./0-give_me_a_page)

The goal of this task is to fix a Docker container running an Apache web server. The container should return a page containing "Hello Holberton" when queried at the root URL.

To accomplish this task, follow the steps below:
1. Start a Docker container with the image "holbertonschool/265-0", mapping port 8080 on the host to port 80 in the container.
2. Check if the web server is running correctly by using `curl` to query the container at `0:8080`. You should see an error message or an empty reply.
3. Connect to the Docker container using `docker exec` and fix the issue preventing the web server from returning the expected page.
4. Test the fixed web server by running `curl 0:8080` and verifying that it returns the expected "Hello Holberton" page.
5. Provide the command(s) used to fix the issue in your answer file.

Remember to document your progress and any troubleshooting steps taken during the debugging process.

Please refer to the actual source code file [0-give_me_a_page](./0-give_me_a_page) for the specific solution.

