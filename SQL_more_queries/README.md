# SQL - More Queries

This project contains SQL scripts that demonstrate advanced MySQL queries, user management, and database permissions.

## Tasks

### 0. My privileges!
**File:** `0-privileges.sql`

Script that lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on the server.

### 1. Root user
**File:** `1-create_user.sql`

Script that creates the MySQL server user `user_0d_1` with all privileges.
- Password: `user_0d_1_pwd`
- Should not fail if the user already exists

### 2. Read user
**File:** `2-create_read_user.sql`

Script that creates the database `hbtn_0d_2` and the user `user_0d_2`.
- User should have only SELECT privilege on the database `hbtn_0d_2`
- Password: `user_0d_2_pwd`
- Should not fail if database or user already exists

### 3. Always a name
**File:** `3-force_name.sql`

Script that creates the table `force_name` with:
- `id` INT
- `name` VARCHAR(256) - can't be null
- Should not fail if the table already exists

### 4. ID can't be null
**File:** `4-never_empty.sql`

Script that creates the table `id_not_null` with:
- `id` INT with default value 1
- `name` VARCHAR(256)
- Should not fail if the table already exists

## Requirements
- All files are executed on MySQL 8.0
- All SQL queries have comments
- All files start with a comment describing the task
- All SQL keywords are in uppercase

## Usage
```bash
cat filename.sql | mysql -hlocalhost -uroot -p
```

## Author
Holberton School Project
