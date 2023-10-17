import torch
from torch import nn
embedding = nn.Embedding(80,256)
print(embedding)
text = []
for i in range(20):
    text_j = []
    for j in range(80):
        text_j.append(j)
    text.append(text_j)

input_t = torch.LongTensor(text)
print(input_t)
print(input_t.shape)
output_t = embedding(input_t)
print(output_t.shape)