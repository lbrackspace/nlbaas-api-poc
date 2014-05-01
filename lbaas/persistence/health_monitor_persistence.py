from lbaas.models.persistence import base
from lbaas.models.persistence import health_monitor
from lbaas.models.persistence import pool
from lbaas.persistence.base import BaseService


class HealthMonitorPersistence(BaseService):
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

class HealthMonitorPersistenceOps(object):
    def __init__(self):
        self.monitor = HealthMonitorPersistence(self)
