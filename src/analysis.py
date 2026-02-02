import pandas as pd
from sqlalchemy import create_engine
import seaborn as sns
import matplotlib.pyplot as plt

engine = create_engine("sqlite:///data/sales.db")
df = pd.read_sql("SELECT * FROM sales", engine)

df["order_date"] = pd.to_datetime(df["order_date"])  # ensure datetime

monthly_sales = df.groupby(df["order_date"].dt.to_period("M"))["sales_amount"].sum()
monthly_sales.index = monthly_sales.index.astype(str)

sns.lineplot(x=monthly_sales.index, y=monthly_sales.values)
plt.xticks(rotation=45)
plt.title("Monthly Sales Trend")
plt.savefig("monthly_sales.png")  # save safely




