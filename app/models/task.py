from sqlalchemy import Boolean, Column, Date, Integer, String

from app.database import Base


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, index=True)
    description = Column(String, nullable=True)
    due = Column(Date, nullable=False)
    completed = Column(Boolean, default=False, nullable=False)
