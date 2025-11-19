from sqlalchemy import text
from connection import get_engine

engine = get_engine()

with engine.begin() as conn:
    
    # category_result = conn.execute(text("SELECT * FROM categories"))
    # for row in category_result:
    #     print(row)
    
    # transactions_result = conn.execute(text("SELECT * FROM transactions"))
    # for row in transactions_result:
    #     print(row)
    
    # groceries_list_result = conn.execute(text("SELECT * FROM transactions WHERE category_id = 2 "))
    # for row in groceries_list_result:
    #     print(row)
    
    # groceries_sum_result = conn.execute(text("SELECT SUM(transaction_amount) FROM transactions WHERE category_id = 2 "))
    # for row in groceries_sum_result:
    #     print(row)
    
    # groceries_sum_april_result = conn.execute(text("SELECT SUM(transaction_amount) FROM transactions WHERE category_id = 2 AND transaction_date BETWEEN '2025-04-01' AND '2025-04-30' "))
    # for row in groceries_sum_april_result:
    #     print(row)
    
    total_spend_april_result = conn.execute(text("SELECT transaction_amount, transaction_date FROM transactions WHERE transaction_date BETWEEN '2025-04-01' AND '2025-04-30' AND transaction_amount < 0 "))
    for row in total_spend_april_result:
        print(row)