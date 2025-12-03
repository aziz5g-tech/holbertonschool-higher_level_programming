#!/usr/bin/python3
# 101-lazy_matrix_mul.py
# ABDULAZIZ ALRSHEDI <11937@holbertonschool.com>
"""Defines a matrix multiplication function using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    """

    try:
        return np.matmul(m_a, m_b)
    except ValueError as e:
        raise ValueError(str(e))
    except TypeError:
        raise TypeError("Scalar operands are not allowed, use '*' instead")
