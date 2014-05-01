from lbaas.models.persistence import base, pool
from lbaas.persistence.base import BaseService


class PoolPersistence(BaseService):

    def get(self, tenant_id, pool_id):
        ret_pool = pool.PoolModel.query.filter_by(tenant_id=tenant_id,
                                                  id_=pool_id).first()
        return ret_pool

    def get_all(self, tenant_id):
        pools = pool.PoolModel.query.filter_by(tenant_id=tenant_id).all()
        return pools

    def create(self, pool_model):
        base.db.session.add(pool_model)
        base.db.session.commit()
        return pool_model

    def update(self, pool_model):
        base.db.session.add(pool_model)
        base.db.session.commit()
        return pool_model

    def delete(self):
        pass


class PoolPersistenceOps(object):
    def __init__(self):
        self.pool = PoolPersistence(self)