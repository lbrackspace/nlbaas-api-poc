from lbaas.services.base import BaseService


class HealthMonitorService(BaseService):

    def get(self, tenant_id, pool_id):
        monitor = self.monitor_persistence.monitor.get(pool_id)
        return monitor

    def get_all(self):
        pass

# type, status_regex, body_regex, delay, timeout, attempts, path, host_header
    def create(self, tenant_id, pool_id, health_monitor):
        monitor = self.monitor_persistence.monitor.create(
            tenant_id, health_monitor)
        self.pool_persistence.pool.update(
            tenant_id, pool_id, {'pool': {'health_monitor_id': monitor.id_}})
        return monitor

    class HealthMonitorServiceOps(object):
        def __init__(self):
            self.monitor_service = HealthMonitorService()