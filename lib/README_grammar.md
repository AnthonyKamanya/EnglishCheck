# GrammarPercent 26 05 2024

User story
estimate of reading time for a text

_write the user story here. add any clarifying notes you might have_

>As a user 
>so i check my grammar
>I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.
>I want to know the percentage checked so far

# 2. Designing the class signature

_include the name of the class, its functions, parameters, return value and side effects._

```python

class GrammarStats:
    def __init__(self):
        pass
  
    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        pass
  
    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        pass
```

# 3. Create Examples as test

_Make a list of examples of what the method will take and return._
```python

"""
Given a string with one word starts with a capital letter with punctuation mark
it should return True
"""
check("Blessing!") => True

"""
Given a string with more than one word starting with a capital letter with punctuation mark
it should return True
"""
check("Blessing from God!") => True


"""
Given a string with one word starts with a small letter with punctuation mark
it should return False
"""
check("blessing!") => False

"""
Given a string with more than one word starting with a small letter with punctuation mark
it should return False
"""
check("blessing from God!") => False

"""
Given a string with one word starts with a capital letter without an punctuation mark
it should return False
"""
check("Blessing") => False


"""
Given a string with one word starts with a small letter without an punctuation mark
it should return False
"""
check("blessing") => False
"""
Given a string with one word starting with an punctuation mark
it should return False
"""
check("?blessing") => False

"""
Given a string with only an punctuation mark
it should return False
"""
check("!") => False

"""
Given an empty string
it should raise and error
"""
check("") => text cannot be empty!

"""
Given a string 
#percentage_good return the number of text that returned True in check

```

# 4 implement the behaviour

_After each test you write, follow the test- driving process of red, green, refactor to implent the bahviour._