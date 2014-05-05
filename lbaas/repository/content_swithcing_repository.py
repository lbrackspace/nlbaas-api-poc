from lbaas.models.persistence import base
from lbaas.repository.base import BaseService
from lbaas.models.persistence import content_switching



class ContentSwitchingRepository(BaseService):
    def get(self, tenant_id, cs_id):
        cs = content_switching.ContentSwitchingModel.query\
            .filter_by(id_=cs_id).first()
        return cs

    def get_by_lb_id(self, tenant_id, lb_id):
        cs = content_switching.ContentSwitchingModel.query\
            .filter_by(lb_id=lb_id).first()
        return cs

    def update(self, tenant_id, cs_model):
        base.db.session.add(cs_model)
        base.db.session.commit()
        return cs_model

    def delete(self, cs_model):
        base.db.session.delete(cs_model)
        base.db.session.commit()


class ContentSwitchingRepositoryOps(object):
    def __init__(self):
        self.content_switching = ContentSwitchingRepository(self)