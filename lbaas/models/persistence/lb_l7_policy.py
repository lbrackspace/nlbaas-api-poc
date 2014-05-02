from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table, \
    Boolean
from sqlalchemy.orm import relationship, backref

from lbaas.models.persistence import base

from lbaas.models.persistence.pool import PoolModel

class LbL7PolicyModel(base.Base, base.BaseModel):
    __tablename__ = 'lb_l7_policy'
    __table_args__ = {"useexisting": True}

    TAG = 'lb_l7_policy'

    id_ = Column('id', Integer, primary_key=True)
    enabled = Column(Boolean(128))
    lb_id = Column(Integer, ForeignKey('load_balancer.id'))
    pools = relationship("PoolModel")
    condition = Column(String(32))
    type = Column(String(32))

    _child_classes = (PoolModel)

    def __init__(self, enabled=False, lb_id=None, pools=[], condition=None,
                 type=None):
        self.enabled = enabled
        self.lb_id = lb_id
        self.pools = pools
        self.condition = condition
        self.type = type

    def __repr__(self):
        return '<Lbl7Policy %r>' % self.type
