 Customer Segmentation Using RFM

## Overview
This project performs **customer segmentation** using the **RFM (Recency, Frequency, Monetary) model**. It allows users to upload their own CSV files containing customer purchase data and outputs a table showing customer segments and RFM scores. Users can also download the RFM data as a CSV.

---

## Features
- Upload a CSV file with customer data (`CustomerID`, `InvoiceDate`, `Amount`).
- Automatic calculation of:
  - **Recency** – Days since last purchase
  - **Frequency** – Number of purchases
  - **Monetary** – Total purchase value
- **RFM scoring** for each customer.
- Customer segmentation into categories:
  - **Champions**
  - **Loyal Customers**
  - **New Customers**
  - **At Risk**
  - **Lost**
- Display results in a **styled HTML table**.
- **Download RFM results as a CSV**.
- Built using **Python, Flask, Pandas, and Bootstrap**.

---

## Usage

1. **Clone the repository:**

```bash
git clone <your-github-link>
cd <your-repo-folder>
Install dependencies:

bash
Copy code
pip install flask pandas
Run the Flask app:

bash
Copy code
python app.py
Open the app in your browser:

cpp
Copy code
http://127.0.0.1:5000/
Steps inside the app:

Upload a CSV file with customer purchase data.

Click View RFM Analysis.

Check the table with RFM scores and segments.

Optionally, download the CSV using the Download CSV button.

CSV Format
Your CSV file should contain the following columns:

Column Name	Description
CustomerID	Unique identifier for customers
InvoiceDate	Date of the purchase (YYYY-MM-DD)
Amount	Purchase amount (numeric)

Technologies Used
Python – Backend logic and RFM calculations

Flask – Web framework

Pandas – Data manipulation and calculations

Bootstrap – Responsive frontend design

Screenshots
Add your screenshots or description of outputs here.

License
This project is open-source and available under the MIT License.

yaml
Copy code

---

If you want, I can also **add GitHub badges for Python version, Flask version, and license** to make it look more professional.  

Do you want me to do that?






You said:
readme.md 


ChatGPT said:
Here’s your README.md file content ready to save directly in your project:

markdown
Copy code
# Customer Segmentation Using RFM

## Overview
This project performs **customer segmentation** using the **RFM (Recency, Frequency, Monetary) model**. It allows users to upload their own CSV files containing customer purchase data and outputs a table showing customer segments and RFM scores. Users can also download the RFM data as a CSV.

---

## Features
- Upload a CSV file with customer data (`CustomerID`, `InvoiceDate`, `Amount`).
- Automatic calculation of:
  - **Recency** – Days since last purchase
  - **Frequency** – Number of purchases
  - **Monetary** – Total purchase value
- **RFM scoring** for each customer.
- Customer segmentation into categories:
  - **Champions**
  - **Loyal Customers**
  - **New Customers**
  - **At Risk**
  - **Lost**
- Display results in a **styled HTML table**.
- **Download RFM results as a CSV**.
- Built using **Python, Flask, Pandas, and Bootstrap**.

---

## Usage

1. **Clone the repository:**

```bash
git clone <your-github-link>
cd <your-repo-folder>
Install dependencies:

bash
Copy code
pip install flask pandas
Run the Flask app:

bash
Copy code
python app.py
Open the app in your browser:

cpp
Copy code
http://127.0.0.1:5000/
Steps inside the app:

Upload a CSV file with customer purchase data.

Click View RFM Analysis.

Check the table with RFM scores and segments.

Optionally, download the CSV using the Download CSV button.

CSV Format
Your CSV file should contain the following columns:

Column Name	Description
CustomerID	Unique identifier for customers
InvoiceDate	Date of the purchase (YYYY-MM-DD)
Amount	Purchase amount (numeric)

Technologies Used
Python – Backend logic and RFM calculations

Flask – Web framework

Pandas – Data manipulation and calculations

Bootstrap – Responsive frontend design

