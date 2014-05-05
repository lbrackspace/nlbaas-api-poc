from lbaas.models.persistence import base, lb_vip
from lbaas.repository.base import BaseService


class LbVipRepository(BaseService):

    def delete(self, lb_id):
        base.db.session.query(lb_vip.LbVipModel)\
            .filter(lb_vip.LbVipModel.lb_id == lb_id).delete()


class LbVipRepositoryOps(object):
    def __init__(self):
        self.lb_vip = LbVipRepository(self)