from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table, \
    Boolean
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.associationproxy import association_proxy
from lbaas.models.persistence.ssl_decrypt import SslDecryptModel
from lbaas.models.persistence.pool import PoolModel
from lbaas.models.persistence.vip import VipModel
from lbaas.models.persistence.content_switching \
    import ContentSwitchingModel

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
    ssl_decrypt = relationship("SslDecryptModel",
                               backref=backref("load_balancer", uselist=False))
    vips = relationship("VipModel", secondary=lambda: lb_vip_table)
    vips_ass = association_proxy('vips', 'vip')
    name = Column(String(128))
    port = Column(String(32))
    protocol = Column(Integer(32))
    status = Column(Integer(32))
    content_switching = relationship("ContentSwitchingModel",
                                            uselist=False,
                                            backref="load_balancer")

    _child_classes = (
        PoolModel, SslDecryptModel, VipModel, ContentSwitchingModel)

    def __init__(self, tenant_id=None, pool=None, ssl_decrypt=None, vips=None,
                 name=None, port=None, protocol=None, status=None,
                 content_switching=None):
        self.tenant_id = tenant_id
        self.pool = pool
        self.ssl_decrypt = ssl_decrypt
        self.vips = vips
        self.name = name
        self.port = port
        self.protocol = protocol
        self.status = status
        self.content_switching = content_switching

    #def to_dict(self):
    #    lb_dict = {'id': self.id_, 'name': self.name}
    #    return lb_dict

    def __repr__(self):
        return '<LB %r>' % self.name


lb_vip_table = Table('lb_vip', base.Base.metadata,
                     Column('lb_id', Integer, ForeignKey("load_balancer.id"),
                            primary_key=True),
                     Column('vip_id', Integer, ForeignKey("vip.id"),
                            primary_key=True)
)
