from src.transform.transformed_data import df
from db.connection import connect

categories = df.groupby("Category")
df_categories = categories.all().to_string() #Bills, Eating out, Entertainment, Fitness, Groceries, Health, Income, Shopping, Transport

df_categories.to_sql('categories', con=connect, if_exists='replace', index=False)
