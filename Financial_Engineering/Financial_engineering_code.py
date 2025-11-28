import numpy as np
import pandas as pd
import re

data = pd.read_csv(r"C:\D_Drive\Practise\machine_learning_pipeline\data\data\consumer_complaints_with_narrative.csv")
data = data.dropna(subset=['Consumer complaint narrative'])