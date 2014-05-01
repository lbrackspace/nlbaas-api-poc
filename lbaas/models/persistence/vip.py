from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table, \
    Boolean
from sqlalchemy.orm import relationship

from lbaas.models.persistence import base


class VipModel(base.Base, base.BaseModel):
    __tablename__ = 'vip'
    __table_args__ = {"useexisting": True}

    TAG = 'vip'

    id_ = Column('id', Integer, primary_key=True)
    tenant_id = Column(Integer(32))
    subnet_id = Column(String(32))
    type = Column(Integer(32))
    address = Column(String(32))

    def __init__(self, tenant_id=None, subnet_id=None, type=None,
                 address=None):
        self.tenant_id = tenant_id
        self.subnet_id = subnet_id
        self.type = type
        self.address = address

    #def to_dict(self):
    #    vip_dict = {'id': self.id_, 'name': self.type}
    #    return vip_dict

    def __repr__(self):
        return '<Vip %r>' % self.type
