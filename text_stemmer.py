import os
import re
import sys
import collections
import glob
import nltk, re, pprint

class ScoreText(object):
    def __init__(self, stemmer, words_list):
        self._stemmer = stemmer
        wordsdic = {}
        for (k,score) in words_list.items():
            wordsdic.update({self._stem(k):score})
        self._wordsdic = wordsdic
    def _stem(self, word):
        return self._stemmer.stem(word).lower()
    def _score(self,tokens):
        score = 0
        score_g = 0
        score_b = 0
        good_words = []
        bad_words = []
        for word in tokens:
            if self._stem(word) in self._wordsdic:
                value = self._wordsdic[self._stem(word)]
                score += value
                if value >0:
                    good_words.append(word)
                    score_g += value
                else:
                    bad_words.append(word)
                    score_b -= value
        return (good_words,bad_words,score, score_g, score_b)
