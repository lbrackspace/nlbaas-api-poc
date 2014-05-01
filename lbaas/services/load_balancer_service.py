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
        l7_json = json_lb.get('content-switching')
        ssl_decrypt_json = json_lb.get('ssl_decrypt')

        ##Vips
        vips_json = json_lb.get('vips')
        vips_in = []
        if vips_json is not None:
            for v in vips_json:
                vips_in.append(vip.VipModel(tenant_id=tenant_id,
                                            subnet_id=v.get('subnet_id'),
                                            type=v.get('type')))

        ##Pool Model
        pool_json = json_lb.get('pool')
        pool_in = None
        if pool_json is not None:
            members_json = pool_json.get('members')
            members_in = []
            if members_json is not None:
                for m in members_json:
                    members_in.append(member.MemberModel(ip=m.get('ip'),
                                                         port=m.get('port'),
                                                         weight=m.get('weight'),
                                                         condition=m.get('condition')))

            hm_json = json_lb.get('health_monitor')
            healthmonitor_in = ""
            if hm_json is not None:
                healthmonitor_in = health_monitor.HealthMonitorModel(
                    type=hm_json.get('type'),
                    delay=hm_json.get('delay'),
                    timeout=hm_json.get('timeout'),
                    attempts_before_deactivation=hm_json.get('attempts_before_deactivation'),
                    status_regex=hm_json.get('timeout'),
                    body_regex=hm_json.get('body_regex'),
                    host_header=hm_json.get('host_header'),
                    path=hm_json.get('path'))

            sslencrypt_json = pool_json.get('ssl_encrypt')
            sslen_in = ""
            if sslencrypt_json is not None:
                sslen_in = ssl_encrypt.SslEncryptModel(tenant_id=tenant_id,
                                                       enabled=sslencrypt_json.get('enabled'),
                                                       tls_certificate_id=sslencrypt_json.get('tls_cerificate_id'))

            pool_in = pool.PoolModel(tenant_id=tenant_id,
                                     ssl_encrypt=sslen_in,
                                     health_monitor=healthmonitor_in,
                                     name=pool_json.get('name'),
                                     subnet_id=pool_json.get('subnet_id'),
                                     algorithm=pool_json.get('algorithm'),
                                     session_persistence=pool_json.get('session_persistence'),
                                     members=members_in)



        lb_in = load_balancer.LoadbalancerModel(tenant_id, vips=vips_in,
                                                name=json_lb.get('name'),
                                                port=json_lb.get('port'),
                                                protocol=json_lb.get('protocol'),
                                                status="BUILD",
                                                pool=pool_in)
        lb = self.lb_persistence.loadbalancer.create(lb_in)
        return lb

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