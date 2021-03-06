import random
from sqlalchemy.exc import IntegrityError
from lbaas.models.util.mappings.model_mapper import JsonToDomainModelMapper
from lbaas.services.base import BaseService
from lbaas.models.persistence import load_balancer, pool, \
    content_switching, vip, member, ssl_encrypt, ssl_decrypt, \
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
                if 'vip_id' in v:
                    self.vip_persistence.vip.get(tenant_id=tenant_id,
                                                 vip_id=v.get('vip_id'))
                else:
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
                ##Update for certs/sni
                tls_certificate=None)

        ##Content switching handled outside of load balancer create for now...
        ###WIP
        cs_in = None
        if 'content_switching' in json_lb:
            cs_json = json_lb.get('content_switching')
            if 'id' in cs_json:
                cs_in = self.content_swithcing_repository.content_switching\
                    .get(tenant_id, cs_json.get('id'))
            else:
                pools_in = []
                if 'pools' in cs_json:
                    pools_json = cs_json.get('pools')
                    for p in pools_json:
                        pools_in.append(
                            JsonToDomainModelMapper()
                            .compile_pool_model_from_json(tenant_id, p))
                cs_in = content_switching.ContentSwitchingModel(
                    pools=pools_in,
                    enabled=cs_json.get('enabled'),
                    match=cs_json.get('rule').get('match'),
                    type_=cs_json.get('rule').get('type'))

        lb_in = load_balancer.LoadbalancerModel(tenant_id,
                                                vips=vips_in,
                                                name=json_lb.get('name'),
                                                port=json_lb.get('port'),
                                                protocol=json_lb.get(
                                                    'protocol'),
                                                status="BUILD",
                                                pool=pool_in,
                                                ssl_decrypt=ssld_in,
                                                content_switching=cs_in)
        lb = self.lb_persistence.loadbalancer.create(lb_in)

        return lb

    def update(self, tenant_id):
        self._validate_all_resources_exist(tenant_id=tenant_id)
        pass

    def delete(self, tenant_id, lb_id):
        self._validate_all_resources_exist(tenant_id=tenant_id, lb_id=lb_id)
        #lb = self.lb_persistence.loadbalancer.get(tenant_id, lb_id)

        self.lb_vip_persistence.lb_vip.delete(lb_id)
        self.lb_persistence.loadbalancer.delete(lb_id)

        cs = self.content_swithcing_repository.content_switching\
            .get_by_lb_id(tenant_id, lb_id)
        cs.lb_id = None
        self.content_swithcing_repository\
            .content_switching.update(tenant_id, cs)


class LoadbalancerServiceOps(object):
    def __init__(self):
        self.lb_service = LoadbalancerService()
        self.lbs_service = LoadbalancersService()