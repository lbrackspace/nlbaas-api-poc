from lbaas.services.base import BaseService


class LoadbalancersService(BaseService):

    def get_all(self, tenant_id):
        self._validate_all_resources_exist(tenant_id=tenant_id)
        lbs = self.lb_persistence.loadbalancer.get_all(tenant_id)
        return lbs

    def create(self):
        pass


class LoadbalancerService(BaseService):

    def get(self, tenant_id, lb_id):
        self._validate_all_resources_exist(tenant_id=tenant_id, lb_id=lb_id)
        lb = self.lb_persistence.loadbalancer.get(tenant_id, lb_id)
        return lb

    def create(self, tenant_id):
        self._validate_all_resources_exist(tenant_id=tenant_id)
        pass


class LoadbalancerServiceOps(object):
    def __init__(self):
        self.lb_service = LoadbalancerService()
        self.lbs_service = LoadbalancersService()