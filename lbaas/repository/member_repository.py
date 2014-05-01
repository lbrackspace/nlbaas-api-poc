from lbaas.models.persistence import base, member
from lbaas.repository.base import BaseService


class MemberRepository(BaseService):

    def get(self, pool_id, member_id):
        ret_member = member.MemberModel.query.filter_by(pool_id=pool_id,
                                                        id_=member_id).first()
        return ret_member

    def get_all(self, pool_id):
        members = member.MemberModel.query.filter_by(pool_id=pool_id).all()
        return members

    def create(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass


class MemberRepositoryOps(object):
    def __init__(self):
        self.member = MemberRepository(self)