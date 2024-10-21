"""
main_test.py



Author: Zack Hankin

Started: 27/02/2023
"""

from clock_ui.main import main


def test_main_returns_zero():
    assert main() == 0
