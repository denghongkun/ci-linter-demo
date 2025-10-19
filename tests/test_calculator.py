"""Test cases for calculator module."""
import pytest
from calculator import add, subtract, multiply


def test_add_positive_numbers():
    """测试正数相加"""
    assert add(2, 3) == 5
    assert add(10, 15) == 25


def test_add_negative_numbers():
    """测试负数相加"""
    assert add(-2, -3) == -5
    assert add(-10, 5) == -5


def test_add_zero():
    """测试零值情况"""
    assert add(0, 0) == 0
    assert add(5, 0) == 5
    assert add(0, -3) == -3


def test_add_float_numbers():
    """测试浮点数相加"""
    assert add(1.5, 2.5) == 4.0
    assert add(-1.1, 1.1) == pytest.approx(0.0)


def test_add_large_numbers():
    """测试大数相加"""
    assert add(1000000, 2000000) == 3000000


def test_subtract_positive_numbers():
    """测试正数相减"""
    assert subtract(5, 3) == 2
    assert subtract(10, 5) == 5


def test_subtract_negative_numbers():
    """测试负数相减"""
    assert subtract(5, -3) == 8
    assert subtract(-5, -3) == -2


def test_subtract_zero():
    """测试零值情况"""
    assert subtract(5, 0) == 5
    assert subtract(0, 5) == -5


def test_multiply_positive_numbers():
    """测试正数相乘"""
    assert multiply(2, 3) == 6
    assert multiply(5, 4) == 20


def test_multiply_negative_numbers():
    """测试负数相乘"""
    assert multiply(-2, 3) == -6
    assert multiply(-2, -3) == 6


def test_multiply_zero():
    """测试零值相乘"""
    assert multiply(5, 0) == 0
    assert multiply(0, 10) == 0
