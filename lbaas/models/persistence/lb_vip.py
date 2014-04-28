from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table, \
    Boolean
from sqlalchemy.orm import relationship

from lbaas.models.persistence import base


class LbVipModel(base.Base, base.BaseModel):
    __tablename__ = 'lb_vip'
    __table_args__ = {"useexisting": True}

    TAG = 'lb_vip'

    lb_id = Column(Integer, ForeignKey('load_balancer.id'))
    load_balancer = relationship("LoadbalancerModel", backref=backref("lb_vip", uselist=False))
    vip_id = Column(Integer, ForeignKey('vip.id'))
    vip = relationship("VipModel", backref=backref("lb_vip", uselist=False))

    def __init__(self, load_balancer=None, vip=None):
        self.load_balancer = load_balancer
        self.vip = vip

    def to_dict(self):
        lv_dict = {'lb_id': self.lb_id, 'vip_id': self.vip_id}
        return lv_dict

    def __repr__(self):
        return '<LbVip %r>' % self.name
