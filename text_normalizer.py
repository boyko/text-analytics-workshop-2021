# https://gist.github.com/lvngd/3695aac64461de2cfb9d50bb11d5fbb3

import re
import string
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

# from pycontractions import Contractions
# from word2number import w2n

"""
Text Normalization for NLP
	-removes extra whitespace within text
	-converts unicode to ascii
	-converts to lowercase
	-remove leading or trailing whitespace
	-expands contractions
	-tokenizes sentences and words
	-removes punctuation
	-lemmatizes words
	-removes stopwords
"""


class TextNormalizer:
    def __init__(self):
        # self.cont = Contractions(kv_model=api.load("glove-twitter-25"))
        self.lemmatizer = WordNetLemmatizer()
        self.punctuation_table = str.maketrans('', '', string.punctuation)
        self.stop_words = set(stopwords.words('english'))

    def normalize_text(self, text):
        normalized_sentences = []
        text = re.sub(r'\s+', ' ', text)
        # text = unidecode.unidecode(text)
        text = text.lower()
        # expanded_contractions = list(self.cont.expand_texts([text], precise=True))
        # if expanded_contractions:
        #     text = expanded_contractions[0]
        sentences = sent_tokenize(text)
        for sentence in sentences:
            # remove punctuation
            sentence = sentence.translate(self.punctuation_table)
            # strip leading/trailing whitespace
            sentence = sentence.strip()
            words = word_tokenize(sentence)
            # lemmatize and remove stopwords
            filtered = [self.lemmatizer.lemmatize(word) for word in words if word not in self.stop_words]
            new_sentence = ' '.join(filtered)
            normalized_sentences.append(new_sentence)
        return normalized_sentences
