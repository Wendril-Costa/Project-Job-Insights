import pytest
from src.pre_built.counter import count_ocurrences
from unittest.mock import mock_open, patch


@pytest.fixture
def fixture():
    return """JavaScript JavaScript
    Python Python Python C++ C C# C++ python javascript"""


def test_counter(fixture):
    assert count_ocurrences("data/jobs.csv", "javascript") == 122

    assert count_ocurrences("data/jobs.csv", "python") == 1639

    with patch("builtins.open", mock_open(read_data=fixture)):
        assert count_ocurrences("data/jobs.csv", "JAVASCRIPT") == 3
