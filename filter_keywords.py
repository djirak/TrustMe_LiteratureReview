'''Brief script to filter current reviews with topic ``XAI", ``trust", etc.
Input is Excel file that contains: 1.col=Title, 2.col=publication year 3. keywords associated with that review paper
'''
import pandas as pd

# Load the Excel file
file_path = 'path_to_your_file/Reviews.xlsx'  # Replace with your file path
df = pd.read_excel(file_path)

# Filter rows where (here: third column) contains words starting with ``trust" using a regular expression
trust_filtered_df = df[df.iloc[:, 2].str.contains(r'\btrust\w*', na=False, case=False, regex=True)]

#print(trust_filtered_df)
#trust_filtered_df.to_excel('filtered.xlsx', index=False)
trust_filtered_df.to_csv('filtered.csv', index=False)