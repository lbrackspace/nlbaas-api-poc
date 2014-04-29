from base import BaseResource
from flask import jsonify
from flask import request
from lbaas.persistence.health_monitor_persistence \
    import HealthMonitorPersistence as hm_persistence


class HealthMonitorResource(BaseResource):
    def get(self, tenant_id, pool_id):
        # Object validation, error handling, etc...
        pass

    def post(self, tenant_id, pool_id, health_monitor):
        json_body = self.get_request_body(request)
        json_monitor = json_body.get('monitor')
        # Object validation, error handling, etc...
        monitor = hm_persistence.create(tenant_id, pool_id, json_monitor)
        return jsonify({'health_monitor': monitor.to_dict()})

    def put(self, account_id, pool_id, health_monitor):
        # Object validation, error handling, etc...
        pass

    def delete(self, accound_id, pool_id):
        # Object validation, error handling, etc...
        pass
