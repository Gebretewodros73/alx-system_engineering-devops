# Firewall Configuration Repository

This repository explores the concepts of firewalls and contains tasks related to configuring and managing firewalls using the `ufw` (Uncomplicated Firewall) utility. The tasks are organized into separate files, each focusing on a specific firewall configuration scenario. Below are the tasks included in this repository:

## [Task 0: Block all incoming traffic but](./0-block_all_incoming_traffic_but)

In this task, the goal is to configure the `ufw` firewall on `web-01` to block all incoming traffic except for specific TCP ports. The required TCP ports to be allowed are:
- Port 22 (SSH)
- Port 443 (HTTPS SSL)
- Port 80 (HTTP)

The `0-block_all_incoming_traffic_but` file in this repository contains the necessary commands and configuration to achieve this firewall setup. Feel free to apply these rules to other servers (`lb-01` and `web-02`), although they won't be checked.

## [Task 1: Port forwarding (advanced)](./100-port_forwarding)

In this advanced task, the focus is on configuring port forwarding using the firewall. Specifically, the goal is to configure `web-01` to redirect incoming TCP traffic on port 8080 to port 80. This means that any requests received on port 8080 should be automatically forwarded to port 80.

The `100-port_forwarding` file in this repository provides the modified configuration of the `ufw` firewall on `web-01` to enable port forwarding. You can refer to this file to understand how the port forwarding setup was achieved.

Please note that the `netstat` output and `curl` commands are included in the task description to demonstrate the successful redirection of traffic from port 8080 to port 80.

## Repository Details

- GitHub Repository: [alx-system_engineering-devops](https://github.com/gebretewodros73/alx-system_engineering-devops)
- Directory: [0x13-firewall](https://github.com/gebretewodros73/alx-system_engineering-devops/0x13-firewall)

Feel free to explore the repository and access the task files for detailed information on the firewall configurations.
