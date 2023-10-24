# need to pip install requests
import requests
# from phonemizer import phonemize
# from phonemizer.separator import Separator
# from phonemizer.backend import EspeakBackend
import os
from os.path import isfile, join
import re
import sys
import shutil
import pandas as pd
import csv
from tqdm import tqdm

data_df = pd.read_csv("/home/ubuntu/AuxiliaryASR-Customized/Data-Sample/train_tamil_tokens.txt")

data_df["file"] = data_df["file"].apply(lambda x: "/mnt/d/mile_tamil_asr_corpus/asr_train_data/waves/" + x)
# data_df["text"] = data_df["text"].apply(lambda x: x.replace("|", " "))

data_df = data_df[["file", "text", "class"]]
print(data_df.head())

size = data_df.shape[0]
split_no = int(size * 0.8)

train_list = data_df[:split_no]
val_list = data_df[split_no:]

train_list.to_csv("/home/ubuntu/AuxiliaryASR-Customized/Data/train_list.txt", header=None, sep="|", index=False)
val_list.to_csv("/home/ubuntu/AuxiliaryASR-Customized/Data/val_list.txt", header=None, sep="|", index=False)