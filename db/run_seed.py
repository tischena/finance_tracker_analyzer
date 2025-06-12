from db.seed import seed
from db.connection import create_conn, close_db

# Example dummy data to seed with — replace with real ones
data = {
    "transactions": [],
    "categories": ["Groceries", "Shopping", "Rent", "Health", "Transport", "Income", "Eating out", "Bills", "Entertainment", "Fitness", "Other"]
}

db = None
try:
    db = create_conn()
    seed(db, **data)
except Exception as e:
    print("Error:", e)
finally:
    if db:
        close_db(db)
