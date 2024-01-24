from util import *

# Add your import statements here
import re
from nltk.tokenize import TreebankWordTokenizer


class Tokenization():

    def naive(self, text):
        """
        Tokenization using a Naive Approach

        Parameters
        ----------
        text : list
            A list of strings where each string is a single sentence

        Returns
        -------
        list
            A list of lists where each sub-list is a sequence of tokens
        """

        tokenizedText = None
        self.n = len(text)
        for i in range(self.n):
            temp = text[i]
            token = re.findall(r'\w+|[^\w\s]', temp)
            text[i] = token
        tokenizedText = text

        return tokenizedText


    def pennTreeBank(self, text):
        """
        Tokenization using the Penn Tree Bank Tokenizer

        Parameters
        ----------
        text : list
            A list of strings where each string is a single sentence

        Returns
        -------
        list
            A list of lists where each sub-list is a sequence of tokens
        """

        tokenizedText = []
        for sentence in text:
            tokens = TreebankWordTokenizer().tokenize(sentence)
            tokenizedText.append(tokens)

        return tokenizedText
