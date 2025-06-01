import pytest
from scripts.word_freq import count_word_frequencies, sort_frequencies

def test_count_word_frequencies_simple():
    text = "Hello hello world"
    expected {"hello": 2, "world": 1}
    assert count_word_frequencies(text) == excepted
    
def test_count_word_frequencies_empty():
    assert count_word_frequencies("") == {}
    
def test_sort_frequencies_tie_break():
    freq = {"apple": 2, "banana": 2, "cherry": 1}
    sorted_list = sort_frequencies(freq)
    
    assert sorted_list[0] == ("apple", 2)
    assert sorted_list[1] == ("banana", 2)
    assert sorted_list[2] == ("cherry", 1)