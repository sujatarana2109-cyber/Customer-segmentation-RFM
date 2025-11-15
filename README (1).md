# Customer Segmentation using RFM

This project performs **Customer Segmentation** using the **RFM Model**
(Recency, Frequency, Monetary) with data stored in a **MySQL database**
and analyzed in **Python**.

------------------------------------------------------------------------

## 📌 Features

-   Connects to MySQL database
-   Fetches customer transaction data
-   Calculates RFM scores
-   Assigns RFM segments (Champions, Loyal, At Risk, etc.)
-   Exports results to CSV
-   Includes a ready-to-use Python script

------------------------------------------------------------------------

## 📂 Project Structure

    ├── RFM_Segmentation.py
    ├── rfm_segments.csv
    ├── requirements.txt
    └── README.md

------------------------------------------------------------------------

## 🛠 Requirements

Install required packages:

    pip install -r requirements.txt

------------------------------------------------------------------------

## 🧪 How to Run

1.  Update your MySQL database details in the Python script:

```{=html}
<!-- -->
```
    host = "localhost"
    user = "root"
    password = "your_password"
    database = "your_database"

2.  Run the script:

```{=html}
<!-- -->
```
    python RFM_Segmentation.py

3.  Output CSV will be generated as:

```{=html}
<!-- -->
```
    rfm_segments.csv

------------------------------------------------------------------------

## 📊 RFM Segmentation Logic

-   **Recency** → Days since last purchase\
-   **Frequency** → Total number of purchases\
-   **Monetary** → Total amount spent

Segments include: - Champions\
- Loyal Customers\
- Potential Loyalist\
- At Risk\
- Hibernating\
- Lost

------------------------------------------------------------------------

## 👩‍💻 Author

Created for learning **Data Analytics** and **Customer Segmentation**
using Python + SQL.
