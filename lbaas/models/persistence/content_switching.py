from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table, \
    Boolean
from sqlalchemy.orm import relationship, backref

from lbaas.models.persistence import base

from lbaas.models.persistence.pool import PoolModel

class ContentSwitchingModel(base.Base, base.BaseModel):
    __tablename__ = 'content_switching'
    __table_args__ = {"useexisting": True}

    TAG = 'content_switching'

    id_ = Column('id', Integer, primary_key=True)
    enabled = Column(Boolean(128))
    lb_id = Column(Integer, ForeignKey('load_balancer.id'))
    pools = relationship("PoolModel")
    match = Column(String(32))
    type_ = Column('type', String(32))

    _child_classes = (PoolModel)

    def __init__(self, enabled=False, lb_id=None, pools=[], match=None,
                 type_=None):
        self.enabled = enabled
        self.lb_id = lb_id
        self.pools = pools
        self.match = match
        self.type_ = type_

    def __repr__(self):
        return '<ContentSwitchingPolicy %r>' % self.enabled
