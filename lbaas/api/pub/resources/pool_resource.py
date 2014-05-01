from base import BaseResource
from flask import jsonify
from flask import request
from lbaas.services import pool_service


class PoolResource(BaseResource):
    def get(self, tenant_id, pool_id):
        pool = pool_service.PoolService().get(tenant_id, pool_id)
        return self._verify_and_form_response_body(pool, 'pool')

    def post(self, tenant_id):
        pass

    def put(self, tenant_id, pool_id):
        # Object validation, error handling, etc...
        pass

    def delete(self, tenant_id, pool_id):
        # Object validation, error handling, etc...
        pass


class PoolsResource(BaseResource):
    def get(self, tenant_id):
        pools = pool_service.PoolService().get_all(tenant_id)
        return self._verify_and_form_response_body(pools, 'pools')

    def post(self, tenant_id):
        pool = self.get_request_body(request)
        pool = pool.get('pool')
        created_pool = pool_service.PoolService().create(tenant_id, pool)
        return self._verify_and_form_response_body(created_pool, 'pool')

    def put(self, tenant_id, pool_id):
        # Object validation, error handling, etc...
        pass

    def delete(self, tenant_id, pool_id):
        # Object validation, error handling, etc...
        pass
