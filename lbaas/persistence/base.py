from lbaas.models.persistence import base, load_balancer, health_monitor


class BaseService(object):
    def __init__(self, operations):
        #Set up model services here...
        load_balancer.LoadbalancerModel.query = \
            base.db.session.query_property()
        health_monitor.HealthMonitorModel.query = \
            base.db.session.query_property()
