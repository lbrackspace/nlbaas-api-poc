from lbaas.models.persistence import base, load_balancer, health_monitor, \
    pool, member, vip, content_switching


class BaseService(object):
    def __init__(self, operations):
        #Set up model services here...
        load_balancer.LoadbalancerModel.query = \
            base.db.session.query_property()
        health_monitor.HealthMonitorModel.query = \
            base.db.session.query_property()
        pool.PoolModel.query = base.db.session.query_property()
        member.MemberModel.query = base.db.session.query_property()
        vip.VipModel.query = base.db.session.query_property()
        content_switching.ContentSwitchingModel.query = \
            base.db.session.query_property()