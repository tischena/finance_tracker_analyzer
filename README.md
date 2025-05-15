<!-- Summary:
Build a tool to track personal expenses, automatically categorize them (e.g. groceries, rent, entertainment), and store results in a database with visual analytics.

Key Skills Used:
Python (pandas, regex, datetime)
PostgreSQL/MySQL
ETL logic
Excel file processing

Optional: Matplotlib/Seaborn or Streamlit

Steps:
Input CSV/Excel bank statements.
Parse and clean data, auto-tag categories.
Store results in PostgreSQL.
Show summaries (monthly spend, categories, trends).

Stretch goal: Add a rule-based classifier to categorize transactions. 

Project Workflow:
1.Extract:
Load data from CSVs or Excel (bank statements or sample datasets).
Use libraries like pandas, openpyxl, or csv.

2.Transform:
Clean missing/invalid data.
Parse dates, extract merchant names.
Categorize transactions: e.g., “Tesco” → Groceries.

3.Load
Store in a PostgreSQL or SQLite database.
Build a schema: transactions, categories, summary.

4.Analyze
Monthly spend trends.
Category breakdowns.
Biggest changes month-over-month.

5.Visualize (Optional)
Use Matplotlib, Seaborn, or Plotly.
Create a Streamlit dashboard (easy + interactive).

🧠 Add-on Analysis Ideas:
Compare spending to budget
Detect unusual spikes
Cluster expenses using K-Means (mini intro to unsupervised ML)
Generate monthly financial health reports (automated PDF or dashboard)

📊 Tools Stack:
Python (pandas, numpy, matplotlib, seaborn)
PostgreSQL or SQLite (lightweight)
VS Code
Optionally: Streamlit or Jupyter Notebooks for interactive analysis-->