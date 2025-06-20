from src.extract.extract_from_excel import df
import re

category_rules = {
    "Tesco": "Groceries",
    "Budgens": "Groceries",
    "Arc'teryx": "Shopping",
    "AliExpress": "Shopping",
    "EBAY Commerce UK Ltd": "Income",
    "Heathley Park": "Eating out",
    "Uber": "Transport",
    "Netflix": "Entertainment",
    "Pinnacle Bouldering": "Fitness",
    "Rent": "Rent",
    "Salary": "Income",
    "Holland & Barrett": "Health",
    "Boots": "Health",
    "iHerb": "Health",
    "Trainline": "Transport",
    "Chocoberry": "Shopping",
    "McDonald's": "Eating out",
    "Social Climbing": "Fitness",
    "Weekday": "Shopping",
    "Wakaze": "Eating out",
    "Devils Own Piercing L": "Entertainment",
    "Kubus Leicester Ltd": "Groceries",
    "Deliveroo": "Eating out",
    "Hotel Chocolat": "Shopping",
    "Oakley": "Shopping",
    "Lcuk Leicester Ltd": "Shopping",
    "MM Dental Care": "Health",
    "Baltika Local": "Groceries",
    "Amazon": "Shopping",
    "Cupp Leicester": "Eating out",
    "Arriva": "Transport",
    "Fee refund": "Income",
    "Trowell N E Bk": "Groceries",
    "Mangopay S.A.": "Income",
    "Seoul Plaza": "Shopping",
    "Vodafone": "Bills",
    "Sp Regn Ltd": "Shopping",
    "Jigbox": "Shopping",
    "Societe des Autoroutes": "Transport",
    "John Lewis": "Shopping",
    "Mark & Spencer": "Groceries"
}

def normalize(text):
    return re.sub(r"[^\w\s]", "", text)

normalized_rules = {}
for k, v in category_rules.items():
    normalized_key = normalize(k)
    normalized_rules[normalized_key] = v


df["Description"] = df["Description"].str.strip()

def categorize(description):
    norm_desc = normalize(description)
    for keyword, category in normalized_rules.items():
        if keyword in norm_desc:
            return category
    return "Other"

df["Category"] = df["Description"].apply(categorize)

#other_df = df[df["Category"] == "Other"]
#print(len(other_df)) # 0

#categories = df.groupby("Category")
#print(categories.all().to_string()) #Bills, Eating out, Entertainment, Fitness, Groceries, Health, Income, Shopping, Transport
