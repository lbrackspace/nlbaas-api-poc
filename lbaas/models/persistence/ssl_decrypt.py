import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table, \
    Boolean
from sqlalchemy.orm import relationship

from lbaas.models.persistence import base


class SslDecryptModel(base.Base, base.BaseModel):
    __tablename__ = 'ssl_decrypt'
    __table_args__ = {"useexisting": True}

    TAG = 'ssl_decrypt'

    id_ = Column('id', Integer, primary_key=True)
    tenant_id = Column(Integer(32))
    enabled = Column(Boolean(128))
    barbican_uuid = Column(String(128))


    def __init__(self, tenant_id=None, enabled=False,
                 barbican_uuid=None):
        self.tenant_id = tenant_id
        self.enabled = enabled
        self.barbican_uuid = barbican_uuid

    def to_dict(self):
        ssl_dict = {'id': self.id_, 'enabled': self.enabled}
        return ssl_dict

    def __repr__(self):
        return '<SSLDecrypt %r>' % self.enabled
