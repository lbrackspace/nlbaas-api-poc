from base import BaseResource
from flask import jsonify
from flask import request
from lbaas.services import member_service


class MemberResource(BaseResource):
    def get(self, tenant_id, pool_id):
        members = member_service.MemberService().get_all(pool_id)
        member_list = [l.to_dict() for l in members]
        members = {"members": member_list}
        return members

    def post(self, account_id, pool_id):
        pass

    def put(self, account_id, pool_id, member_id):
        # Object validation, error handling, etc...
        pass

    def delete(self, accound_id, pool_id, member_id):
        # Object validation, error handling, etc...
        pass
