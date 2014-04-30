from lbaas.services.base import BaseService


class MemberService(BaseService):
    def get_all(self, pool_id):
        members = self.member_persistence.member.get_all(pool_id)
        return members

    def get(self, pool_id, member_id):
        member = self.member_persistence.member.get(pool_id, member_id)
        return member

    def create(self):
        pass


class MemberServiceOps(object):
    def __init__(self):
        self.member_service = MemberService()