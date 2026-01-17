# Python - Object Relational Mapping

This project demonstrates how to connect Python with MySQL databases using two different approaches: MySQLdb and SQLAlchemy ORM.

## Description

This project covers the fundamentals of Object Relational Mapping (ORM) in Python, bridging the gap between object-oriented programming and relational databases.

## Tasks

### MySQLdb Tasks (0-5)
- **0-select_states.py**: Lists all states from the database
- **1-filter_states.py**: Lists all states with names starting with 'N'
- **2-my_filter_states.py**: Displays states matching user input (vulnerable to SQL injection)
- **3-my_safe_filter_states.py**: Safe version using parameterized queries
- **4-cities_by_state.py**: Lists all cities with their states
- **5-filter_cities.py**: Lists all cities of a specific state

### SQLAlchemy Tasks (6-14)
- **model_state.py**: Defines the State class using SQLAlchemy
- **7-model_state_fetch_all.py**: Lists all State objects
- **8-model_state_fetch_first.py**: Prints the first State object
- **9-model_state_filter_a.py**: Lists states containing the letter 'a'
- **10-model_state_my_get.py**: Prints a specific state by name
- **11-model_state_insert.py**: Adds a new State object
- **12-model_state_update_id_2.py**: Updates a State object
- **13-model_state_delete_a.py**: Deletes states containing 'a'
- **model_city.py**: Defines the City class with foreign key to State
- **14-model_city_fetch_by_state.py**: Lists all cities with their states

## Requirements

- Python 3.x
- MySQLdb (mysqlclient)
- SQLAlchemy
- MySQL Server

## Installation

```bash
# Install MySQLdb
brew install mysql
pip3 install mysqlclient

# Install SQLAlchemy
pip3 install SQLAlchemy
```

## Usage

```bash
# MySQLdb example
./0-select_states.py root root hbtn_0e_0_usa

# SQLAlchemy example
./7-model_state_fetch_all.py root root hbtn_0e_6_usa
```

## Learning Objectives

- Connect to a MySQL database from Python
- Execute SQL queries using MySQLdb
- Understand SQL injection and how to prevent it
- Map Python classes to MySQL tables using ORM
- Create, read, update, and delete records using SQLAlchemy
- Work with foreign keys and relationships

## Author

Holberton School Project
