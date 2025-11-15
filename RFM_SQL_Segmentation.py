import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from datetime import datetime

# -----------------------------------------
# RFM Customer Segmentation using SQL + Python
# -----------------------------------------

# Step 1: Connect to SQL Database (Edit credentials)
HOST = "localhost"
USER = "root"
PASSWORD = "12345"
DATABASE = "salesdb"

engine = create_engine(f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}/{DATABASE}")

# Step 2: Load Data from SQL Table
query = "SELECT InvoiceNo, CustomerID, InvoiceDate, Quantity, UnitPrice FROM orders"
df = pd.read_sql(query, engine)

# Step 3: Data Cleaning
df.dropna(subset=['CustomerID'], inplace=True)
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['TotalAmount'] = df['Quantity'] * df['UnitPrice']

# Step 4: Define Reference Date
reference_date = df['InvoiceDate'].max() + pd.Timedelta(days=1)

# Step 5: Calculate RFM Metrics
rfm = df.groupby('CustomerID').agg(
    Recency=('InvoiceDate', lambda x: (reference_date - x.max()).days),
    Frequency=('InvoiceNo', 'nunique'),
    Monetary=('TotalAmount', 'sum')
).reset_index()

# Step 6: Assign RFM Scores (1–5)
rfm['R_Score'] = pd.qcut(rfm['Recency'], 5, labels=[5,4,3,2,1])
rfm['F_Score'] = pd.qcut(rfm['Frequency'], 5, labels=[1,2,3,4,5])
rfm['M_Score'] = pd.qcut(rfm['Monetary'], 5, labels=[1,2,3,4,5])

# Step 7: Create RFM Combined Score
rfm['RFM_Score'] = (
    rfm['R_Score'].astype(str) 
    + rfm['F_Score'].astype(str) 
    + rfm['M_Score'].astype(str)
)

# Step 8: Customer Segmentation Logic
def segment_customer(row):
    r, f, m = int(row['R_Score']), int(row['F_Score']), int(row['M_Score'])

    if r >= 4 and f >= 4 and m >= 4:
        return "Champions"
    elif r >= 3 and f >= 3 and m >= 3:
        return "Loyal Customers"
    elif r >= 3 and f <= 2 and m <= 2:
        return "New Customers"
    elif r <= 2 and f >= 3 and m >= 3:
        return "At-Risk"
    elif r <= 2 and f <= 2 and m <= 2:
        return "Lost"
    else:
        return "Others"

rfm['Segment'] = rfm.apply(segment_customer, axis=1)

# Step 9: Print Final RFM Table
print("Final RFM Segmentation Table:")
print(rfm)
