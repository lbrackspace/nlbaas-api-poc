import flask
from flask import request
from flask_restful import Resource
from lbaas.persistence.health_monitor_persistence \
    import HealthMonitorPersistenceOps
from lbaas.persistence.load_balancer_persistence \
import LoadbalancerPersistenceOps
from lbaas.persistence.pool_persistence import PoolPersistenceOps
from lbaas.persistence.member_persistence import MemberPersistenceOps


class BaseService(Resource):
    def __init__(self):
        #Init persistence classes here ex:
        ##naming and links looks odd, figure how to chain differently
        self.lb_persistence = LoadbalancerPersistenceOps()
        self.monitor_persistence = HealthMonitorPersistenceOps()
        self.pool_persistence = PoolPersistenceOps()
        self.member_persistence = MemberPersistenceOps()

    def validate_resources(self):
        resources = request.view_args.copy()
        if 'healthmonitor' in request.path:
            resources['health_monitor'] = True
        self._validate_all_resources_exist(**resources)

    def _validate_all_resources_exist(self, tenant_id=None, lb_id=None,
                                      pool_id=None, member_id=None,
                                      health_monitor=False):
        resources = []

        if pool_id is not None:
            pool = self.pool_persistence.pool.get(tenant_id, pool_id)
            resources.append(pool)
            if member_id is not None:
                resources.append(
                    self.member_persistence.member.get(pool_id, member_id))
            if health_monitor:
                resources.append(pool.health_monitor)

        if lb_id is not None:
            resources.append(self.lb_persistence.loadbalancer.get(tenant_id,
                                                                  lb_id))

        for resource in resources:
            if resource is None:
                flask.abort(404)
