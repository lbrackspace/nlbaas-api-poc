import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table, \
    Boolean
from sqlalchemy.orm import relationship, backref

from lbaas.models.persistence import base


class SslSniDecryptPolicy(base.Base, base.BaseModel):
    __tablename__ = 'ssl_sni_decrypt_policy'
    __table_args__ = {"useexisting": True}

    TAG = 'ssl_sni_decrypt_policy'

    id_ = Column('id', Integer, primary_key=True)
    enabled = Column(Boolean())
    sni_match = Column(String(128))
    ssl_decrypt_id = Column(Integer, ForeignKey('ssl_decrypt.id'))
    ssl_decrypt = relationship("SslDecryptModel", backref=backref("ssl_sni_decrypt_policy", uselist=False))
    tls_certificate_id = Column(Integer, ForeignKey('tls_certificate.id'))
    tls_certificate = relationship("TlsCertificateModel", backref=backref("ssl_sni_decrypt_policy", uselist=False))

    def __init__(self, tenant_id=None, enabled=False, sni_match=None,
                 ssl_decrypt=None, tls_certificate=None):
        self.tenant_id = tenant_id
        self.enabled = enabled
        self.sni_match = sni_match
        self.ssl_decrypt = ssl_decrypt
        self.tls_certificate = tls_certificate

    def to_dict(self):
        ssl_dict = {'id': self.id_, 'enabled': self.enabled}
        return ssl_dict

    def __repr__(self):
        return '<SSLSniDecryptPolicy %r>' % self.enabled
