from lbaas.services.base import BaseService
from lbaas.models.persistence.content_switching import ContentSwitchingModel
from lbaas.models.util.mappings.model_mapper import JsonToDomainModelMapper



class ContentSwitchingService(BaseService):

    def get(self, tenant_id, cs_id):
        cs = self.content_swithcing_repository.content_switching\
            .get(tenant_id, cs_id)
        return cs

    def get_all(self):
        pass

    def create(self, tenant_id, cs_json):
        pools_in = []
        if 'pools' in cs_json:
            pools_json = cs_json.get('pools')
            for p in pools_json:
                pools_in.append(
                    JsonToDomainModelMapper()
                    .compile_pool_model_from_json(tenant_id, p))
        cs_model = ContentSwitchingModel(
            pools=pools_in,
            enabled=cs_json.get('enabled'),
            match=cs_json.get('rule').get('match'),
            type_=cs_json.get('rule').get('type'))
        return cs_model

    def update(self, tenant_id, cs_id, monitor):
        pass

    def delete(self, tenant_id, cs_id):
        self.delete(tenant_id, cs_id)

    class ContentSwitchingServiceOps(object):
        def __init__(self):
            self.content_switching = ContentSwitchingService()