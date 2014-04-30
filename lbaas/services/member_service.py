from lbaas.services.base import BaseService

class MemberService(BaseService):
    def get_all(self, pool_id):
        members = self.member_persistence.member.get_all(pool_id)
        return members

    def create(self):
        pass


class MemberServiceOps(object):
    def __init__(self):
        self.member_service = MemberService()