import unittest
from python_code_practice.ManagePrompts import ManagePrompts

class ManagePromptsTest(unittest.TestCase):
    def test_single_word_appears_once(self):
        prompts = ["I love unit tests."]
        banned_words = ["love"]
        filtered_prompts = ManagePrompts._filter_prompts(prompts, banned_words)
        expected_prompts = ["I **** unit tests."]
        self.assertListEqual(filtered_prompts, expected_prompts, "Banned word filtering is not returning the expected result with a single word and prompt.")

    def test_two_prompts(self):
        prompts = ["I love unit tests.", "Really, why?"]
        banned_words = ["unit", "why"]
        filtered_prompts = ManagePrompts._filter_prompts(prompts, banned_words)
        expected_prompts = ["I love **** tests.", "Really, ***?"]
        self.assertListEqual(filtered_prompts, expected_prompts, "Banned word filtering is not returning the expected result with two prompts.")

    def test_single_word_appears_twice(self):
        prompts = ["I love that they help prevent regressions, and I love that describe behaviour."]
        banned_words = ["love"]
        filtered_prompts = ManagePrompts._filter_prompts(prompts, banned_words)
        expected_prompts = ["I **** that they help prevent regressions, and I **** that describe behaviour."]
        self.assertListEqual(filtered_prompts, expected_prompts, "Banned word filtering is not returning the expected result with the same banned word appearing twice.")

    def test_capital_letter_in_prompt(self):
        prompts = ["Really, why?"]
        banned_words = ["really"]
        filtered_prompts = ManagePrompts._filter_prompts(prompts, banned_words)
        expected_prompts = ["******, why?"]
        self.assertListEqual(filtered_prompts, expected_prompts, "Banned word filtering is not returning the expected result regarding case.")

    def test_multiple_banned_words(self):
        prompts = ["I love that they help prevent regressions, and I love that describe behaviour."]
        banned_words = ["love", "i", "that"]
        filtered_prompts = ManagePrompts._filter_prompts(prompts, banned_words)
        expected_prompts = ["* **** **** they help prevent regressions, and * **** **** describe behaviour."]
        self.assertListEqual(filtered_prompts, expected_prompts, "Banned word filtering is not returning the expected result with multiple banned words.")

    def test_banned_word_is_substring(self):
        prompts = ["Unit tests in python and java are alike."]
        banned_words = ["like"]
        filtered_prompts = ManagePrompts._filter_prompts(prompts, banned_words)
        expected_prompts = ["Unit tests in python and java are alike."]
        self.assertListEqual(filtered_prompts, expected_prompts, "Banned words that are substrings of string in the prompt are being replaced.")

if __name__ == '__main__':
    unittest.main()
