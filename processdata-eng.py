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

train_list = pd.read_csv("/home/koushik/AuxiliaryASR-Customized/Data-Sample/train_list.txt", delimiter="|", header=None)
val_list = pd.read_csv("/home/koushik/AuxiliaryASR-Customized/Data-Sample/val_list.txt", delimiter="|", header=None)
print(train_list.head())

train_list[0] = train_list[0].apply(lambda x: "/home/koushik/AuxiliaryASR-Customized/LJSpeech_small/wavs/" + x)
val_list[0] = val_list[0].apply(lambda x: "/home/koushik/AuxiliaryASR-Customized/LJSpeech_small/wavs/" + x)

train_list.to_csv("/home/koushik/AuxiliaryASR-Customized/Data/train_list.txt", header=None, sep="|", index=False)
val_list.to_csv("/home/koushik/AuxiliaryASR-Customized/Data/val_list.txt", header=None, sep="|", index=False)