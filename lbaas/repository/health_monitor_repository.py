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

    def update(self, hm_model):
        base.db.session.add(hm_model)
        base.db.session.commit()
        return hm_model

    def delete(self, hm_model):
        base.db.session.delete(hm_model)
        base.db.session.commit()
        return hm_model

class HealthMonitorRepositoryOps(object):
    def __init__(self):
        self.monitor = HealthMonitorRepository(self)
