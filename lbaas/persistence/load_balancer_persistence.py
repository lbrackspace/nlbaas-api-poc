from lbaas.models.persistence import base, load_balancer
from lbaas.persistence.base import BaseService


class LoadbalancerPersistence(BaseService):
    def get(self, tenant_id):
        lbs = load_balancer.LoadbalancerModel\
            .query.filter_by(tenant_id=tenant_id).all()
        return lbs

    def create(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass