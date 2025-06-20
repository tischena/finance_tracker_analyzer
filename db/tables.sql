--DROP TABLE IF EXISTS example;

CREATE TABLE categories(
    category_id SERIAL PRIMARY KEY,
    category_name VARCHAR(50) NOT NULL
);

CREATE TABLE transactions(
    transaction_id SERIAL PRIMARY KEY,
    transaction_date DATE NOT NULL,
    transaction_description TEXT NOT NULL,
    transaction_amount NUMERIC NOT NULL,
    category_id INT REFERENCES categories(category_id)
);

-- INSERT INTO categories (category_id, category_name)
-- VALUES (0, 'Bills'),
--        (1, 'Eating out'),
--        (2, 'Entertainment'),
--        (3, 'Fitness'),
--        (4, 'Groceries'),
--        (5, 'Health'),
--        (6, 'Income'),
--        (7, 'Shopping'),
--        (8, 'Transport'),
--        (9, 'Other');