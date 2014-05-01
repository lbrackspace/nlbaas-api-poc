from lbaas.models.persistence import base
from lbaas.models.persistence import health_monitor
from lbaas.models.persistence import pool
from lbaas.persistence.base import BaseService


class HealthMonitorPersistence(BaseService):
    def get(self, pool_id):
        monitor_pool = pool.PoolModel.query.filter_by(id_=pool_id).first()
        return monitor_pool.health_monitor

    def create(self, tenant_id, pool_id, json_monitor):
        monitor = health_monitor.HealthMonitorModel(
            json_monitor.get('host_header'), json_monitor.get('status_regex'),
            json_monitor.get('path'), json_monitor.get('body_regex'),
            json_monitor.get('delay'), json_monitor.get('timeout'),
            json_monitor.get('attempts'), json_monitor.get('type'))
        base.db.session.add(monitor)
        base.db.session.commit()
        return monitor

    def update(self, tenant_id, pool_id, json_monitor):
        monitor = health_monitor.HealthMonitorModel.query(
            id_=json_monitor.id_).first()
        pass

    def delete(self):
        pass

class HealthMonitorPersistenceOps(object):
    def __init__(self):
        self.monitor = HealthMonitorPersistence(self)
