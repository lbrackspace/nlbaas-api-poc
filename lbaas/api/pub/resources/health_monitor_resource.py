from base import BaseResource
from flask import jsonify
from flask import request
from lbaas.persistence.health_monitor_persistence \
    import HealthMonitorPersistence


class HealthMonitorResource(BaseResource):
    def get(self, tenant_id, pool_id):
        # Object validation, error handling, etc...
        monitor = HealthMonitorPersistence.get(tenant_id, pool_id)
        return jsonify({"health_monitor": monitor.to_dict()})

# TODO:  Fix this method in regards to its arguments and implementation
    def post(self, tenant_id, pool_id, health_monitor):
        json_body = self.get_request_body(request)
        json_monitor = json_body.get('monitor')
        # Object validation, error handling, etc...
        monitor = HealthMonitorPersistence.create(tenant_id, pool_id,
                                                  json_monitor)
        return jsonify({"health_monitor": monitor.to_dict()})

    def put(self, tenant_id, pool_id, health_monitor):
        # Object validation, error handling, etc...
        json_body = self.get_request_body(request)
        json_monitor = json_body.get('monitor')
        monitor = HealthMonitorPersistence.update(tenant_id, pool_id,
                                                  json_monitor)
        return jsonify({"health_monitor": monitor.to_dict()})

    def delete(self, accound_id, pool_id):
        # Object validation, error handling, etc...
        pass
