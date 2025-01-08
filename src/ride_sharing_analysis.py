import pandas as pd

# 1. Data Loading and Inspection
# Load the dataset into a Pandas DataFrame.
excel_file = "Ride Sharing Dataset.xlsx"
df = pd.read_excel(excel_file)

# Display the first few rows and summarize the dataset.
print(df.head(5))

# Check for missing values and any anomalies.

# 2. Data Preprocessing
# Convert the Request Time column into a readable datetime format.

# Create new columns for Hour and Month extracted from the Request Time.

# Impute missing User Ratings with the average rating.

# 3. Exploratory Data Analysis (EDA)
# Find the average fare amount grouped by Traffic Conditions.

# Identify the most common Vehicle Type used during Peak Hours.

# Determine which day of the week has the highest average user rating.

# Visualize the distribution of Ride Distance using a histogram.

# 4. Trend Analysis
# Analyse the correlation between Ride Distance and Fare Amount.

# Identify the busiest time of the day for ride requests based on Request Time.

# Compare the average Fare Amount on public holidays vs. non-holidays.
