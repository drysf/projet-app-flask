import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('data.csv')

# Display the first few rows of the DataFrame
print(df.head())

# Get the shape of the DataFrame (number of rows, number of columns)
print(df.shape)

# Get descriptive statistics of the DataFrame
print(df.describe())

# Filter the DataFrame based on a condition
filtered_df = df[df['column_name'] > 10]

# Group the DataFrame by a column and calculate the mean of another column
grouped_df = df.groupby('column_name')['another_column'].mean()

# Save the filtered DataFrame to a new CSV file
filtered_df.to_csv('filtered_data.csv', index=False)