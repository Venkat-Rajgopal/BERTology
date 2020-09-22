import os
import pandas as pd
from tqdm import tqdm

def read_texts(path, target):
    """
    Takes an input path and reads the txt files 
    All outputs rewitten as pandas dataframes with review and sentiment as columns
    Text sentiment classes are already known
    """

    df = pd.DataFrame(columns = ['review', 'sentiment'])

    for dirname, dirnames, filenames in os.walk(path):
    # print path to all subdirectories first.

        for filename in tqdm(filenames,total = len(filenames)):      
            file = os.path.join(dirname, filename)
        
            with open(file, 'r', encoding="utf8") as f:
                rev = f.readlines()
                df = df.append({'review': rev[0], 'sentiment': target}, ignore_index=True)
            
    return df


df_trainpos = read_texts(path='data/train/pos/', target='positive')
df_trainneg = read_texts(path='data/train/neg/', target='negative')

