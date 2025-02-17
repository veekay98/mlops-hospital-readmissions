import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/hospital_readmissions.csv")

# Basic preprocessing
df.dropna(inplace=True)

# Save cleaned dataset
df.to_csv("data/processed_data.csv", index=False)

# Exploratory Data Analysis
sns.histplot(df["readmitted"], kde=True)
plt.title("Readmission Distribution")
plt.savefig("eda_readmission.png")
