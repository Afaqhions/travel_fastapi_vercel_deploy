from sqlalchemy import Column, Integer, String, Text
from app.database import Base


class Destination(Base):
    __tablename__ = "destinations"

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String, nullable=False)
    country = Column(String, nullable=False)
    description = Column(Text, default="")
