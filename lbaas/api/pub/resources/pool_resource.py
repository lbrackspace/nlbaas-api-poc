from base import BaseResource
import flask
from flask import jsonify
from flask import request
from lbaas.services import pool_service


_attrs_to_remove = ('content_switching_id', 'health_monitor_id', 'tenant_id')


class PoolResource(BaseResource):
    def get(self, tenant_id, pool_id):
        pool = pool_service.PoolService().get(tenant_id, pool_id)
        return self._verify_and_form_response_body(pool, 'pool',
                                                   remove=_attrs_to_remove)

    def post(self, tenant_id, pool_id):
        flask.abort(405)

    def put(self, tenant_id, pool_id):
        # Object validation, error handling, etc...
        pass

    def delete(self, tenant_id, pool_id):
        pool_service.PoolService().delete(tenant_id, pool_id)


class PoolsResource(BaseResource):
    def get(self, tenant_id):
        pools = pool_service.PoolService().get_all(tenant_id)
        return self._verify_and_form_response_body(pools, 'pools',
                                                   remove=_attrs_to_remove)

    def post(self, tenant_id):
        pool = self.get_request_body(request)
        pool = pool.get('pool')
        created_pool = pool_service.PoolService().create(tenant_id, pool)
        return self._verify_and_form_response_body(created_pool, 'pool',
                                                   remove=_attrs_to_remove)

    def put(self, tenant_id, pool_id):
        flask.abort(405)

    def delete(self, tenant_id, pool_id):
        flask.abort(405)
