from flask.ext.restful import Resource
from lbaas.persistence.health_monitor_persistence \
    import HealthMonitorPersistenceOps
from lbaas.persistence.load_balancer_persistence \
import LoadbalancerPersistenceOps
from lbaas.persistence.pool_persistence import PoolPersistenceOps


class BaseService(Resource):
    def __init__(self):
        #Init persistence classes here ex:
        self.lb_persistence = LoadbalancerPersistenceOps()
        self.monitor_persistence = HealthMonitorPersistenceOps()
        self.pool_persistence = PoolPersistenceOps()