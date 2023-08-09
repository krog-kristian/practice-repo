import addition
import pytest

def test_add():
  assert addition.add(5, 3) == 8

def test_sub():
  assert addition.sub(7, 4) == 3