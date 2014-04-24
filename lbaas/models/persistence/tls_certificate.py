import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table, \
    Boolean
from sqlalchemy.orm import relationship

from lbaas.models.persistence import base


class TlsCertificateModel(base.Base, base.BaseModel):
    __tablename__ = 'tls_certificate'
    __table_args__ = {"useexisting": True}

    TAG = 'tls_certificate'

    id_ = Column('id', Integer, primary_key=True)
    tenant_id = Column(Integer(32))
    barbican_uuid = Column(String(128))
    simple_certificate_data = Column(String(256))

    def __init__(self, tenant_id=None, enabled=False,
                 barbican_uuid=None, simple_certificate_data=None):
        self.tenant_id = tenant_id
        self.enabled = enabled
        self.barbican_uuid = barbican_uuid
        self.simple_certificate_data = simple_certificate_data

    def to_dict(self):
        tls_dict = {'id': self.id_,
                   'simple_certificate_data': self.simple_certificate_data}
        return tls_dict

    def __repr__(self):
        return '<TlsCertificate %r>' % self.simple_certificate_data
