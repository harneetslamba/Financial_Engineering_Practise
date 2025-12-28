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

clean_data.to_excel(r"C:\D_Drive\Practise\machine_learning_pipeline\data\cleaned_complaints.xlsx", index=False)
print("Cleaned data saved to Excel file.")

clean_data['addressed_narrative'] = clean_data['addressed_narrative'].apply(
    lambda x: re.sub(r'http\S+|www\S+|https\S+', '', x, flags=re.MULTILINE))

clean_data.to_excel(r"C:\D_Drive\Practise\machine_learning_pipeline\data\data\cleaned_consumer_complaints.xlsx", index=False)
print("Cleaned data saved to Excel file.")

data_summary = clean_data['Product'].value_counts().reset_index()
data_summary.columns = ['Product', 'Count']

df = data.pivot_table(index='Product', values='Consumer complaint narrative', aggfunc=lambda x: ' '.join(x))
df.to_csv(r"C:\D_Drive\Practise\machine_learning_pipeline\data\data\pivoted_consumer_complaints.csv")

<<<<<<< HEAD
Additional_summary = clean_data['Product'].value_counts().reset_index()
Additional_summary.columns = ['Product', 'Count']
=======
print("Pivoted data saved to CSV file.")
clean_data.to_csv(r"C:\D_Drive\Practise\machine_learning_pipeline\data\data\cleaned_consumer_complaints.csv", index=False)
print("Cleaned data saved to CSV file.")
>>>>>>> test_branch
