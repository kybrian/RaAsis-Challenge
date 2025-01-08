# RaAsis-Challenge
# Setup Instructions
#### Create Environment
`python3 -m venv env`

#### Activate Environment
`source env/bin/activate`

#### Install Dependencies
`pip install -r requirements.txt`

___

# Task Description
You are tasked with analysing a ride-sharing dataset to extract insights and trends.
Your goal is to process the data, uncover patterns, and generate actionable findings.

## About Dataset
The dataset includes 650 rows and the following columns:
- **Ride ID**: Unique identifier for each ride.
- **Request Time**: Timestamp of when the ride was requested.
- **Pickup Location**: Latitude and longitude of the pickup location.
- **Dropoff Location**: Latitude and longitude of the dropoff location.
- **Ride Distance**: Distance of the ride in miles.
- **Fare Amount**: Total fare for the ride.
- **Payment Method**: Method used for payment (e.g., Credit Card, Cash).
- **Driver ID**: Identifier for the driver.
- **Vehicle Type**: Type of vehicle used for the ride (e.g., SUV, Sedan, Motorcycle).
- **Traffic Conditions**: Traffic level during the ride (e.g., Low, Medium, High).
- **Day of Week**: Day the ride took place.
- **Public Holiday**: Indicates if the ride occurred on a public holiday.
- **Peak Hours**: Indicates if the ride was during peak hours.
- **User Ratings**: Rating given by the rider for the ride experience.

## Task Steps

### 1. Data Loading and Inspection
- Load the dataset into a Pandas DataFrame.
- Display the first few rows and summarize the dataset.
- Check for missing values and any anomalies.

### 2. Data Preprocessing
- Convert the Request Time column into a readable datetime format.
- Create new columns for Hour and Month extracted from the Request Time.
- Impute missing User Ratings with the average rating.

### 3. Exploratory Data Analysis (EDA)
- Find the average fare amount grouped by Traffic Conditions.
- Identify the most common Vehicle Type used during Peak Hours.
- Determine which day of the week has the highest average user rating.
- Visualize the distribution of Ride Distance using a histogram.

### 4. Trend Analysis
- Analyse the correlation between Ride Distance and Fare Amount.
- Identify the busiest time of the day for ride requests based on Request Time.
- Compare the average Fare Amount on public holidays vs. non-holidays.

### 5. Bonus Challenge (For Bonus Points)
- Simulate working with a larger dataset by loading the data in chunks (e.g., using Pandas’ chunksize).
- Predict the Fare Amount for a ride using a simple linear regression model with Ride Distance as the predictor.

## Deliverables
You should create a GitHub repository containing your work and share the link. The repository should include:

### Python Scripts
- A well-organized Python script file (`ride_sharing_analysis.py`) containing:
  - **Data Inspection and Preprocessing**: Steps to load and clean the data.
  - **EDA Code**: Functions or clearly marked sections performing exploratory data analysis.
  - **Visualizations**: Code to generate and save plots (e.g., using Matplotlib or Seaborn) as image files.

- **Bonus Task Code (if attempted)**: A separate Python file (`fare_prediction.py`) implementing the bonus challenge (e.g., linear regression model).

### Output Files
- Saved visualizations (e.g., histograms, line charts) as image files in a `visualizations/` folder.
- Summary insights printed to the console and optionally written to a text file (`summary.txt`).
