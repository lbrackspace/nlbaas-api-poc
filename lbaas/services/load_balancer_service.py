from lbaas.services.base import BaseService

class LoadbalancerService(BaseService):

    def get_all(self, tenant_id):
        lbs = self.lb_persistence.loadbalancer.get_all(tenant_id)
        return lbs

    def create(self):
        pass


class LoadbalancerServiceOps(object):
    def __init__(self):
        self.lb_service = LoadbalancerService()