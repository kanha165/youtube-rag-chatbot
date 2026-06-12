from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    TIMESTAMP
)

from sqlalchemy.sql import func
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Session(Base):

    __tablename__ = "sessions"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    session_id = Column(
        String(255),
        unique=True,
        nullable=False
    )

    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )


class Video(Base):

    __tablename__ = "videos"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    session_id = Column(
        String(255),
        nullable=False
    )

    video_id = Column(
        String(100),
        nullable=False
    )

    video_url = Column(
        Text,
        nullable=False
    )

    title = Column(
        String(500)
    )

    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )


class Chat(Base):

    __tablename__ = "chats"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    session_id = Column(
        String(255),
        nullable=False
    )

    video_id = Column(
        String(100),
        nullable=False
    )

    question = Column(
        Text,
        nullable=False
    )

    answer = Column(
        Text,
        nullable=False
    )

    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )