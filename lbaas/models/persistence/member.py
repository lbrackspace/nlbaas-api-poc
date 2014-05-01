from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table, \
    Boolean
from sqlalchemy.orm import relationship, backref

from lbaas.models.persistence import base


class MemberModel(base.Base, base.BaseModel):
    __tablename__ = 'member'
    __table_args__ = {"useexisting": True}

    TAG = 'member'

    id_ = Column('id', Integer, primary_key=True)
    pool_id = Column(Integer, ForeignKey('pool.id'))
    ip = Column(String(128))
    port = Column(Integer(32))
    weight = Column(Integer(32))
    status = Column(String(32))
    condition = Column(String(32))

    def __init__(self, pool_id=None, ip=None, port=None, weight=None,
                 status=None, condition=None):
        self.pool_id = pool_id
        self.ip = ip
        self.port = port
        self.weight = weight
        self.status = status
        self.condition = condition

    def to_dict(self):
        m_dict = {'id': self.id_, 'ip': self.ip}
        return m_dict

    def __repr__(self):
        return '<Member %r>' % self.ip
