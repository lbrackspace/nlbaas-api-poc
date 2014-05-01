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

    def create(self, member_model):
        base.db.session.add(member_model)
        base.db.session.commit()
        return member_model

    def update(self, member_model):
        base.db.session.add(member_model)
        base.db.session.commit()
        return member_model


    def delete(self, member_model):
        base.db.session.delete(member_model)
        base.db.session.commit()
        return member_model


class MemberRepositoryOps(object):
    def __init__(self):
        self.member = MemberRepository(self)