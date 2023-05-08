from test import predict
from config import *

data = open(new_data, 'r', encoding='utf-8').read().split()

# Travel the new data
for i in range(0, len(data) - window):
    words = ' '.join(data[i:i+window])
    if predict(words) == original_id:
        print('New ID is: ', data[i+window])
        break
