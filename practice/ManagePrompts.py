import re
from functools import reduce

class ManagePrompts:

    banned_words = ["like", "and"]

    def __init__(self, prompts):
        self.prompts = prompts

    @staticmethod
    def filter_prompts(prompts, banned_words):
        return list(map(lambda prompt:
                        reduce(lambda prompt, banned_word:
                               re.sub(re.compile("\\b"+re.escape(banned_word)+"\\b", flags=re.IGNORECASE),
                                      "*"*len(banned_word), prompt), banned_words, prompt), prompts))
