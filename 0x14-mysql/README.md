# MySQL Configuration and Backup

This repository contains scripts and configurations for setting up a MySQL database, configuring replication between a primary and replica server, and performing backups.

## Installation

Before getting started, make sure you have MySQL installed on both your `web-01` and `web-02` servers. The MySQL distribution version should be `5.7.x`. You can verify the installation by running the following command:

```bash
mysql --version
```
## Configuration Steps

Follow the steps below to set up the MySQL configuration, replication, and backup:

0. Create MySQL Users
Create a MySQL user named `holberton_user` on both `web-01` and `web-02` servers. Use the following command:

```bash
mysql -uroot -p -e "CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';"
```
Grant permissions to `holberton_user` to check the primary/replica status of the databases:

```bash
mysql -uroot -p -e "GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';"
```
1. Create a Database and Table

On the primary server `(web-01)`, create a database named `tyrell_corp` and a table named `nexus6`. Add at least one entry to the `nexus6` table.

Grant `SELECT` permissions on the table to `holberton_user`:

```bash
mysql -uholberton_user -p -e "USE tyrell_corp; SELECT * FROM nexus6;"
```
2. Create a Replica User

On the primary server `(web-01)`, create a replica user named `replica_user` with the host set to `%` (allowing connections from any host). Assign appropriate replication permissions to the user:

```bash
mysql -uroot -p -e "CREATE USER 'replica_user'@'%' IDENTIFIED BY '<replica_user_password>';"
mysql -uroot -p -e "GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';"
```
3. Setup Primary-Replica Infrastructure

On the primary server `(web-01)`, comment out the `bind-address` parameter in the MySQL configuration file. The configuration file can be found at `/etc/mysql/mysql.conf.d/mysqld.cnf` or `/etc/mysql/my.cnf`.

On the replica server `(web-02)`, update the MySQL configuration file `/etc/mysql/mysql.conf.d/mysqld.cnf` or `/etc/mysql/my.cnf` with the appropriate replica configuration.

Create the configuration files for the primary and replica servers:

4. MySQL Backup

To perform a MySQL backup, use the provided Bash script 5-mysql_backup. The script generates a MySQL dump, compresses it into a tar.gz archive, and stores it in a different data center.

Usage
```bash
./5-mysql_backup <password>:
```
The script will create a MySQL dump file named `backup.sql` and a compressed archive file named `day-month-year.tar.gz`.

Please note that the script assumes the MySQL root user for database connection.

## Directory Structure

The directory has the following structure:

├── 0x14-mysql
│   ├── 4-mysql_configuration_primary
│   ├── 4-mysql_configuration_replica
│   └── 5-mysql_backup
└── README.md

* The 0x14-mysql directory contains the scripts and configurations for MySQL setup, replication, and backup.
* The [4-mysql_configuration_primary](./4-mysql_configuration_primary) file is the primary server configuration.
* The [4-mysql_configuration_replica](./4-mysql_configuration_replica) file is the replica server configuration.
* The [5-mysql_backup](./5-mysql_backup) file is the Bash script for performing MySQL backup.
* The [README.md](./README.md) file contains instructions and information about the repository.
