import sys
import os

from fileio import *

def test_count_lines():
    assert count_lines('./test.txt') == 3

# def test_print_lines(capsys):
#     print_lines('./test.txt')
#     captured = capsys.readouterr()
#     assert captured.out == "Hello, World!\nThis is a test file.\nPython is fun!\n"