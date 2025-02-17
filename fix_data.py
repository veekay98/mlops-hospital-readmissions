import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load the dataset
input_file = "data/processed_data.csv"  # Update the path if needed
output_file = "data/cleaned_data.csv"

df = pd.read_csv(input_file)

# Convert age ranges to numeric values (e.g., "[70-80)" -> 75)
def convert_age_range(age):
    age = age.strip("[]()")  # Remove brackets
    lower, upper = age.split('-')
    return (int(lower) + int(upper)) / 2  # Take average of range

df['age'] = df['age'].apply(convert_age_range)

# Convert binary categorical columns ('yes'/'no') to 0/1
binary_columns = ['glucose_test', 'A1Ctest', 'change', 'diabetes_med', 'readmitted']
for col in binary_columns:
    df[col] = df[col].map({'no': 0, 'yes': 1})

# Label Encode categorical features
categorical_columns = ['medical_specialty', 'diag_1', 'diag_2', 'diag_3']
label_encoders = {}

for col in categorical_columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col].astype(str))  # Ensure data is treated as string
    label_encoders[col] = le  # Save encoders for future use

# Save cleaned dataset
df.to_csv(output_file, index=False)
print(f"✅ Data cleaning complete! Cleaned dataset saved at: {output_file}")

# Display first few rows to confirm changes
print(df.head())
