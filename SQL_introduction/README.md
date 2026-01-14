# SQL Introduction

This directory contains SQL scripts that introduce fundamental MySQL database operations.

## Description

This project focuses on learning the basics of SQL and MySQL database management. The scripts demonstrate how to perform common database operations including creating, listing, and deleting databases.

## Requirements

- MySQL 8.0 (version 8.0.25)
- Ubuntu 20.04 LTS
- All files should end with a new line
- All SQL queries should have a comment just before
- All SQL keywords should be in uppercase (SELECT, WHERE, etc.)

## Files

| File | Description |
|------|-------------|
| `0-list_databases.sql` | Script that lists all databases of MySQL server |
| `1-create_database_if_missing.sql` | Script that creates the database `hbtn_0c_0` |
| `2-remove_database.sql` | Script that deletes the database `hbtn_0c_0` |

## Usage

To run any of these SQL scripts, use the following command:

```bash
cat <script_name>.sql | mysql -hlocalhost -uroot -p
```

Example:
```bash
cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
```

## Author

Holberton School Project
