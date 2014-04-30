from lbaas.models.persistence import base, load_balancer, health_monitor, \
    pool, member


class BaseService(object):
    def __init__(self, operations):
        #Set up model services here...
        load_balancer.LoadbalancerModel.query = \
            base.db.session.query_property()
        health_monitor.HealthMonitorModel.query = \
            base.db.session.query_property()
        pool.PoolModel.query = base.db.session.query_property()
        member.MemberModel.query = base.db.session.query_property()