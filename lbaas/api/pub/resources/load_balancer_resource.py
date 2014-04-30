from base import BaseResource
from flask import jsonify
from flask import request
from lbaas.services \
    import load_balancer_service


class LoadbalancerResource(BaseResource):
    def get(self, tenant_id):
        lbs = load_balancer_service.LoadbalancerService().get_all(tenant_id)
        lb_list = [l.to_dict() for l in lbs]
        lbs = {"loadbalancers": lb_list}
        return lbs

    def post(self, account_id):
        pass

    def put(self, account_id, lb_id):
        # Object validation, error handling, etc...
        pass

    def delete(self, accound_id, lb_id):
        # Object validation, error handling, etc...
        pass
