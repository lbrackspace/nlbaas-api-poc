from flask.ext.restful import Resource
# Import persistence classes EX: from lbaas.persistence.lb_persistence import LbPersistenceOps


class BaseService(Resource):
    def __init__(self):
        #Init persistence classes here ex:
        #self.lbpersistence = LbPersistenceOps()
        pass