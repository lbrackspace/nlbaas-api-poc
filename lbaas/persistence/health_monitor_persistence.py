from lbaas.models.persistence import health_monitor
from lbaas.persistence.base import BaseService


class HealthMonitorPersistence(BaseService):
    def get(self):
        pass

    def create(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

class HealthMonitorPersistenceOps(object):
    def __init__(self):
        self.monitor_persistence = HealthMonitorPersistence(self)