import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

# -----------------------------
# STEP 1: LOAD CSV FILE
# -----------------------------
# Replace 'your_file.csv' with your CSV file path


df = pd.read_csv(r"C:\Users\abhi1\Downloads\iris.csv")

# -----------------------------
# STEP 2: BASIC DATA INSPECTION
# -----------------------------
print("First 5 rows:")
print(df.head())

print("\nData info:")
print(df.info())

print("\nBasic statistics:")
print(df.describe())

# -----------------------------
# STEP 3: CHECK NULL VALUES
# -----------------------------
print("\nNull values in each column:")
print(df.isnull().sum())

print("\nNull values in each row:")
print(df.isnull().sum(axis=1))

# -----------------------------
# STEP 4: HANDLE NULL VALUES
# -----------------------------
# Option 1: Drop rows with null values
df_drop = df.dropna()
print("\nAfter dropping null values:")
print(df_drop)

# Option 2: Fill null values with a constant value "0"
df_fill_constant = df.fillna(0)
print("\nAfter filling null values with 0:")
print(df_fill_constant)

# Option 3: Fill null values with forward fill (ffill) or backward fill (bfill)
df_ffill = df.fillna(method='ffill')
df_bfill = df.fillna(method='bfill')

# Option 4: Fill null values with mean of a column
# Replace 'column_name' with your actual column name
column_name = df.columns[0]  # Example: use first column
mean_value = df[column_name].mean()
df[column_name].fillna(mean_value, inplace=True)

# -----------------------------
# STEP 5: DETECT OUTLIERS USING BOXPLOT
# -----------------------------
# Replace 'column_name' with your actual column name for outlier detection
plt.figure(figsize=(8,5))
sns.boxplot(x=df[column_name])
plt.title("Boxplot for Outlier Detection")
plt.show()

# -----------------------------
# STEP 6: REMOVE OUTLIERS USING IQR METHOD
# -----------------------------
Q1 = df[column_name].quantile(0.25)
Q3 = df[column_name].quantile(0.75)
IQR = Q3 - Q1

# Filtering out outliers
df_no_outliers_iqr = df[~((df[column_name] < (Q1 - 1.5 * IQR)) | (df[column_name] > (Q3 + 1.5 * IQR)))]

# Check with boxplot after IQR
plt.figure(figsize=(8,5))
sns.boxplot(x=df_no_outliers_iqr[column_name])
plt.title("Boxplot After Removing Outliers (IQR)")
plt.show()

# -----------------------------
# STEP 7: REMOVE OUTLIERS USING Z-SCORE METHOD
# -----------------------------
z_scores = stats.zscore(df[column_name])
abs_z_scores = abs(z_scores)
df_no_outliers_z = df[abs_z_scores < 3]  # Keep rows with z-score < 3

# Check with boxplot after Z-score
plt.figure(figsize=(8,5))
sns.boxplot(x=df_no_outliers_z[column_name])
plt.title("Boxplot After Removing Outliers (Z-Score)")
plt.show()

print("\nScript Completed!")
