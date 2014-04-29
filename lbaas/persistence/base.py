from lbaas.models.persistence.load_balancer import LoadbalancerModel
from lbaas.models.persistence import base


class BaseService(object):
    def __init__(self, operations):
        #Set up model services here ex:
        LoadbalancerModel.query = base.db.session.query_property()