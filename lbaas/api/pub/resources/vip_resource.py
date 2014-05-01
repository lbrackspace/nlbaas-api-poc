from base import BaseResource
import flask
from flask import jsonify
from flask import request
from lbaas.services import vip_service


_attrs_to_remove = ('tenant_id')


class VIPResource(BaseResource):
    def get(self, tenant_id, vip_id):
        member = vip_service.VIPService().get(tenant_id, vip_id)
        return self._verify_and_form_response_body(member, 'vip',
                                                   remove=_attrs_to_remove)

    def post(self, tenant_id, vip_id):
        flask.abort(405)

    def put(self, tenant_id, vip_id):
        # Object validation, error handling, etc...
        pass

    def delete(self, tenant_id, vip_id):
        vip_service.VIPService().delete(tenant_id, vip_id)


class VIPsResource(BaseResource):
    def get(self, tenant_id):
        vips = vip_service.VIPService().get_all(tenant_id)
        return self._verify_and_form_response_body(vips, 'vips',
                                                   remove=_attrs_to_remove)

    def post(self, tenant_id):
        vip = self.get_request_body(request)
        vip = vip.get('vip')
        created_vip = vip_service.VIPService().create(tenant_id, vip)
        return self._verify_and_form_response_body(created_vip, 'vip',
                                                   remove=_attrs_to_remove)

    def put(self, tenant_id):
        flask.abort(405)

    def delete(self, tenant_id):
        flask.abort(405)
