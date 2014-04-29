from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table, \
    Boolean
from sqlalchemy.orm import relationship

from lbaas.models.persistence import base


class HealthMonitorModel(base.Base, base.BaseModel):
    __tablename__ = 'health_monitor'
    __table_args__ = {"useexisting": True}

    TAG = 'health_monitor'

    id_ = Column('id', Integer, primary_key=True)
    type = Column(String(32))
    delay = Column(Integer(32))
    timeout = Column(Integer(32))
    attempts_before_deactivation = Column(Integer(32))
    status_regex = Column(String(32))
    body_regex = Column(String(32))
    host_header = Column(String(32))
    path = Column(String(32))

    def __init__(self, type=None, delay=None, timeout=None,
                 attempts_before_deactivation=None, status_regex=None,
                 body_regex=None, host_header=None, path=path):
        self.type = type
        self.delay = delay
        self.timeout = timeout
        self.attempts_before_deactivation = attempts_before_deactivation
        self.status_regex = status_regex
        self.body_regex = body_regex
        self.host_header = host_header
        self.path = path

    def to_dict(self):
        hm_dict = {'id': self.id_, 'type': self.type}
        return hm_dict

    def __repr__(self):
        return '<HealthMonitor %r>' % self.type