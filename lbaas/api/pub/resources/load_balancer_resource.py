from base import BaseResource
from flask import jsonify
from flask import request
from lbaas.services \
    import load_balancer_service


class LoadbalancerResource(BaseResource):
    def get(self, tenant_id, lb_id):
        lb = load_balancer_service.LoadbalancerService().get(tenant_id, lb_id)
        return self._verify_response_body(lb, 'loadbalancer')

    def put(self, tenant_id, lb_id):
        # Object validation, error handling, etc...
        pass

    def delete(self, tenant_id, lb_id):
        # Object validation, error handling, etc...
        pass


class LoadbalancersResource(BaseResource):
    def get(self, tenant_id):
        lbs = load_balancer_service.LoadbalancersService().get_all(tenant_id)
        #return lbs
        return self._verify_and_form_response_body(lbs, 'loadbalancers')

    def post(self, tenant_id):
        json_lb = self.get_request_body(request).get('loadbalancer')
        lb = load_balancer_service\
            .LoadbalancersService().create(tenant_id, json_lb)
        return lb