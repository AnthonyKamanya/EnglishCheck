import string

class GrammarStats:
    def __init__(self):

        self.num_of_checked_text = 0
        self.count_checked_text = 0

    def check(self, text):
        self.count_checked_text += 1
        if text == "":
            raise Exception("text cannot be empty!")
        elif text[0].isupper() and text[-1] in string.punctuation:
            self.num_of_checked_text += 1
            return True
        return False
    
    def percentage_good(self):
        percentage = self.num_of_checked_text /self.count_checked_text
        return percentage * 100