import random
from lbaas.services.base import BaseService
from lbaas.models.persistence.vip import VipModel


def get_random_ip():
    octet1 = random.randint(1, 254)
    octet2 = random.randint(1, 254)
    octet3 = random.randint(1, 254)
    octet4 = random.randint(1, 254)
    return '{0}.{1}.{2}.{3}'.format(octet1, octet2, octet3, octet4)


class VIPService(BaseService):

    def get(self, tenant_id, vip_id):
        vip = self.vip_persistence.vip.get(tenant_id, vip_id)
        return vip

    def get_all(self, tenant_id):
        vips = self.vip_persistence.vip.get_all(tenant_id)
        return vips

    def create(self, tenant_id, vip):
        created_vip = VipModel(tenant_id=tenant_id,
                               subnet_id=vip.get('subnet_id'),
                               type=vip.get('type'),
                               address=get_random_ip())
        created_vip = self.vip_persistence.vip.create(created_vip)
        return created_vip

    def update(self, tenant_id, vip):
        flask.abort(405)

    def delete(self, tenant_id, vip_id):
        vip = self.get(tenant_id, vip_id)
        return self.vip_persistence.vip.delete(tenant_id, vip)


class VIPServiceOps(object):
    def __init__(self):
        self.vip_service = VIPService()