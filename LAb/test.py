import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df_mtx = pd.read_csv("c411_mtx.csv")
df_puro_2019 = pd.read_csv("puro_2019.csv")
df_puro_2013 = pd.read_csv("puro_2013.csv")
df_stem = pd.read_csv('c411_stem_2013.csv')
df_puro_2019 = df_puro_2019.drop('Unnamed: 11', axis = 1).set_index('Chromosome #')
df_stem = df_stem.set_index('Chromosome #')
df_puro_2013 = df_puro_2013.set_index('Chromosome #')
columns = ['K1', 'K10', 'K11', 'K12', 'K13', 'K14', 'K15', 'K16', 'K17', 'K18', 'K19', 'K20']
df_mtx = df_mtx.drop(columns, axis = 1).set_index('Chromosome #')