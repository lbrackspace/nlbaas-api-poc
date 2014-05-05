from base import BaseResource
from flask import jsonify
from flask import request
from lbaas.services import content_switching_service


class ContentSwitchingResource(BaseResource):
    def get(self, tenant_id, pool_id):
        # Object validation, error handling, etc...
        cs_model = content_switching_service.ContentSwitchingService().get(
            tenant_id, pool_id)
        return self._verify_and_form_response_body(cs_model, 'content_switching')

    def post(self, tenant_id):
        json_body = self.get_request_body(request)
        json_cs = json_body.get('content_switching')
        cs_model = content_switching_service.ContentSwitchingService().create(
            tenant_id, json_cs)
        return self._verify_and_form_response_body(cs_model, 'content_switching')

    def put(self, tenant_id, pool_id):
        pass

    def delete(self, tenant_id, cs_id):
        content_switching_service.ContentSwitchingService()\
            .delete(tenant_id, cs_id)
