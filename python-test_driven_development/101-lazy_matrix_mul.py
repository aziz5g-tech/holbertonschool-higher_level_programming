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
    A = np.array(m_a)
    B = np.array(m_b)
    
    if A.ndim != 2 or B.ndim != 2:
        raise TypeError("Scalar operands are not allowed, use '*' instead")

    a_rows, a_cols = A.shape
    b_rows, b_cols = B.shape

    if a_cols != b_rows:
        raise ValueError(
            "shapes ({},{}) and ({},{}) not aligned: {} (dim 1) != {} (dim 0)"
            .format(a_rows, a_cols, b_rows, b_cols, a_cols, b_rows)
        )

    # الآن استخدم matmul بأمان
    return np.matmul(A, B)
    
