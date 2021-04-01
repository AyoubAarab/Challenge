import pandas as pd
import numpy as np

def format_drop (df, col): #expecting the dataset to always be in the same format when downloaded
    df.drop(['U1','U2'],axis=1,inplace=True)
    df.dropna(inplace=True)
    
    return df

def format_name (df, rename):
    df.columns= rename
    return df

def format_time (df):
    formated_time = pd.to_datetime(df['Date'] + " "+ df["Time"], format = '%d/%m/%Y %H:%M:%S')
    df.insert(0,'Timeused',formated_time)
    df = df[df['Time'] <= '09:00:00']
    df = df.sort_index(ascending = False).drop_duplicates('Date')
    df = df.sort_index(ascending=True)
    df.reset_index(drop=True, inplace=True)
    return df

