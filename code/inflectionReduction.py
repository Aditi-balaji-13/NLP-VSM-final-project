from util import *

# Add your import statements here
import nltk
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer

class InflectionReduction:

    def reduce(self, text):
        """
        Stemming/Lemmatization
        Note: This code implements Lemmatization as it is identified 
        to be a better fit for the given dataset

        Parameters
        ----------
        arg1 : list
            A list of lists where each sub-list a sequence of tokens
            representing a sentence

        Returns
        -------
        list
            A list of lists where each sub-list is a sequence of
            stemmed/lemmatized tokens representing a sentence
        """

        reducedText = []
        lemmatizer = WordNetLemmatizer()
        for sentence in text:
            temp = [lemmatizer.lemmatize(word) for word in sentence]
            reducedText.append(temp)
        
        return reducedText
