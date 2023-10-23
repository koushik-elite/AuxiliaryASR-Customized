from phonemizer import phonemize
from phonemizer.backend import EspeakBackend
from phonemizer.separator import Separator
import os
from os import listdir
from os.path import isfile, join
from os import walk
import pandas as pd
from tqdm import tqdm
import shutil


mypath = "/mnt/d/mile_tamil_asr_corpus/mile_tamil_asr_corpus/train"
trans_files = mypath + "/trans_files"
audio_files = mypath + "/audio_files/"
text_dataframe = pd.DataFrame([], columns=["file", "text", "class"])

srcpath = "/mnt/d/mile_tamil_asr_corpus/asr_train_data"
if os.path.exists(srcpath):
    shutil.rmtree(srcpath)
os.makedirs(srcpath + "/waves")

f = []
backend = EspeakBackend('ta')
separator_out = Separator(phone=' ', word='__')
n = 50000
for (dirpath, dirnames, filenames) in walk(trans_files):
    for file in tqdm(filenames[:n]):

        file_name, extension = os.path.splitext(file)
        # print(file_name)
        # print(dirpath)
        readline = ""
        with open(dirpath + "/" + file) as fp:
            for line in fp:
                readline = line
        # print(readline)
        out_phonemize = backend.phonemize([readline], separator=separator_out, strip=True)[0]
        if "'" in out_phonemize:
            out_phonemize.remove("'")
        # Create a pandas Series object with all the column values passed as a Python list
        # s_row = pd.Series([file_name,out_phonemize,0], index=text_dataframe.columns)
        
        # Append the above pandas Series object as a row to the existing pandas DataFrame
        # Using the DataFrame.append() function
        # text_dataframe = text_dataframe.append(s_row, ignore_index=True)
        text_dataframe = pd.concat([
            pd.DataFrame([[file_name + ".wav",out_phonemize,0]], columns=["file", "text", "class"]), 
           text_dataframe
        ], ignore_index=True)
        # print(out_phonemize)
        # print(out_phonemize.split("__"))
        # print(len(out_phonemize.split("__")))
        # n = n - 1
        dest = shutil.copy(
            audio_files + file_name + ".wav", 
            srcpath + "/waves/" + file_name + ".wav"
        )

print(text_dataframe.head())
text_dataframe.to_csv("../Data-Sample/train_tamil_tokens.txt", index=False)