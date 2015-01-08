from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import create_engine

Base = declarative_base()


class LogModel(Base):
    """
    """
    __tablename__ = "fixers"

    id = Column(Integer, primary_key=True)
    logger = Column(String(25))
    level = Column(String(15))
    trace = Column(String(64))
    message = Column(String(128))
    created_at = Column(DateTime, default=func.now())

    def __init__(self, logger=None, level=None, trace=None, message=None):

        self.logger = logger
        self.level = level
        self.trace = trace
        self.message = message

    def __unicode__(self,):
        return self.__repr__()

    def __repr__(self):
        return "<Log: %s - %s>" % (self.created_at.strftime('%m/%d/%Y-%H:%M:%S'), self.msg[:50])
