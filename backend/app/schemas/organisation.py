from email.policy import default
from sqlalchemy import Column, ForeignKey, Boolean, Float, Integer, String, Date, func, or_, and_
from sqlalchemy.orm import relationship, object_session
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.hybrid import hybrid_property
import datetime as dt

from sqlalchemy.sql.sqltypes import VARCHAR

from app import utils
from app.db.base import Base
from enum import IntEnum

class Organisation(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    address = Column(String)
    city = Column(String)
    state = Column(String)
    country = Column(String)
    postcode = Column(String)
    phone = Column(String)
    email = Column(String, nullable=False)
    website = Column(String)
    active = Column(Boolean, default=True)
    sqlite_autoincrement=True