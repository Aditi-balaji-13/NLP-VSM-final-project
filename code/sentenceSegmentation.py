from util import split

# Add your import statements here
import nltk
nltk.download('punkt')


class SentenceSegmentation():

	def naive(self, text):
		"""
		Sentence Segmentation using a Naive Approach

		Parameters
		----------
		arg1 : str
			A string (a bunch of sentences)

		Returns
		-------
		list
			A list of strings where each string is a single sentence
		"""

		segmentedText = []

		#Fill in code here
		segmentedText=split(text,('.','!','?'))
		

		return segmentedText





	def punkt(self, text):
		"""
		Sentence Segmentation using the Punkt Tokenizer

		Parameters
		----------
		arg1 : str
			A string (a bunch of sentences)

		Returns
		-------
		list
			A list of strings where each strin is a single sentence
		"""
		tokenizer = nltk.tokenize.punkt.PunktSentenceTokenizer()
		segmentedText = tokenizer.tokenize(text)

		#Fill in code here
		
		return segmentedText
