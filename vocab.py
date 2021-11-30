import config
from dataset import *
from collections import Counter
import numpy as np
class Vocab:
    PAD = 0
    SOS = 1
    EOS = 2
    UNK = 3
    def __init__(self,):
        self.word2index = {}
        self.word2count = Counter()
        self.reserved = ['<PAD>', '<SOS>', '<EOS>', '<UNK>']
        self.index2word = self.reserved[:]
        self.embeddings = None
        self.data = Dataset.read_data(config.path)
        self.longth = 4
    def add_words(self,sentence):
        """
        :param sentence:
        added word
        """
        for word in sentence:
            if word not in self.index2word:
                self.index2word[word] = self.longth
                self.longth+=1
        self.word2count.update(word)
    def do_cut(self,string,cut):
        """
        :param string: sentence
        :return: cuted sentence item
        """
        if cut=="split":
            return [string.split(" ")]

if __name__=="__main__":
    print(config.path)