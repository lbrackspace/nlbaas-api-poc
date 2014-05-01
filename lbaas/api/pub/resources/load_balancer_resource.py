from base import BaseResource
from flask import jsonify
from flask import request
from lbaas.services \
    import load_balancer_service


class LoadbalancerResource(BaseResource):
    def get(self, tenant_id, lb_id):
        lb = load_balancer_service.LoadbalancerService().get(tenant_id, lb_id)
        return self._verify_response_body(lb, 'loadbalancer')

    def post(self, account_id):
        pass

    def put(self, account_id, lb_id):
        # Object validation, error handling, etc...
        pass

    def delete(self, accound_id, lb_id):
        # Object validation, error handling, etc...
        pass


class LoadbalancersResource(BaseResource):
    def get(self, tenant_id):
        lbs = load_balancer_service.LoadbalancerService().get_all(tenant_id)
        return self._verify_response_body(lbs, 'loadbalancers')

    def post(self, account_id):
        pass

    def put(self, account_id, lb_id):
        # Object validation, error handling, etc...
        pass

    def delete(self, accound_id, lb_id):
        # Object validation, error handling, etc...
        pass
