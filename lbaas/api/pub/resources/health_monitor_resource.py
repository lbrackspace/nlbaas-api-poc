from base import BaseResource
from flask import jsonify
from flask import request
from lbaas.services import health_monitor_service


class HealthMonitorResource(BaseResource):
    def get(self, tenant_id, pool_id):
        # Object validation, error handling, etc...
        monitor = health_monitor_service.HealthMonitorService().get(
            tenant_id, pool_id)
        return self._verify_and_form_response_body(monitor, 'health_monitor')

# TODO:  Fix this method in regards to its arguments and implementation
    def post(self, tenant_id, pool_id):
        json_body = self.get_request_body(request)
        json_monitor = json_body.get('health_monitor')
        # Object validation, error handling, etc...
        monitor = health_monitor_service.HealthMonitorService().create(
            tenant_id, pool_id, json_monitor)
        return jsonify({"health_monitor": monitor.to_dict()})

    def put(self, tenant_id, pool_id, health_monitor):
        pass

    def delete(self, accound_id, pool_id):
        # Object validation, error handling, etc...
        pass
