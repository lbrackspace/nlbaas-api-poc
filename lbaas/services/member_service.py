from lbaas.services.base import BaseService
from lbaas.models.persistence.member import MemberModel


class MemberService(BaseService):
    def get_all(self, pool_id):
        members = self.member_persistence.member.get_all(pool_id)
        return members

    def get(self, pool_id, member_id):
        member = self.member_persistence.member.get(pool_id, member_id)
        return member

    def create(self, pool_id, member):
        pool = self.pool_persistence.pool.get(tenant_id, pool_id)
        created_member = MemberModel(pool=pool,
                                     ip=member.get('ip'),
                                     port=member.get('port'),
                                     weight=member.get('weight'),
                                     condition=member.get('condition'))
        created_member = self.member_persistence.member.create(created_member)
        return created_member

    def update(self, pool_id, member_id, member):
        updated_member = self.member_persistence.member.get(pool_id, member_id)
        updated_member.ip = member.get('ip')
        updated_member.port = member.get('port')
        updated_member.condition = member.get('condition')
        updated_member.weight = member.get('weight')
        updated_member = self.member_persistence.member.create(updated_member)
        return updated_member

    def delete(self, pool_id, member_id):
        member = self.get(pool_id, member_id)
        return self.member_persistence.member.delete(member)


class MemberServiceOps(object):
    def __init__(self):
        self.member_service = MemberService()