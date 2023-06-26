# Attack is the best defense

This project focuses on various topics related to security, DevOps, scripting, and hacking. It is an optional project that offers additional credit and is designed to enhance your understanding and practical skills in these areas.

## Concepts

To successfully complete this project, familiarize yourself with the following concepts:

- Network basics
- Docker
- Security concepts such as network sniffing, ARP spoofing, and dictionary attacks

## Background Context

The purpose of this project is to explore network security, with a specific focus on intercepting unencrypted traffic and gathering information from it. Although modern network security measures have improved, some legacy systems still rely on unencrypted communication methods, making them vulnerable to potential attacks. By understanding these vulnerabilities, you can better appreciate the importance of secure communication practices.

Throughout the project, you will encounter different tasks that involve network sniffing, ARP spoofing, dictionary attacks, and more. The project provides real-world examples and scenarios to help you gain practical experience in various security-related techniques.

## Resources

To successfully complete this project, you may find the following resources helpful:

- Read or watch content related to:
  - [Network sniffing](https://www.lifewire.com/definition-of-sniffer-817996)
  - [ARP spoofing](https://www.veracode.com/security/arp-spoofing)
  - [Connecting to SendGrid's SMTP relay using telnet](https://docs.sendgrid.com/ui/account-and-settings/troubleshooting-delays-and-latency)
  - [Docker and its popularity](https://www.zdnet.com/article/what-is-docker-and-why-is-it-so-darn-popular/)
  - [Dictionary attacks](https://en.m.wikipedia.org/wiki/Dictionary_attack)
- Refer to the `man` or `help` pages of the following commands:
  - tcpdump
  - hydra
  - telnet
  - docker

## Tasks

This project consists of multiple tasks. Each task will build upon the knowledge and skills acquired in the previous ones. Below is an overview of the tasks involved:

### Task 0: ARP Spoofing and Sniffing Unencrypted Traffic (Advanced)

In this task, you will delve into network security by intercepting unencrypted traffic through ARP spoofing. By redirecting traffic to a malicious machine, you can analyze the intercepted data for potential sensitive information. The task involves sniffing unencrypted traffic and forwarding it to its intended destination while remaining undetected. The provided example showcases using telnet to send an email via SendGrid's SMTP relay. Your objective is to execute the `user_authenticating_into_server` script locally and use `tcpdump` to sniff the network and find the password. Please note that the script won't work on Docker containers or macOS.

**File:** [0-sniffing](./0-sniffing)

### Task 1: Dictionary Attack (Advanced)

This task explores password-based authentication systems and the vulnerabilities associated with them. You will conduct a dictionary attack on an SSH account using the Docker environment. The objective is to find the password for the SSH account named `sylvain`. You will need to install Docker, pull and run the Docker image `sylvainkalache/264-1`, acquire a password dictionary, and use `hydra` to attempt a brute force attack on the SSH account. The Docker container can be accessed locally via IP address `127.0.0.1` and port `2222`.

**File:** [1-dictionary_attack](./1-dictionary_attack)

## Learning Objectives

- Gain a deeper understanding of network security and its importance
- Familiarize yourself with techniques such as network sniffing, ARP spoofing, and dictionary attacks
- Apply your knowledge of Docker and its usage in security-related scenarios
- Enhance your scripting skills by executing provided scripts and customizing them to meet project requirements
- Develop critical thinking and problem-solving abilities in the context of security and DevOps practices

Best of luck with your project, and have fun exploring the exciting world of security, DevOps, scripting, and hacking!

**Note:** Please refer to the actual project repository for the most up-to-date instructions and files related to this project.
