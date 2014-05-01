from lbaas.models.persistence import base, vip
from lbaas.repository.base import BaseService


class VIPRepository(BaseService):

    def get(self, tenant_id, vip_id):
        ret_vip = vip.VipModel.query.filter_by(tenant_id=tenant_id,
                                               id_=vip_id).first()
        return ret_vip

    def get_all(self, tenant_id):
        vips = vip.VipModel.query.filter_by(tenant_id=tenant_id).all()
        return vips

    def create(self, vip_model):
        base.db.session.add(vip_model)
        base.db.session.commit()
        return vip_model

    def update(self, vip_model):
        base.db.session.add(vip_model)
        base.db.session.commit()
        return vip_model

    def delete(self):
        pass


class VipRepositoryOps(object):
    def __init__(self):
        self.vip = VIPRepository(self)