import pytest
from pipeline import normalize_signal

def test_basic_normalization():
    data = [1 , 2, 3]
    result = normalize_signal(data)
    assert round(sum(result), 6) == 0 # mean should be zero

def test_empty_input():
    with pytest.raises(ValueError):
        normalize_signal([])

def test_output_length():
    data = [5, 5, 5]
    result = normalize_signal(data)
    assert len(result) == len(data)