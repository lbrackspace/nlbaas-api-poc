from lbaas.models.persistence import load_balancer, pool, \
    content_switching, vip, member, ssl_encrypt, ssl_decrypt, \
    ssl_sni_decrypt_policy, ssl_sni_encrypt_policy, health_monitor


class JsonToDomainModelMapper():
    def __init__(self):
        pass

    def compile_pool_model_from_json(self, tenant_id, pool_json):
            if 'pool_id' in pool_json:
                return self.pool_persistence.pool.get(tenant_id,
                                                      pool_json.get('pool_id'))
            members_json = pool_json.get('members')
            members_in = []
            if members_json is not None:
                for m in members_json:
                    members_in.append(member.MemberModel(
                        ip=m.get('ip'),
                        port=m.get('port'),
                        weight=m.get('weight'),
                        condition=m.get('condition')))

            healthmonitor_in = None
            if "health_monitor" in pool_json:
                hm_json = pool_json.get('health_monitor')
                healthmonitor_in = health_monitor.HealthMonitorModel(
                    type=hm_json.get('type'),
                    delay=hm_json.get('delay'),
                    timeout=hm_json.get('timeout'),
                    attempts_before_deactivation=hm_json.get(
                        'attempts_before_deactivation'),
                    status_regex=hm_json.get('timeout'),
                    body_regex=hm_json.get('body_regex'),
                    host_header=hm_json.get('host_header'),
                    path=hm_json.get('path'))

            sslen_in = None
            if 'ssl_encrypt' in pool_json:
                sslencrypt_json = pool_json.get('ssl_encrypt')
                sslen_in = ssl_encrypt.SslEncryptModel(
                    tenant_id=tenant_id,
                    enabled=sslencrypt_json.get('enabled'),
                    ##Update for certs/sni
                    tls_certificate=None)

            return pool.PoolModel(tenant_id=tenant_id,
                                  ssl_encrypt=sslen_in,
                                  health_monitor=healthmonitor_in,
                                  name=pool_json.get('name'),
                                  subnet_id=pool_json.get('subnet_id'),
                                  algorithm=pool_json.get('algorithm'),
                                  session_persistence=pool_json.get(
                                      'session_persistence'),
                                  members=members_in)