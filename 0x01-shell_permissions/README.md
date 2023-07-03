# 0x01-shell_permissions

This directory contains shell scripts for various tasks related to system engineering and DevOps. Each script performs a specific action and contributes to automating common tasks on a Unix-based system. The tasks are part of the ALX System Engineering & DevOps program.

## Task List

1. `My name is Betty`
* Description: Switch the current user to the user betty.
* Filename: [0-iam_betty](./0-iam_betty)
2. `Who am I`
* Description: Print the effective username of the current user.
* Filename: [1-who_am_i](./1-who_am_i)
3. `Groups`
* Description: Print all the groups the current user is a part of.
* Filename: [2-groups](./2-groups)
4. `New owner`
* Description: Change the owner of the file `hello` to the user `betty`.
* Filename: [3-new_owner](./3-new_owner)
5. `Empty!`
* Description: Create an empty file called `hello`.
* Filename: [4-empty](./4-empty)
6. `Execute`
* Description: Add execute permission to the owner of the file `hello`.
* Filename: [5-execute](./5-execute)
7. `Multiple permissions`
* Description: Add execute permission to the owner and group owner, and read permission to other users, to the file `hello`.
* Filename: [6-multiple_permissions](./6-multiple_permissions)
8. `James Bond`
* Description: Set the permissions for the file `hello` as follows:
    * Owner: no permission at all
    * Group: no permission at all
    * Other users: all the permissions
* Filename: [8-James_Bond](./8-James_Bond)
10. `John Doe`
* Description: Set the mode of the file `hello` to `-rwxr-x-wx`.
* Filename: [9-John_Doe](./9-John_Doe)
11. `Look in the mirror`
* Description: Set the mode of the file `hello` the same as the mode of `olleh`.
* Filename: [10-mirror_permissions](./10-mirror_permissions)
12. `Directories`
* Description: Add execute permission to all subdirectories of the current directory for the owner, the group owner, and all other users. Regular files should not be changed.
* Filename: [11-directories_permissions](./11-directories_permissions)
13. `More directories`
* Description: Create a directory called `my_dir` with permissions 751 in the working directory.
* Filename: [12-directory_permissions](./12-directory_permissions)
14. `Change group`
* Description: Change the group owner of the file `hello` to `school`.* Filename: [13-change_group](./13-change_group)

