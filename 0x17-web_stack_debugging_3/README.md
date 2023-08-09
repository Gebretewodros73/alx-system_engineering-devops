# Web Stack Debugging 3 - Project Tasks

This directory contains solutions and code files for the Web Stack Debugging 3 project tasks. Each task focuses on debugging and resolving issues related to a web stack setup, and in some cases, automating the resolution using Puppet.

## Task 0: Strace is your friend

**Task Description:** Using strace, find out why Apache is returning a 500 error. Once you find the issue, fix it and then automate it using Puppet (instead of using Bash as you were previously doing).

**Hints:**
- strace can attach to a currently running process
- You can use tmux to run strace in one window and curl in another one

**Requirements:**
- Your `0-strace_is_your_friend.pp` file must contain Puppet code
- You can use whatever Puppet resource type you want for your fix

**Example:**
```bash
$ curl -sI 127.0.0.1
HTTP/1.0 500 Internal Server Error
Date: Fri, 24 Mar 2017 07:32:16 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Powered-By: PHP/5.5.9-1ubuntu4.21
Connection: close
Content-Type: text/html
```

```bash
$ puppet apply 0-strace_is_your_friend.pp
Notice: Compiled catalog for e514b399d69d.ec2.internal in environment production in 0.02 seconds
Notice: /Stage[main]/Main/Exec[fix-wordpress]/returns: executed successfully
Notice: Finished catalog run in 0.08 seconds
```

```bash
$ curl -sI 127.0.0.1:80
HTTP/1.1 200 OK
Date: Fri, 24 Mar 2017 07:11:52 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Powered-By: PHP/5.5.9-1ubuntu4.21
Link: http://127.0.0.1/?rest_route=/; rel="https://api.w.org/"
Content-Type: text/html; charset=UTF-8
```

```bash
$ curl -s 127.0.0.1:80 | grep Holberton
<title>Holberton &#8211; Just another WordPress site</title>
<link rel="alternate" type="application/rss+xml" title="Holberton &raquo; Feed" href="http://127.0.0.1/?feed=rss2" />
... (output truncated)
```

#### Repository Information:

* GitHub repository: [alx-system_engineering-devops](./https://github.com/gebretewodros73/alx-system_engineering-devops)
* Directory: 0x17-web_stack_debugging_3
* File: [0-strace_is_your_friend.pp](./File: 0-strace_is_your_friend.pp)
