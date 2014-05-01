from lbaas.services.base import BaseService
from lbaas.models.persistence import load_balancer, pool, \
    lb_l7_policy, vip, member, ssl_encrypt, ssl_decrypt, \
    ssl_sni_decrypt_policy, ssl_sni_encrypt_policy


class LoadbalancersService(BaseService):

    def get_all(self, tenant_id):
        self._validate_all_resources_exist(tenant_id=tenant_id)
        lbs = self.lb_persistence.loadbalancer.get_all(tenant_id)
        return lbs

    def create(self, tenant_id, json_lb):
        vips_json = json_lb.get('vips')
        pool_json = json_lb.get('pool')
        l7_json = json_lb.get('content-switching')
        ssl_decrypt_json = json_lb.get('ssl_decrypt')

        vips_in = []
        if vips_json is not None:
            for v in vips_json:
                vips_in.append(vip.VipModel(tenant_id=tenant_id,
                                            subnet_id=v.get('subnet_id'),
                                            type=v.get('type')))
        lb_in = load_balancer.LoadbalancerModel(tenant_id, vips=vips_in)
        self.lb_persistence.loadbalancer.create(lb_in)

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