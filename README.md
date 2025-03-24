# Customer Segmentation using RFM Analysis

## Introduction
This project applies **RFM Analysis (Recency, Frequency, Monetary)** and **K-Means Clustering** to segment customers based on their purchasing behavior. The goal is to help businesses understand customer patterns and implement data-driven marketing strategies.

## Features
- Data Preprocessing: Cleaning and transforming raw transaction data.
- RFM Analysis: Calculating Recency, Frequency, and Monetary scores for each customer.
- Data Normalization: Scaling RFM values for better clustering.
- K-Means Clustering: Segmenting customers into distinct groups.
- Visualization: Graphical representation of customer segments and profiles.

## Dataset
The dataset used for this project contains:
- `InvoiceNo`: Unique transaction identifier
- `CustomerID`: Unique customer identifier
- `InvoiceDate`: Date of transaction
- `Quantity`: Number of units purchased
- `UnitPrice`: Price per unit
- `TotalPrice`: Derived feature (Quantity × UnitPrice)

## Installation & Setup
### Prerequisites
Ensure you have the following installed:
- Python 3.x
- Jupyter Notebook (optional)
- Required libraries: Pandas, NumPy, Scikit-learn, Matplotlib

### Install Dependencies
```bash
pip install pandas numpy scikit-learn matplotlib
```

### Run the Project
1. Clone this repository:
```bash
git clone https://github.com/yourusername/customer-segmentation-rfm.git
```
2. Navigate to the project directory:
```bash
cd customer-segmentation-rfm
```
3. Run the Jupyter Notebook or Python script:
```bash
jupyter notebook
# OR
python customer_segmentation.py
```

## Project Workflow
### 1. Data Preprocessing
- Handling missing values and ensuring data consistency.
- Creating `TotalPrice` and converting `InvoiceDate` to datetime.

### 2. RFM Analysis
- Calculating **Recency** (days since last purchase).
- Calculating **Frequency** (total purchases per customer).
- Calculating **Monetary** (total spending per customer).

### 3. Data Normalization
- Applying MinMaxScaler to RFM values.

### 4. K-Means Clustering
- Using the **Elbow Method** to determine the optimal number of clusters.
- Applying K-Means clustering to segment customers.

### 5. Visualization
- **Customer Segment Profiles**: Bar chart of average RFM values per cluster.
- **Customer Segment Distribution**: Pie chart of customer distribution across clusters.

## Results & Business Strategies
- **High-Value Customers**: Loyalty programs, premium services.
- **Mid-Value Customers**: Incentives for larger purchases, referral programs.
- **Low-Value Customers**: Re-engagement strategies, targeted promotions.

## Contribution
Feel free to contribute by submitting a pull request or opening an issue.



---


