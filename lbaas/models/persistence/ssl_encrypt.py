import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table, \
    Boolean
from sqlalchemy.orm import relationship, backref

from lbaas.models.persistence import base


class SslEncryptModel(base.Base, base.BaseModel):
    __tablename__ = 'ssl_encrypt'
    __table_args__ = {"useexisting": True}

    TAG = 'ssl_encrypt'

    id_ = Column('id', Integer, primary_key=True)
    tenant_id = Column(Integer(32))
    enabled = Column(Boolean())
    tls_certificate_id = Column(Integer, ForeignKey('ssl_encrypt.id'))
    tls_certificate = relationship("TlsCertificateModel", backref=backref("ssl_encrypt", uselist=False))

    def __init__(self, tenant_id=None, enabled=False,
                 tls_certificate=None):
        self.tenant_id = tenant_id
        self.enabled = enabled
        self.tls_certificate = tls_certificate

    def to_dict(self):
        ssl_dict = {'id': self.id_, 'enabled': self.enabled}
        return ssl_dict

    def __repr__(self):
        return '<SSLEncrypt %r>' % self.enabled
