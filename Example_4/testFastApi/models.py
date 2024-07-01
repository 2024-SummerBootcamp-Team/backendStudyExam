from sqlalchemy import Column, Integer, String, Text, DateTime
from database import Base
import datetime


class TeamHMember(Base):
    __tablename__ = 'members'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    text = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
