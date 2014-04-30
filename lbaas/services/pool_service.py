from lbaas.services.base import BaseService


class PoolService(BaseService):

    def get(self, tenant_id, pool_id):
        pool = self.pool_persistence.pool.get(tenant_id, pool_id)
        return pool

    def get_all(self, tenant_id):
        pools = self.pool_persistence.pool.get_all(tenant_id)
        return pools

    def create(self):
        pass


class PoolServiceOps(object):
    def __init__(self):
        self.pool_service = PoolService()