from lbaas.models.persistence import health_monitor
from lbaas.persistence.base import BaseService


class HealthMonitorPersistence(BaseService):
    def get(self):
        pass

    def create(self, tenant_id, pool_id, monitor):
        ##Do the stuffs here:
        #account_id, pool_id, health_monitor.get('host_header'),
        #    health_monitor.get('status_regex'), health_monitor.get('path'),
        #    health_monitor.get('body_regex'), health_monitor.get('delay'),
        #    health_monitor.get('timeout'), health_monitor.get('attempts'),
        #    health_monitor.get('type')
        pass

    def update(self):
        pass

    def delete(self):
        pass