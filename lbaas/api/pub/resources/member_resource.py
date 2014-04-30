from base import BaseResource
from flask import jsonify
from flask import request
from lbaas.services import member_service


class MemberResource(BaseResource):
    def get(self, tenant_id, pool_id, member_id):
        member = member_service.MemberService().get(pool_id, member_id)
        return self._verify_response_body(member, 'member')

    def post(self, tenant_id, pool_id):
        pass

    def put(self, tenant_id, pool_id, member_id):
        # Object validation, error handling, etc...
        pass

    def delete(self, tenant_id, pool_id, member_id):
        # Object validation, error handling, etc...
        pass


class MembersResource(BaseResource):
    def get(self, tenant_id, pool_id):
        members = member_service.MemberService().get_all(pool_id)
        return self._verify_response_body(members, 'members')

    def post(self, tenant_id, pool_id):
        pass

    def put(self, tenant_id, pool_id, member_id):
        # Object validation, error handling, etc...
        pass

    def delete(self, tenant_id, pool_id, member_id):
        # Object validation, error handling, etc...
        pass
