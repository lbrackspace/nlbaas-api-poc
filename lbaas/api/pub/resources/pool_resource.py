from base import BaseResource
from flask import jsonify
from flask import request
from lbaas.services import pool_service


class PoolResource(BaseResource):
    def get(self, tenant_id):
        pools = pool_service.PoolService().get_all(tenant_id)
        pool_list = [l.to_dict() for l in pools]
        pools = {"pools": pool_list}
        return pools

    def post(self, account_id):
        pass

    def put(self, account_id, pool_id):
        # Object validation, error handling, etc...
        pass

    def delete(self, accound_id, pool_id):
        # Object validation, error handling, etc...
        pass
