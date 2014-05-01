from lbaas.models.persistence import base, load_balancer
from lbaas.persistence.base import BaseService


class LoadbalancerPersistence(BaseService):

    def get(self, tenant_id, lb_id):
        lb = load_balancer.LoadbalancerModel.query.filter_by(
            tenant_id=tenant_id, id_=lb_id).first()
        return lb

    def get_all(self, tenant_id):
        lbs = load_balancer.LoadbalancerModel\
            .query.filter_by(tenant_id=tenant_id).all()
        return lbs

    def create(self, in_lb):
        ##Error checking etc..
        #defaults for poc...
        base.db.session.add(in_lb)
        base.db.session.flush()
        base.db.session.commit()
        pass

    def update(self):
        pass

    def delete(self):
        pass


class LoadbalancerPersistenceOps(object):
    def __init__(self):
        self.loadbalancer = LoadbalancerPersistence(self)