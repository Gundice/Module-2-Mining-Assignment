import pandas as pd

# Read the dataset
df = pd.read_csv(r'C:\Users\Adeyemo Bolanle\Downloads\dataset copy.csv')

# Rename columns to lowercase
df.columns = df.columns.str.lower()

# Print the column names to verify
print("Original column names:", df.columns)

# Print the number of rows before dropping any missing values
print("Number of rows before dropping missing values:", len(df))

# Implement data cleaning steps
# Replace missing values in 'advertisingagency' with the mode
df['advertisingagency'].fillna(df['advertisingagency'].mode()[0], inplace=True)

# Replace missing values in 'ratingofproduct' with the mean
df['ratingofproduct'].fillna(df['ratingofproduct'].mean(), inplace=True)

# Replace missing values in 'custname' with 'Unknown Customer'
df['custname'].fillna('Unknown Customer', inplace=True)

# Replace missing values in 'age' with the mean
df['age'].fillna(df['age'].mean(), inplace=True)

# Replace missing values in 'product' with the mode
df['product'].fillna(df['product'].mode()[0], inplace=True)

# Drop rows with missing 'datepurchased' values
df.dropna(subset=['datepurchased'], inplace=True)

# Drop rows with missing 'price' values
df.dropna(subset=['price'], inplace=True)

# Print the number of rows after dropping missing values
print("Number of rows after dropping missing values:", len(df))

# Print the cleaned dataset
print("Cleaned dataset:")
print(df)

# Save the cleaned dataset
df.to_csv("C:\\Users\\Adeyemo Bolanle\\Downloads\\cleaned_dataset.csv", index=False)
print("saved Successfully")
