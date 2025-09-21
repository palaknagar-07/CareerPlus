import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
# import seaborn as sns
path = "/Users/palak/Desktop/Project/Career+/DataSet/naukri_com-job_sample.csv"
df = pd.read_csv(path)
print(df.head())
print(df.info())