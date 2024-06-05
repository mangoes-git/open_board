from sqlalchemy import Boolean, Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    usename = Column(String, unique=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)

    messages = relationship("Messages")


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True)
    author_id = Column(
        Integer,
        ForeignKey("users.id"),
    )
    reply_to = Column(
        Integer,
        ForeignKey("messages.id"),
    )
    content = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
