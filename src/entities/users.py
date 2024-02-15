from SQLAlchemy import Column, String, Interger
from src.config import Base

class Users(Base):
  __tablename__ = "users"

  id   = Column(Interger, primary_key=true)
  name = Column(String)

  def __repr__(self) -> str:
    return f"Users [name={self.name}]"