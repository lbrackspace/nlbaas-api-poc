from lbaas.services.base import BaseService
from lbaas.models.persistence.health_monitor import HealthMonitorModel
from lbaas.models.persistence.pool import PoolModel


class HealthMonitorService(BaseService):

    def get(self, tenant_id, pool_id):
        monitor = self.monitor_persistence.monitor.get(pool_id)
        return monitor

    def get_all(self):
        pass

    def create(self, tenant_id, pool_id, monitor):
        created_monitor = HealthMonitorModel(
            host_header=monitor.get('host_header'),
            path=monitor.get('path'),
            body_regex=monitor.get('body_regex'),
            status_regex=monitor.get('status_regex'),
            delay=monitor.get('delay'),
            timeout=monitor.get('timeout'),
            attempts_before_deactivation=monitor.get(
                'attempts_before_deactivation'),
            type=monitor.get('type'))
        monitor = self.monitor_persistence.monitor.create(created_monitor)
        updated_pool = self.pool_persistence.pool.get(tenant_id, pool_id)
        updated_pool.health_monitor = created_monitor
        self.pool_persistence.pool.update(updated_pool)
        return monitor

    class HealthMonitorServiceOps(object):
        def __init__(self):
            self.monitor_service = HealthMonitorService()