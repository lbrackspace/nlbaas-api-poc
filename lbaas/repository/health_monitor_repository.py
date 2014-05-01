from lbaas.models.persistence import base
from lbaas.models.persistence import health_monitor
from lbaas.models.persistence import pool
from lbaas.repository.base import BaseService


class HealthMonitorRepository(BaseService):
    def get(self, pool_id):
        monitor_pool = pool.PoolModel.query.filter_by(id_=pool_id).first()
        return monitor_pool.health_monitor

    def create(self, monitor):
        base.db.session.add(monitor)
        base.db.session.commit()
        return monitor

    def update(self, tenant_id, pool_id, json_monitor):
        pass

    def delete(self):
        pass

class HealthMonitorRepositoryOps(object):
    def __init__(self):
        self.monitor = HealthMonitorRepository(self)
