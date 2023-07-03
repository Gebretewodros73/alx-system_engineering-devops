# Shell Basics

This directory contains a collection of shell scripts for basic shell operations and commands. Each script focuses on a specific task and provides examples of how to use the commands effectively.

## List of Tables

1. [Learnig Objective](#Learnig-Objective)
2. [List of Scripts](#List-of-Scripts)
3. [Usage](#Usage)
4. [Repository](#Repository)

## List of Scripts

1. [0-current_working_directory](./0-current_working_directory): Prints the absolute path name of the current working directory.
2. [1-listit](./1-listit): Displays the contents list of the current directory.
3. [2-bring_me_home](./2-bring_me_home): Changes the working directory to the user's home directory.
4. [3-listfiles](./3-listfiles) : Displays the current directory contents in a long format.
5. [4-listmorefiles](./4-listmorefiles): Displays the current directory contents, including hidden files, in a long format.
6. [5-listfilesdigitonly](./5-listfilesdigitonly): Displays the current directory contents in a long format with user and group IDs displayed numerically, including hidden files.
7. [6-firstdirectory](./6-firstdirectory): Creates a directory named `my_first_directory` in the `/tmp/` directory.
8. [7-movethatfile](./7-movethatfile) : Moves the file `betty` from `/tmp/` to `/tmp/my_first_directory`.
9. [8-firstdelete](./8-firstdelete): Deletes the file `betty` from `/tmp/my_first_directory`.
10. [9-firstdirdeletion](./9-firstdirdeletion): Deletes the directory `my_first_directory` from the `/tmp` directory.
11. [10-back](./10-back): Changes the working directory to the previous one.
12. [11-lists](./11-lists) : Lists all files in the current directory, the parent directory, and the `/boot` directory in long format.
13. [12-file_type](./12-file_type): Prints the type of the file named `iamafile` in the `/tmp` directory.
14. [13-symbolic_link](./13-symbolic_link): Creates a symbolic link to `/bin/ls` named `__ls__` in the current working directory.
15. [14-copy_html](./14-copy_html): Copies all HTML files from the current directory to the parent directory, if they don't exist or are newer.
16. [100-lets_move](./100-lets_move): Moves all files beginning with an uppercase letter to the `/tmp/u` directory.
17. [101-clean_emacs](./101-clean_emacs): Deletes all files in the current directory ending with the character `~`.
18. [102-tree](./102-tree): Creates the directories `welcome/`, `welcome/to/`, and `welcome/to/school` in the current directory.

Feel free to explore and use these scripts for your shell operations and learning.

## Usage

To use any script, simply navigate to the directory containing the script and execute it using the command line.

Example:
```bash
$ ./0-current_working_directory
/root/alx-system_engineering-devops/0x00-shell_basics
```

All files are given executable permissions to the script using the `chmod` command.

## Repository

You can find the repository for these scripts on GitHub:

GitHub repository: [alx-system_engineering-devops](https://github.com/gebretewodros73/alx-system_engineering-devops)



