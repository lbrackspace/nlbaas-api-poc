from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table, \
    Boolean
from sqlalchemy.orm import relationship, backref

from lbaas.models.persistence.load_balancer import LoadbalancerModel
from lbaas.models.persistence.vip import VipModel

from lbaas.models.persistence import base


class LbVipModel(base.Base, base.BaseModel):
    __tablename__ = 'lb_vip'
    __table_args__ = {"useexisting": True}

    TAG = 'lb_vip'

    id_ = Column('id', Integer, primary_key=True)
    lb_id = Column(Integer, ForeignKey('load_balancer.id'))
    vip_id = Column(Integer, ForeignKey('vip.id'))

    load_balancer = relationship(LoadbalancerModel)
    vip = relationship("VipModel")

    def __init__(self, load_balancer=None, vip=None):
        self.load_balancer = load_balancer
        self.vip = vip

    def to_dict(self):
        lv_dict = {'lb_id': self.lb_id, 'vip_id': self.vip_id}
        return lv_dict

    def __repr__(self):
        return '<LbVip %r>' % self.name
