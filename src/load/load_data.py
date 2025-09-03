from src.transform.transformed_data import df
from sqlalchemy import text
from db.connection import get_engine

engine = get_engine()

# try:
#     with engine.connect() as conn:
#         result = conn.execute(text("SELECT 1"))
#         if result.scalar() == 1:
#             print("Connection successful")
# except Exception as e:
#     print("Connection failed", e)

categories_list = list(df['Category'].unique()) #['Shopping', 'Groceries', 'Eating out', 'Income', 'Health', 'Transport', 'Fitness', 'Entertainment', 'Bills']

with engine.begin() as conn:  
    
    #TABLE CATEGORIES
    for category in categories_list:
        conn.execute(
            text("INSERT INTO categories (category_name) VALUES (:category_name) ON CONFLICT DO NOTHING"),
            {"category_name": category}
        )
    # category_result = conn.execute(text("SELECT * FROM categories"))
    # for row in category_result:
    #     print(row)
    
    #mapping category names
    category_map = {}
    result = conn.execute(text("SELECT category_id, category_name FROM categories")).mappings()
    for row in result:
        category_map[row['category_name']] = row['category_id']
        
    #TABLE TRANSACTIONS
    for index, row in df.iterrows():
        conn.execute(
            text("""
                INSERT INTO transactions (transaction_date, transaction_description, transaction_amount, category_id)
                VALUES (:transaction_date, :transaction_description, :transaction_amount, :category_id) ON CONFLICT DO NOTHING
            """),
            {
                "transaction_date": row['Date'],
                "transaction_description": row['Description'],
                "transaction_amount": row['Amount'],
                "category_id": category_map[row['Category']]
            }
        )
    # transactions_result = conn.execute(text("SELECT * FROM transactions"))
    # for row in transactions_result:
    #     print(row)












# categories = df.groupby("Category")
# df_categories = categories.all().to_string() #Bills, Eating out, Entertainment, Fitness, Groceries, Health, Income, Shopping, Transport

# df_categories.to_sql('categories', con=connect, if_exists='replace', index=False)
