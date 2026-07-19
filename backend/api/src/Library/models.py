from api.core.db import Base
from sqlalchemy import Integer, Column, String, Text, Boolean, Date

class Library(Base):
    """Library model for database.

    Attributes:
        id: Unique identifier
        title: Name of the link
        url: Link to that library item
        category: Category like audio, video, article, post
        sub_category: Category like python, motivation, studying, physical gitness
        watched: bool
        summary: A paragraph about what it is.
        date_created: The date the object was added.
    """

    __tablename__ = "Library"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), index=True)
    url = Column(String, nullable=False)
    category = Column(String, nullable=False, index=True)
    sub_category = Column(String, nullable=False, index=True)
    watched = Column(Boolean, index=True)
    summary = Column(Text, index=True)
    date_created = Column(Date, index=True)
