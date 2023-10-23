from phonemizer import phonemize
from phonemizer.backend import EspeakBackend
from phonemizer.separator import Separator
import os
from os import listdir
from os.path import isfile, join
from os import walk
import pandas as pd
from tqdm import tqdm

mypath = "/mnt/d/mile_tamil_asr_corpus/mile_tamil_asr_corpus/train"
trans_files = mypath + "/trans_files"
audio_files = mypath + "/audio_files"

f = []
backend = EspeakBackend('ta')
separator_dict = Separator(phone=' ', word=None)
word_dataframe = pd.DataFrame([], columns=["token"])
n = 10
for (dirpath, dirnames, filenames) in walk(trans_files):
    for file in tqdm(filenames):
        if n < 0:
            break

        file_name, extension = os.path.splitext(file)
        # print(file_name)
        # print(dirpath)
        readline = ""
        with open(dirpath + "/" + file) as fp:
            for line in fp:
                readline = line
        # print(readline)
        dict_phonemize = backend.phonemize([readline], separator=separator_dict, strip=True)[0]
        if "'" in dict_phonemize:
            dict_phonemize.remove("'")
        
        # print(dict_phonemize.split(" "))
        # print(word_dataframe["token"].values)
        token_list = word_dataframe["token"].values.tolist()
        token_list.extend(dict_phonemize.split(" "))
        # print(token_list)
        word_dataframe = pd.DataFrame(token_list, columns=["token"])
        word_dataframe = word_dataframe.drop_duplicates().reset_index(drop=True)
        # n = n - 1

print(word_dataframe)
print(word_dataframe["token"].values.tolist())
word_dataframe.to_csv("../Data-Sample/word_tamil_tokens.txt", index=False)