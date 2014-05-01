from lbaas.services.base import BaseService
from lbaas.models.persistence import load_balancer, pool, \
    lb_l7_policy, vip, member, ssl_encrypt, ssl_decrypt, \
    ssl_sni_decrypt_policy, ssl_sni_encrypt_policy, health_monitor


class LoadbalancersService(BaseService):

    def get_all(self, tenant_id):
        self._validate_all_resources_exist(tenant_id=tenant_id)
        lbs = self.lb_persistence.loadbalancer.get_all(tenant_id)
        return lbs

    def create(self, tenant_id, json_lb):
        ####
        #The body parsing logic here could be place in a
        # general util so all services can use it without duplicating work...
        ####
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

        pool_in = ""
        if pool_json is not None:
            members_json = pool_json.get('members')
            members_in = []
            if members_json is not None:
                for m in members_json:
                    members_in.append(member.MemberModel(ip=m.get('ip'),
                                                         port=m.get('port'),
                                                         weight=m.get('weight'),
                                                         condition=m.get('condition')))
            healthmonitor_in = health_monitor.HealthMonitorModel()
            pool_in = pool.PoolModel(tenant_id=tenant_id,
                                     ssl_encrypt=pool_json.get('ssl_encrypt'),
                                     health_monitor=healthmonitor_in,
                                     name=pool_json.get('name'),
                                     subnet_id=pool_json.get('subnet_id'),
                                     algorithm=pool_json.get('algorithm'),
                                     members=members_in)



        lb_in = load_balancer.LoadbalancerModel(tenant_id, vips=vips_in)
        self.lb_persistence.loadbalancer.create(lb_in)
        return lb_in

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