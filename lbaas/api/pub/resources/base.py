import json

import flask

import lbaas.models.persistence.base as base_model

from flask.ext.restful import Resource


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

    def _verify_response_body(self, response_body, tag):
        if response_body is None:
            flask.abort(404)
        if isinstance(response_body, base_model.BaseModel):
            response_body = flask.jsonify(
                {tag: response_body.to_dict()})
        if isinstance(response_body, list):
            response_body_list = [body.to_dict() for body in response_body]
            response_body = {tag: response_body_list}
        return response_body