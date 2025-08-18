import re
from functools import reduce

class ManagePrompts:
    """Stores prompts and offers utility methods for processing prompts."""

    banned_words = ["like", "and"]
    """Words that are disallowed in prompts. These are fixed."""

    def __init__(self, prompts):
        """The prompts to store."""
        self.prompts = prompts

    @staticmethod
    def _filter_prompts(prompts: list[str], banned_words: list[str]) -> list[str]:
        """
        Removes banned words from prompts and replaces with * sequence of the same length of the replaced words,
        e.g. "It's not mine." becomes "It's *** mine." when "not" is a banned word.
        This method is static for testing. Use :meth:`self.filter_prompts` instead on prompts in the class`

        :param prompts: The prompts to be filtered
        :param banned_words: The words to be replaced with ****'s
        :returns: a list of filtered prompts
        """
        return list(map(lambda prompt:
                        reduce(lambda prompt, banned_word:
                               re.sub(re.compile("\\b"+re.escape(banned_word)+"\\b", flags=re.IGNORECASE),
                                      "*"*len(banned_word), prompt), banned_words, prompt), prompts))

    def filter_prompts(self) -> list[str]:
        """
        Removes the banned words in this class from prompts stored and replaces with * sequence of the
        same length of the replaced words,
        e.g. "It's not mine." becomes "It's *** mine." when "not" is a banned word.
        """
        return self._filter_prompts(self.prompts, self.banned_words)
