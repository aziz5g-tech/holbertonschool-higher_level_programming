# Python - Everything is Object

This project explores how Python handles different types of objects, focusing on the concepts of mutability, immutability, references, and aliases.

## Learning Objectives

- Understanding what an object is in Python
- Difference between a class and an object/instance
- Difference between immutable and mutable objects
- Understanding references, assignments, and aliases
- How to check if two variables are identical or linked to the same object
- Variable identifiers and memory addresses
- Built-in mutable and immutable types
- How Python passes variables to functions

## Key Concepts

### Immutable vs Mutable

**Immutable objects** (cannot be modified after creation):
- int, float, bool
- str
- tuple
- frozenset

**Mutable objects** (can be modified after creation):
- list
- dict
- set

### Example

```python
# Immutable behavior
a = 1
b = a
a = 2
print(b)  # Output: 1

# Mutable behavior
l = [1, 2, 3]
m = l
l[0] = 'x'
print(m)  # Output: ['x', 2, 3]