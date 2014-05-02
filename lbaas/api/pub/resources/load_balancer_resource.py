from sqlalchemy.exc import IntegrityError
from base import BaseResource
import flask
from lbaas.services \
    import load_balancer_service


class LoadbalancerResource(BaseResource):
    def get(self, tenant_id, lb_id):
        lb = load_balancer_service.LoadbalancerService().get(tenant_id, lb_id)
        return self._verify_and_form_response_body(lb, 'loadbalancer')

    def post(self, tenant_id):
        flask.abort(405)

    def put(self, tenant_id):
        flask.abort(501)

    def delete(self, tenant_id):
        flask.abort(501)


class LoadbalancersResource(BaseResource):
    def get(self, tenant_id):
        lbs = load_balancer_service.LoadbalancersService().get_all(tenant_id)
        #return lbs
        return self._verify_and_form_response_body(lbs, 'loadbalancers')

    def post(self, tenant_id):
        json_lb = self.get_request_body(flask.request).get('loadbalancer')
        try:
            lb = load_balancer_service\
                .LoadbalancerService().create(tenant_id, json_lb)
        except IntegrityError as e:
            ##Use custom errors to define actual issue for user
            print e
            flask.abort(400)

        return self._verify_and_form_response_body(lb, 'loadbalancer')

    def put(self, tenant_id):
        flask.abort(405)

    def delete(self, tenant_id):
        flask.abort(405)