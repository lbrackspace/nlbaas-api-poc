from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table, \
    Boolean
from sqlalchemy.orm import relationship, backref

from lbaas.models.persistence import base


class LbL7PolicyModel(base.Base, base.BaseModel):
    __tablename__ = 'lb_l7_policy'
    __table_args__ = {"useexisting": True}

    TAG = 'lb_l7_policy'

    id_ = Column('id', Integer, primary_key=True)
    lb_id = Column(Integer, ForeignKey('load_balancer.id'))
    load_balancer = relationship("LoadbalancerModel", backref=backref("lb_l7_policy", uselist=False))
    pool_id = Column(Integer, ForeignKey('pool.id'))
    pool = relationship("PoolModel", backref=backref("lb_l7_policy"))
    condition = Column(String(32))
    type = Column(String(32))

    def __init__(self, load_balancer=None, pool=None, condition=None, type=None):
        self.load_balancer = load_balancer
        self.pool = pool
        self.condition = condition
        self.type = type

    def __repr__(self):
        return '<Lbl7Policy %r>' % self.type
