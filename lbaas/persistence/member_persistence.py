from lbaas.models.persistence import base, member
from lbaas.persistence.base import BaseService


class MemberPersistence(BaseService):
    def get_all(self, pool_id):
        members = member.MemberModel.query.filter_by(pool_id=pool_id).all()
        return members

    def create(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass


class MemberPersistenceOps(object):
    def __init__(self):
        self.member = MemberPersistence(self)