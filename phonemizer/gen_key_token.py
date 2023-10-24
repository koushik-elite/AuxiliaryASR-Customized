from phonemizer import phonemize
from phonemizer.backend import EspeakBackend
from phonemizer.separator import Separator
import os
from os import listdir
from os.path import isfile, join
from os import walk
import pandas as pd
from tqdm import tqdm
import csv

word_dataframe = pd.read_csv("../Data-Sample/word_tamil_tokens.txt")
word_dataframe['index'] = word_dataframe.index

print(word_dataframe.head())
word_dataframe.to_csv("../Data-Sample/word_tamil_dict.txt", escapechar='\\', quoting=csv.QUOTE_NONNUMERIC, header=False, index=False)