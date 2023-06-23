# Configuration Management Project

This project focuses on configuration management using Puppet, along with other related topics such as DevOps, SysAdmin, Scripting, and CI/CD. The goal is to familiarize yourself with Puppet's syntax and best practices while completing a set of tasks.

## Teble of Contents
1. [Project Details](#Project-Details)
2. [Background Context](#Background-Context)
3. [Resources](#Resources)
4. [Requirements](#Requirements)
5. [Versioning and Installation](#Versioning-and-Installation)
6. [Tasks](#Tasks)
7. [Repository Information](#Repository-Information)

## Project Details

- Author: Sylvain Kalache
- Weight: 1
- Project Start: Jun 23, 2023 6:00 AM
- Project End: Jun 24, 2023 6:00 AM
- Checker Release: Jun 23, 2023 12:00 PM
- Auto Review: Will be launched at the project deadline

## Background Context

The project's background context is based on the experience of the author when working on an auto-remediation tool called Skynet at SlideShare. The tool involved managing, scaling, and fixing cloud infrastructure using a parallel job-execution system called MCollective. However, a bug in the code caused unintended consequences by shutting down a significant portion of SlideShare's infrastructure. The incident highlights the importance of configuration management and the role Puppet played in quickly restoring the infrastructure to normal operation.

## Resources

To complete the project, make use of the following resources:

- [Intro to Configuration Management](https://www.digitalocean.com/community/tutorials/an-introduction-to-configuration-management)
- [Puppet resource type: file](https://www.puppet.com/docs/puppet/5.5/types/file.html)
- [Puppet's Declarative Language: Modeling Instead of Scripting](https://www.puppet.com/docs/puppet/5.5/types/file.html)
- [Puppet lint](https://www.puppet.com/blog)
- [Puppet emacs mode](http://puppet-lint.com/)

## Requirements

General requirements for the project are as follows:

- The project assumes an Ubuntu 20.04 LTS environment.
- All files should end with a new line.
- A `README.md` file at the root of the project folder is mandatory.
- Puppet manifests must pass `puppet-lint` version

## Versioning and Installation

The project assumes a preinstalled Puppet 5.5 on your Ubuntu 20.04 VM. If it's not already installed, follow the instructions below:

```bash
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet
```
You do not need to attempt to upgrade versions, as this project focuses on the basic level syntax, which is virtually identical in newer versions of Puppet.

To install `puppet-lint`, use the following command:

```bash
$ gem install puppet-lint
```
## Tasks
#### Task 0: Create a File
Using Puppet, install `flask` from `pip3` with specific requirements.

Requirements:

* Install `flask` package.
* Version must be `2.1.0`

Refer to the Puppet manifest file `1-install_a_package.pp` in the repository for an example.
#### Task 2: Execute a Command
Using Puppet, create a manifest that kills a process named `killmenow`.

Requirements:

* Use the exec Puppet resource.
* Use `pkill` command to kill the process.

Refer to the Puppet manifest file `2-execute_a_command.pp` in the repository for an example.

## Repository Information
The project repository can be accessed at the following location:
* GitHub Repository: [alx-system_engineering-devops](/.alx-system_engineering-devops)
* Directory: [0x0A-configuration_management](./0x0A-configuration_management)
Feel free to explore the repository for additional details and files related to the project.

For any further assistance or questions, please reach out to the project author, Sylvain Kalache.
