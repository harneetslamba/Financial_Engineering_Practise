import numpy as np
import pandas as pd
import re

data = pd.read_csv(r"C:\D_Drive\Practise\machine_learning_pipeline\data\data\consumer_complaints_with_narrative.csv")
data = data.dropna(subset=['Consumer complaint narrative'])

data = data.sample(n=1000, random_state=42)
data = data.loc[data['Product'].isin(['Credit reporting, credit repair services, or other personal consumer reports',
                                     'Debt collection'])]
clean_data = data[['Product', 'Consumer complaint narrative']].copy()
clean_data['addressed_narrative'] = clean_data['Consumer complaint narrative'].str.lower()
