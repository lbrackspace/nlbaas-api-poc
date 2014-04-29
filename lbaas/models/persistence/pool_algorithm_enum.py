from sqlalchemy import Column, Integer, String

from lbaas.models.persistence import base


class lbStatusEnumModel(base.Base, base.BaseModel):
    __tablename__ = 'pool_algorithm_enum'
    __table_args__ = {"useexisting": True}

    TAG = 'pool_algorithm_enum'

    id_ = Column('id', Integer, primary_key=True)
    name = Column(String(32))
    description = Column(String(128))

    def __init__(self, name=None, description=None):
        self.name = name
        self.description = description

    def to_dict(self):
        stat_dict = {'id': self.id_, 'name': self.name,
                     'description': self.description}
        return stat_dict

    def __repr__(self):
        return '<PoolAlgorithmEnum %r>' % self.name
