from flask.ext.restful import Resource
from lbaas.persistence.health_monitor_persistence \
    import HealthMonitorPersistenceOps
# Import persistence classes EX: from lbaas.persistence.lb_persistence import LbPersistenceOps


class BaseService(Resource):
    def __init__(self):
        #Init persistence classes here ex:
        #self.lbpersistence = LbPersistenceOps()
        self.monitorpersistence = HealthMonitorPersistenceOps()