from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKey, Integer, String

from ..db.database import Base, BaseModel

class Schedule(Base, BaseModel):
    __tablename__ = "schedules"

    week_day = Column('week_day', Integer, nullable=False) # 0 = Sunday, 1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday
    date = Column(Date, nullable=False)
    start_at = Column(DateTime, nullable=False)
    finish_at = Column(DateTime, nullable=False)
