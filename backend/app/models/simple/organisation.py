from app import schemas
from .base import Base
from typing import List
from .employee import Employee

class Organisation(Base):
    id : int = None
    name : str = None
    address : str = None
    city : str = None
    state : str = None
    country : str = None
    postcode : str = None
    phone : str = None
    email : str = None
    website : str = None
    active : bool = None
    retainer : float = None
    