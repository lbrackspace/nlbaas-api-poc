from lbaas.models.persistence import base
from lbaas.models.persistence import health_monitor
from lbaas.models.persistence import pool
from lbaas.persistence.base import BaseService


class HealthMonitorPersistence(BaseService):
    def get(self, pool_id):
        monitor_pool = pool.PoolModel.query.filter_by(id_=pool_id).first()
        return monitor_pool.health_monitor

    def create(self, monitor):
        created_monitor = health_monitor.HealthMonitorModel(
            host_header=monitor.get('host_header'),
            path=monitor.get('path'),
            body_regex=monitor.get('body_regex'),
            status_regex=monitor.get('status_regex'),
            delay=monitor.get('delay'),
            timeout=monitor.get('timeout'),
            attempts=monitor.get('attempts'),
            type=monitor.get('type'))
        base.db.session.add(created_monitor)
        base.db.session.commit()
        return created_monitor

    def update(self, tenant_id, pool_id, json_monitor):
        pass

    def delete(self):
        pass

class HealthMonitorPersistenceOps(object):
    def __init__(self):
        self.monitor = HealthMonitorPersistence(self)
