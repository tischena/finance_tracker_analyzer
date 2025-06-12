def seed(db, transactions, categories):
    '''Seeds database'''
    db.run("DROP TABLE IF EXISTS transactions;")
    db.run("DROP TABLE IF EXISTS categories;")
    create_categories(db)
    create_transactions(db)
    insert_categories(db, categories)

def create_categories(db):
    db.run('''
        CREATE TABLE categories(
            category_id SERIAL PRIMARY KEY,
            category_name VARCHAR(50) NOT NULL
        );
    ''')

def create_transactions(db):
    db.run('''
        CREATE TABLE transactions(
            transaction_id SERIAL PRIMARY KEY,
            transaction_date DATE NOT NULL,
            transaction_description TEXT NOT NULL,
            transaction_amount NUMERIC NOT NULL,
            category_id INT REFERENCES categories(category_id)
        );
    ''')

def insert_categories(db, categories):
    for cat in categories:
        db.run('''
            INSERT INTO categories(category_name)
            VALUES(:category_name)
        ''', category_name=cat)
