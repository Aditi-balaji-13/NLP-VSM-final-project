from util import *
import pandas as pd
import numpy as np
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import gensim.downloader as api
class InformationRetrieval():

	def __init__(self):
		self.index = None
		self.doc_num = None

	def buildIndex(self, docs, docIDs):
		"""
		Builds the document index in terms of the document
		IDs and stores it in the 'index' class variable

		Parameters
		----------
		arg1 : list
			A list of lists of lists where each sub-list is
			a document and each sub-sub-list is a sentence of the document
		arg2 : list
			A list of integers denoting IDs of the documents
		Returns
		-------
		None
		"""
		self.docs=[]
		self.docIDs = docIDs
		self.doc_num = len(docIDs)
		for doc in docs:
			d=''
			for sentence in doc:
				sent=' '.join(sentence)
				d+=sent
			self.docs.append(d)
		#Fill in code here
		tfidf=TfidfVectorizer()
		tfidfv=tfidf.fit_transform(self.docs).toarray()
		words_set = tfidf.get_feature_names_out()
		vocabulary=tfidf.vocabulary_
		self.ws=words_set
		w2v_model = api.load('word2vec-google-news-300')
		self.model=w2v_model
		embedding_matrix = np.zeros((len(vocabulary), w2v_model.vector_size))
		for word, index in vocabulary.items():
			if word in w2v_model.vocab:
				embedding_matrix[index] = w2v_model[word]
		modified_tfidf_matrix = self.tfidfv.dot(embedding_matrix)
		modified_tfidf=pd.Dataframe(modified_tfidf_matrix,columns=self.ws)
		self.tfidfv=modified_tfifdf
	def rank(self, queries):
	    doc_IDs_ordered = []
	
	    for query in queries:
	        query1=''
	        for sentence in query:
	            sent=' '.join(sentence)
	            query1+=sent
	        tfidf=TfidfVectorizer()
	        tfidfq=tfidf.fit_transform([query1]).toarray()
	        c=tfidf.get_feature_names_out()
	        vocabulary=tfidf.vocabulary_
	        embedding_matrix = np.zeros((len(vocabulary), w2v_model.vector_size))
	        for word, index in vocabulary.items():
	            if word in self.w2v_model.vocab:
	                embedding_matrix[index] = w2v_model[word]
	        mtfifdfq=tfidfq.dot(embedding_matrix)
	        fe=list(set(self.ws)&set(c))
	        cosine=linear_kernel(self.tfidfv[fe],mtfidfq[fe])
	        cosine=pd.DataFrame(cosine)
	        cols=cosine.columns[0]
	        cosine['DocIDs']=self.docIDs
	        doc_IDs_ordered.append(cosine.sort_values(cols,ascending=False)['DocIDs'])
	
	       
	
	    return doc_IDs_ordered
