import pytest
from pipeline import normalize_signal

def test_basic_normalization():
    data = [1, 2, 3]
    result = normalize_signal(data)
    assert round(sum(result), 6) == 0 # mean should be zero

def test_empty_input():
    with pytest.raises(ValueError):
        normalize_signal([])

def test_output_length():
    data = [5, 5, 5]
    result = normalize_signal(data)
    assert len(result) == len(data)

def test_intentional_failure():
    data = [1, 2, 3]
    result = normalize_signal(data)
    assert result == [0, 0, 0]  # This will FAIL intentionally

import time

def test_performance():
    data = list(range(1000000)) # large dataset
    start = time.time()

    normalize_signal(data)

    duration = time.time() - start
    assert duration < 1.0 # should run under 1 second