from base import BaseResource
from flask import jsonify
from flask import request
from lbaas.persistence.load_balancer_persistence \
    import LoadbalancerPersistence as lb_persistence


class LoadbalancerResource(BaseResource):
    def get(self, tenant_id):
        lbs = lb_persistence.get(tenant_id)
        lb_list = [l.to_dict() for l in lbs]
        lbs = {"loadbalancers": lb_list}
        return lbs

    def post(self, account_id, pool_id, health_monitor):
        pass

    def put(self, account_id, pool_id, health_monitor):
        # Object validation, error handling, etc...
        pass

    def delete(self, accound_id, pool_id):
        # Object validation, error handling, etc...
        pass
