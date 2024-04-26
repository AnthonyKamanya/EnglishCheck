from lib.grammar import GrammarStats
import pytest

"""
Given a string with one word starts with a capital letter with punctuation mark
it should return True
"""
def test_one_word_starts_with_capital_and_punctuation_at_the_end():
    grammar = GrammarStats()
    results = grammar.check("Blessing!")
    assert results == True

"""
Given a string with more than one word starting with a capital letter with punctuation mark
it should return True
"""
def test_a_string_starts_with_capital_and_punctuation_at_the_end():
    grammar = GrammarStats()
    results = grammar.check("Blessing from God!")
    assert results == True

"""
Given a string with one word starts with a small letter with punctuation mark
it should return False
"""
def test_one_word_starts_with_small_letter_and_punctuation_at_the_end():
    grammar = GrammarStats()
    results = grammar.check("blessing!")
    assert results == False

"""
Given a string with more than one word starting with a small letter with punctuation mark
it should return False
"""
def test_string_more_words_starts_with_small_letter_and_punctuation_at_the_end():
    grammar = GrammarStats()
    results = grammar.check("blessing from God!")
    assert results == False


# """
# Given a string with one word starts with a capital letter without an punctuation mark
# it should return False
# """
def test_one_word_starts_with_capital_and_without_punctuation_at_the_end():
    grammar = GrammarStats()
    results = grammar.check("Blessing")
    assert results == False

# """
# Given a string with one word starts with a small letter without an punctuation mark
# it should return False
# """

def test_one_word_starts_with_small_letter_without_a_punctuation_at_the_end():
    grammar = GrammarStats()
    results = grammar.check("blessing")
    assert results == False


"""
Given a string with one word starting with an punctuation mark
it should return False
"""
def test_one_word_starts_with_small_letter_and_a_punctuation_at_the_beginning():
    grammar = GrammarStats()
    results = grammar.check("!blessing")
    assert results == False

"""
Given a string with only an punctuation mark
it should return False
"""
def test_string_only_a_punctuation():
    grammar = GrammarStats()
    results = grammar.check("!")
    assert results == False


"""
Given an empty string
it should raise and error
"""
def test_an_empty_string_():
    grammar = GrammarStats()
    with pytest.raises(Exception) as err:
        grammar.check("")
    error_message = str(err.value)
    assert error_message == "text cannot be empty!"
 

"""
Given a string 
#percentage_good return the number of text that returned True in check
"""
def test_number_checked_true():
    grammar = GrammarStats()
    grammar.check("Hi What is your name?")
    grammar.check("Hi What is your name")
    grammar.check("hi What is your name?")
    grammar.check("Hi What is your name!")
    grammar.check("hi What is your ?name")
    results = grammar.percentage_good()
    assert results == 40
