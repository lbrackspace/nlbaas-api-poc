from lbaas.services.base import BaseService


class HealthMonitorService(BaseService):

    def get(self, tenant_id, pool_id):
        monitor = self.monitor_persistence.monitor.get(pool_id)
        return monitor

    def get_all(self):
        pass

# type, status_regex, body_regex, delay, timeout, attempts, path, host_header
    def create(self, account_id, pool_id, health_monitor):
        monitor = self.monitor_persistence.monitor.create(
            account_id, pool_id, health_monitor.get('host_header'),
            health_monitor.get('status_regex'), health_monitor.get('path'),
            health_monitor.get('body_regex'), health_monitor.get('delay'),
            health_monitor.get('timeout'), health_monitor.get('attempts'),
            health_monitor.get('type'))
        return monitor

    class HealthMonitorServiceOps(object):
        def __init__(self):
            self.monitor_service = HealthMonitorService()