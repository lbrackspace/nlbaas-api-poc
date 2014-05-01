from lbaas.services.base import BaseService
from lbaas.models.persistence.pool import PoolModel
from lbaas.models.persistence.health_monitor import HealthMonitorModel
from lbaas.models.persistence.member import MemberModel


class PoolService(BaseService):

    def get(self, tenant_id, pool_id):
        pool = self.pool_persistence.pool.get(tenant_id, pool_id)
        return pool

    def get_all(self, tenant_id):
        pools = self.pool_persistence.pool.get_all(tenant_id)
        return pools

    def create(self, tenant_id, pool):
        created_hm = None
        created_members = None
        if 'health_monitor' in pool:
            hm = pool.get('health_monitor')
            created_hm = HealthMonitorModel(
                type=hm.get('type'),
                delay=hm.get('delay'),
                timeout=hm.get('timeout'),
                attempts_before_deactivation=hm.get(
                    'attempts_before_deactivation'),
                status_regex=hm.get('status_regex'),
                body_regex=hm.get('body_regex'),
                host_header=hm.get('host_header'),
                path=hm.get('path'))
        if 'members' in pool:
            created_members = []
            for member in pool.get('members'):
                created_members.append(MemberModel(
                    ip=member.get('ip'),
                    port=member.get('port'),
                    weight=member.get('weight'),
                    condition=member.get('condition')))

        if 'ssl_encrypt' in pool:
            pass
        created_pool = PoolModel(
            tenant_id=tenant_id,
            health_monitor=created_hm,
            name=pool.get('name'),
            subnet_id=pool.get('subnet_id'),
            algorithm=pool.get('algorithm'),
            session_persistence=pool.get('session_persistence'),
            members=created_members)
        created_pool = self.pool_persistence.pool.create(created_pool)
        return created_pool

    def update(self, tenant_id, pool_id, pool):
        updated_pool = self.pool_persistence.pool.get(tenant_id, pool_id)
        updated_pool.name = pool.get('name')
        updated_pool.subnet_id = pool.get('subnet_id')
        updated_pool.algorithm = pool.get('algorithm')
        updated_pool.session_persistence = pool.get('session_persistence')
        updated_pool = self.pool_persistence.pool.create(updated_pool)
        return updated_pool

    def delete(self, tenant_id, pool_id):
        pool = self.get(tenant_id, pool_id)
        return self.pool_persistence.pool.delete(tenant_id, pool)


class PoolServiceOps(object):
    def __init__(self):
        self.pool_service = PoolService()