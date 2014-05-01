from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table, \
    Boolean
from sqlalchemy.orm import relationship, backref
from lbaas.models.persistence.ssl_decrypt import SslDecryptModel
from lbaas.models.persistence.pool import PoolModel

from lbaas.models.persistence import base


class LoadbalancerModel(base.Base, base.BaseModel):
    __tablename__ = 'load_balancer'
    __table_args__ = {"useexisting": True}

    TAG = 'load_balancer'

    id_ = Column('id', Integer, primary_key=True)
    tenant_id = Column(Integer(32))
    pool_id = Column(Integer, ForeignKey('pool.id'))
    pool = relationship("PoolModel")
    ssl_decrypt_id = Column(Integer, ForeignKey('ssl_decrypt.id'))
    ssl_decrypt = relationship("SslDecryptModel",backref=backref("load_balancer", uselist=False))
    name = Column(String(128))
    content_switching = Column(Boolean(128))
    port = Column(String(32))
    protocol = Column(Integer(32))
    status = Column(Integer(32))

    def __init__(self, tenant_id=None, pool=None, ssl_decrypt=None, name=None,
                 content_switching=False, port=None, protocol=None,
                 status=None):
        self.tenant_id = tenant_id
        self.pool = pool
        self.ssl_decrypt = ssl_decrypt
        self.name = name
        self.content_switching = content_switching
        self.port = port
        self.protocol = protocol
        self.status = status

    def to_dict(self):
        lb_dict = {'id': self.id_, 'name': self.name}
        return lb_dict

    def __repr__(self):
        return '<LB %r>' % self.name
