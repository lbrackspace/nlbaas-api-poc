import random
from sqlalchemy.exc import IntegrityError
from lbaas.models.util.mappings.model_mapper import JsonToDomainModelMapper
from lbaas.services.base import BaseService
from lbaas.models.persistence import load_balancer, pool, \
    lb_l7_policy, vip, member, ssl_encrypt, ssl_decrypt, \
    ssl_sni_decrypt_policy, ssl_sni_encrypt_policy, health_monitor


def gen_ipv4():
    octet1 = random.randint(1, 254)
    octet2 = random.randint(1, 254)
    octet3 = random.randint(1, 254)
    octet4 = random.randint(1, 254)
    return '{0}.{1}.{2}.{3}'.format(octet1, octet2, octet3, octet4)


class LoadbalancersService(BaseService):
    def get_all(self, tenant_id):
        self._validate_all_resources_exist(tenant_id=tenant_id)
        lbs = self.lb_persistence.loadbalancer.get_all(tenant_id)
        return lbs


class LoadbalancerService(BaseService):
    def get(self, tenant_id, lb_id):
        self._validate_all_resources_exist(tenant_id=tenant_id, lb_id=lb_id)
        lb = self.lb_persistence.loadbalancer.get(tenant_id, lb_id)
        return lb

    def create(self, tenant_id, json_lb):
        ####
        #The body parsing logic here could be place in a
        # general util so all services can use it without duplicating work...
        ####

        ##Vips
        vips_in = []
        if "vips" in json_lb:
            vips_json = json_lb.get('vips')
            for v in vips_json:
                vips_in.append(vip.VipModel(
                    tenant_id=tenant_id,
                    subnet_id=v.get('subnet_id'),
                    type=v.get('type'),
                    address=gen_ipv4()))

        ##Pool
        pool_in = None
        if 'pool' in json_lb:
            pool_json = json_lb.get('pool')
            pool_in = JsonToDomainModelMapper().compile_pool_model_from_json(
                tenant_id, pool_json)


        ##Ssl Decrypt
        ssld_in = None
        if 'ssl_decrypt' in json_lb:
            ssld_json = json_lb.get('ssl_decrypt')
            ssld_in = ssl_decrypt.SslDecryptModel(
                tenant_id=tenant_id,
                enabled=ssld_json.get('enabled'),
                tls_certificate_id=ssld_json.get('tls_cerificate_id'))


        ##Content switching handled outside of load balancer create for now...
        ###WIP
        cs_in = None
        if 'content-switching' in json_lb:
            cs_json = json_lb.get('content-switching')
            pools_in = []
            if 'pools' in cs_json:
                pools_json = cs_json.get('pools')
                for p in pools_json:
                    pools_in.append(
                        JsonToDomainModelMapper().compile_pool_model_from_json(
                            tenant_id, p))
            cs_in = lb_l7_policy.LbL7PolicyModel(
                pools=pools_in,
                condition=cs_json.get('match'),
                type=cs_json.get('type'))

        lb_in = load_balancer.LoadbalancerModel(tenant_id,
                                                vips=vips_in,
                                                name=json_lb.get('name'),
                                                content_switching=json_lb.get(
                                                    'content-swithcing'),
                                                port=json_lb.get('port'),
                                                protocol=json_lb.get(
                                                    'protocol'),
                                                status="BUILD",
                                                pool=pool_in,
                                                ssl_decrypt=ssld_in,
                                                lb_l7_policy=cs_in)
        lb = self.lb_persistence.loadbalancer.create(lb_in)

        return lb

    def update(self, tenant_id):
        self._validate_all_resources_exist(tenant_id=tenant_id)
        pass

    def delete(self, tenant_id):
        self._validate_all_resources_exist(tenant_id=tenant_id)
        pass


class LoadbalancerServiceOps(object):
    def __init__(self):
        self.lb_service = LoadbalancerService()
        self.lbs_service = LoadbalancersService()