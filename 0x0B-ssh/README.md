# 0x0B-ssh - DevOps Project

## Table of Contents
1. [Overview](#Overview)
2. [Background Context](#Background-Context)
3. [Learning Objectives](./Learning-Objectives)
4. [Your Servers](#Your-Servers)
5. [Tasks](#Tasks)

## Overview

This project covers various tasks related to SSH, network, sysadmin, and security. The project aims to provide a practical understanding of servers, SSH, RSA key pairs, and secure connections.

## Background Context

Along with this project, you have been attributed an Ubuntu server, living in a datacenter far far away. Like level 2 of the application process, you will connect using SSH. But contrary to level 2, you will not connect using a password but an RSA key. We’ve configured your server with the public key you created in the first task of a previous project shared on your intranet profile.

## Learning Objectives

By the end of this project, you are expected to be able to explain the following without the help of Google:

- What is a server and where servers usually live?
- What is SSH?
- How to create an SSH RSA key pair?
- How to connect to a remote host using an SSH RSA key pair?
- The advantage of using `#!/usr/bin/env bash` instead of `/bin/bash`.


### Your Servers

Name | Username | IP | State
--- | --- | --- | ---
209964-web-01 | | |


## Tasks

### Task 0: Use a private key - [0-use_a_private_key](./0-use_a_private_key)

Write a Bash script that uses SSH to connect to your server using the private key `~/.ssh/school` with the user `ubuntu`.

Requirements:

- Only use SSH single-character flags
- You cannot use `-l`
- You do not need to handle the case of a private key protected by a passphrase

Example:

```bash
$ ./0-use_a_private_key
ubuntu@server01:~$ exit
Connection to 8.8.8.8 closed.
$
```
### Task 1: Create an SSH key pair - [1-create_ssh_key_pair](./1-create_ssh_key_pair)

Write a Bash script that creates an RSA key pair.

Requirements:

* Name of the created private key must be `school`.
* Number of bits in the created key to be created 4096.
* The created key must be protected by the passphrase `betty`.

Example:

```bash
$ ./1-create_ssh_key_pair
Generating public/private rsa key pair.
Your identification has been saved in school.
Your public key has been saved in school.pub.
The key fingerprint is:
5d:a8:c1:f5:98:b6:e5:c0:9b:ee:02:c4:d4:01:f3:ba vagrant@ubuntu
The key's randomart image is:
+--[ RSA 4096]----+
|      oo...      |
|      .+.o =     |
|     o  + B +    |
|      o. = O     |
|     .. S = .    |
|      .. .       |
|      E.  .      |
|        ..       |
|         ..      |
+-----------------+
$
```

### Task 2: Client configuration - [2-ssh_configured](./2-ssh_configured)

Write a Bash script that configures the client SSH configuration file to use the private key `~/.ssh/school`:

* Your SSH client configuration must be configured to use the private key `~/.ssh/school`.
* You must be able to connect to the SSH server without typing a password.
* `ssh` will refuse to connect using a password if the private key is not passphrase-protected

Example:

```bash
$ ./2-ssh_configured
$ ssh -o StrictHostKeyChecking=no -i ~/.ssh/school ubuntu@8.8.8.8 hostname
ubuntu
$
```
In the example above, after executing the script, we can connect to the server using `ssh` without typing a password.

### Task 3: Let me in! - [3-ssh_authorized_key](./3-ssh_authorized_key)

Write a Bash script that adds the SSH public key from Task #1 to your server:

* You will need to add the public key to the `~/.ssh/authorized_keys` file for the user ubuntu on your server.
* Make sure `authorized_keys` has the correct permissions: `600`.

Example:

```bash
$ ./3-ssh_authorized_key
$
```

In the example above, after executing the script, the SSH public key from Task #1 is added to the `authorized_keys` file on the server.

### Task 4: Client configuration (w/ Puppet) - [4-puppet_ssh_config.pp](./4-puppet_ssh_config.pp)

Puppet is installed on the server, so create a Puppet manifest that configures an Ubuntu server with the following requirements:

* Configures `localhost` as the only authorized SSH key.
* Configures the SSH client configuration file to use the private key `~/.ssh/school`.
* SSH client configuration must be configured to refuse to authenticate using password.

Example:

```bash
$ sudo puppet apply 4-puppet_ssh_config.pp
$ ssh -o StrictHostKeyChecking=no localhost hostname
localhost
$
```
In the example above, after applying the Puppet manifest, we can connect to `localhost` using `ssh` without typing a password.

