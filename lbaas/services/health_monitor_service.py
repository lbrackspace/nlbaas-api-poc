from lbaas.services.base import BaseService
from lbaas.models.persistence.health_monitor import HealthMonitorModel


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

    def update(self, tenant_id, pool_id, monitor):
        updated_hm = self.get(tenant_id, pool_id)
        updated_hm.host_header = monitor.get('host_header')
        updated_hm.path = monitor.get('path')
        updated_hm.body_regex = monitor.get('body_regex')
        updated_hm.status_regex = monitor.get('status_regex')
        updated_hm.delay = monitor.get('delay')
        updated_hm.timeout = monitor.get('timeout')
        updated_hm.attempts_before_deactivation = monitor.get(
            'attempts_before_deactivation')
        updated_hm.type = monitor.get('type')
        updated_hm = self.monitor_persistence.monitor.update(updated_hm)
        return updated_hm

    def delete(self, tenant_id, pool_id):
        pool = self.pool_persistence.pool.get(tenant_id, pool_id)
        pool.health_monitor_id = None
        self.pool_persistence.pool.update(pool)
        hm = self.get(tenant_id, pool_id)
        return self.monitor_persistence.monitor.delete(hm)

    class HealthMonitorServiceOps(object):
        def __init__(self):
            self.monitor_service = HealthMonitorService()