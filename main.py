import pandas as pd  

# Defining the file path of the Excel file
file_path = "sample.xlsx"  

# Reading the Excel file and storing its contents into a pandas DataFrame
df = pd.read_excel(file_path)  

# Create an empty DataFrame to store the percentages of responses
result_df = pd.DataFrame(columns=['Question No.', 'Question', 'Response', 'Percentage'])

# Converting the DataFrame's column names to a list for iteration
columns_to_include = df.columns.tolist()  

# Initialize a counter for row numbers
row_number = 1

# Iterating through each column in the DataFrame
for column in columns_to_include:
    # Counting the total number of responses in the current column
    total_responses = df[column].count() 
    
    # Calculating the percentage of each response in the current column
    percentage_responses = (df[column].value_counts() / total_responses) * 100  
    
    # Create a DataFrame with the percentages of responses for the current column
    response_df = pd.DataFrame({'Question No.': row_number, 'Question': column, 'Response': percentage_responses.index, 'Percentage': percentage_responses.values})
    
    # Concatenate the response DataFrame with the result DataFrame
    result_df = pd.concat([result_df, response_df], ignore_index=True)
    
    row_number += 1

# Exporting the result DataFrame to a CSV file
result_csv_file = "response_percentages.csv"

# Rename columns
result_df = result_df.rename(columns={'Question No.': 'Question No.', 'Question': 'Question', 'Response': 'Response', 'Percentage': 'Percentage'})

result_df.to_csv(result_csv_file, index=False)

print(f"Results have been saved to {result_csv_file}")
