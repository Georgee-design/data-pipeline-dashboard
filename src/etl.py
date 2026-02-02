import pandas as pd
from sqlalchemy.orm import sessionmaker
from db import Sales, engine

Session = sessionmaker(bind=engine)
session = Session()

# Replace with your dataset path
df = pd.read_csv("data/superstore.csv")
df["order_date"] = pd.to_datetime(df["order_date"])

for _, row in df.iterrows():
    record = Sales(
        product=row["Product Name"],
        category=row["Category"],
        sales_amount=row["Sales"],
        order_date=row["Order Date"]
    )
    session.add(record)
    

session.commit()

