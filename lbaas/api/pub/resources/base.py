import json

import flask

import lbaas.models.persistence.base as base_model

from flask_restful import Resource


class BaseResource(Resource):
    def __init__(self):
        #Can set configurations and other resource options here...
        pass

    def get_request_body(self, req):
        try:
            #JSON Validation
            raw_json = req.stream.read(req.content_length)
        except Exception:
            raise flask.abort(500)
        try:
            #JSON Validation
            json_body = json.loads(raw_json, 'utf-8')
        except ValueError:
            raise flask.abort(400)
        return json_body

    def _verify_and_form_response_body(self, response_body, tag,
                                       remove=None):
        if isinstance(response_body, base_model.BaseModel):
            response_body = response_body.to_dict()
            if remove:
                copy_body = dict(response_body)
                for attr in response_body:
                    if attr in remove:
                        del copy_body[attr]
                response_body = copy_body
            response_body = {tag: response_body}
        if isinstance(response_body, list):
            response_body_list = [body.to_dict() for body in response_body]
            if remove:
                new_response_body_list = []
                for body in response_body_list:
                    copy_body = dict(body)
                    for attr in body:
                        if attr in remove:
                            del copy_body[attr]
                            new_response_body_list.append(copy_body)
                response_body_list = new_response_body_list
            response_body = {tag: response_body_list}
        return response_body