from lbaas.models.persistence import base, pool
from lbaas.persistence.base import BaseService


class PoolPersistence(BaseService):
    def get_all(self, tenant_id):
        pools = pool.PoolModel.query.filter_by(tenant_id=tenant_id).all()
        return pools

    def create(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass


class PoolPersistenceOps(object):
    def __init__(self):
        self.pool = PoolPersistence(self)