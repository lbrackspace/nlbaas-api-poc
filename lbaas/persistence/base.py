from lbaas.models.persistence import load_balancer


class BaseService(object):
    def __init__(self, operations):
        #Set up model services here ex:
        load_balancer.LoadbalancerModel.query = base.db.session.query_property()