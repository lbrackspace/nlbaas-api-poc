from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy.orm import backref
from sqlalchemy.orm import relationship
from lbaas.models.persistence import base
from lbaas.models.persistence.health_monitor import HealthMonitorModel
from lbaas.models.persistence.ssl_encrypt import SslEncryptModel


class PoolModel(base.Base, base.BaseModel):
    __tablename__ = 'pool'
    __table_args__ = {"useexisting": True}

    TAG = 'pool'

    id_ = Column('id', Integer, primary_key=True)
    tenant_id = Column(Integer(32))
    health_monitor_id = Column(Integer, ForeignKey('health_monitor.id'))
    health_monitor = relationship("HealthMonitorModel")
    ssl_encrypt_id = Column(Integer, ForeignKey('ssl_encrypt.id'))
    ssl_encrypt = relationship("SslEncryptModel",
                               backref=backref("pool", uselist=False))
    name = Column(String(128))
    subnet_id = Column(Integer(32))
    algorithm = Column(String(32))
    session_persistence = Column(Integer(32))

    _child_classes = (HealthMonitorModel)

    def __init__(self, tenant_id=None, ssl_encrypt=None,
                 health_monitor=None, name=None, subnet_id=False,
                 algorithm=None, session_persistence=None):
        self.tenant_id = tenant_id
        self.ssl_encrypt = ssl_encrypt
        self.health_monitor = health_monitor
        self.name = name
        self.subnet_id = subnet_id
        self.algorithm = algorithm
        self.session_persistence = session_persistence

    def __repr__(self):
        return '<Pool %r>' % self.name
