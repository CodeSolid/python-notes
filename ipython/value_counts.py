# Counting values for a column of data:
import pandas as pd
tab = pd.read_csv('test_counts.csv')
print(tab.Names.value_counts())
