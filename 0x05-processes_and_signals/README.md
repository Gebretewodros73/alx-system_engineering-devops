# Processes and signals
## Processes:
- A process is a program in execution. it is an instance of a program that is being excuted by the operating system.
- To start a process, the operating system allocates resources such as memory and CPU time to the process.
- Each process has its own address space, whick means it has its own memory area that it can access and modify.
- Processes can communicate with each other by using inter process communication(IPC) mechanisms such as pipes, sockets, or shared memory.
- Processes can be created by using system calls such as fork() or exec() in Unix-based systems or CreateProcess() in Windows.
## Signals:
- A signal is a software interrupt delivered to a process by the operating system. it is a notification that something has happened, such as the process receving a message or encountering an error.
- Signals can be sent to a process by using the kill() system call in Unix-based system or the TerminateProcess() function in Windows.
- Signals can be handled by the process using signal handler, which are functions that are executed when a signal is received.
- Some common signal include SIGINT, which is sent when the user presses Ctrl+C, and SIGTERM, which is sent when a process is asked to terminate.
- Signals can be used to control the behavior of a process such as terminating it gracefully or restarting it in case of a crash.
## Projects covered in repository
#### Bash script that displays its own PID.
#### Bash script that displays a list of currently running processes.
#### Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of Bash process.
#### Bash script that displays the PID, along with the process name, of processes whose name contain the word bash.
#### Bash script that displays to infinity and beyond indefinitely.
#### Bash script that stops infinity and beyond indefinitely using kill function and not. 
