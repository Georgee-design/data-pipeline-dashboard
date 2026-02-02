
from sqlalchemy import Column, Integer, String, Float, Date, create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Sales(Base):
    __tablename__ = "sales"
    id = Column(Integer, primary_key=True)
    product = Column(String)
    category = Column(String)
    sales_amount = Column(Float)
    order_date = Column(Date)

engine = create_engine("sqlite:///data/sales.db")
Base.metadata.create_all(engine)


