import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table, \
    Boolean
from sqlalchemy.orm import relationship

from lb.models.persistence import base


class LoadbalancerModel(base.Base, base.BaseModel):
    __tablename__ = 'load_balancer'
    __table_args__ = {"useexisting": True}

    TAG = 'load_balancer'

    id_ = Column('id', Integer, primary_key=True)
    tenant_id = Column(Integer(32))
    ssl_decrypt_id = Column(Integer, ForeignKey('ssl_decrypt.id'))
    ssl_decrypt = relationship("SslDecryptModel", backref=backref("load_balancer", uselist=False))
    tls_certificate_id = Column(Integer, ForeignKey('ssl_decrypt.id'))
    tls_certificate = relationship("TlsCertificateModel", backref=backref("load_balancer", uselist=False))
    name = Column(String(128))
    content_switching = Column(Boolean(128))
    port = Column(String(32))
    protocol = Column(Integer(32))
    status = Column(Integer(32))

    def __init__(self, tenant_id=None, ssl_decrypt_id=None,
                 tls_certificate_id=None, name=None, content_switching=False,
                 port=None, protocol=None, status=None):
        self.tenant_id = tenant_id
        self.ssl_decrypt_id = ssl_decrypt_id
        self.tls_certificate_id = tls_certificate_id
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
