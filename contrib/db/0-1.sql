SET autocommit=0;
SET unique_checks=0;
SET foreign_key_checks=0;

DROP TABLE IF EXISTS `member`;
CREATE TABLE `member` (
    `id` varchar(128) NOT NULL,
    `pool_id` int(11) DEFAULT NULL,
    `ip` varchar(128) DEFAULT NULL,
    `condition` varchar(32) DEFAULT NULL,
    `weight` int(11) DEFAULT NULL,
    `status` varchar(32) DEFAULT NULL,
    PRIMARY KEY (`id`),
    CONSTRAINT  `fk_m_condition` FOREIGN KEY (condition) REFERENCES `enum_member_condition`(name),
    CONSTRAINT `fk_m_status` FOREIGN KEY (status) REFERENCES `enum_member_status`(name),
    CONSTRAINT `fk_m_pool` FOREIGN KEY (pool_id) REFERENCES pool(id)
) ENGINE=InnoDB;

DROP TABLE IF EXISTS `pool`;
CREATE TABLE `pool` (
    `id` int(32) NOT NULL,
    `health_monitor_id` int(32) NOT NULL,
    `tenant_id` varchar(128) DEFAULT NULL
    `name` varchar(128) DEFAULT NULL,
    `subnet_id` varchar(128) DEFAULT NULL,
    `ssl_encrypt_id` int(32) DEFAULT NULL,
    `session_persistence` varchar(32) DEFAULT NULL,
    `algorithm` varchar(32) DEFAULT NULL,
    PRIMARY KEY (`id`),
    CONSTRAINT `fk_p_sp` FOREIGN KEY (session_persistence) REFERENCES enum_pool_session_persistence(id),
    CONSTRAINT `fk_p_algo` FOREIGN KEY (algorithm) REFERENCES enum_pool_algorithm(id),
    CONSTRAINT `fk_p_ssl_encrypt` FOREIGN KEY (ssl_encrypt_id) REFERENCES ssl_encrypt(id),
    CONSTRAINT `fk_p_hm_id` FOREIGN KEY (health_monitor_id) REFERENCES health_monitor(id)
) ENGINE=InnoDB;

DROP TABLE IF EXISTS `health_monitor`;
CREATE TABLE `health_monitor` (
    `id` int(32) NOT NULL,
    `type` varchar(32) DEFAULT NULL,
    `delay` int(32) DEFAULT NULL,
    `timeout` int(32) DEFAULT NULL,
    `attempts_before_deactivation` int(32) DEFAULT NULL,
    `status_regex` varchar(128) DEFAULT NULL,
    `body_regex` varchar(128) DEFAULT NULL,
    `host_header` varchar(256) DEFAULT NULL,
    `path` varchar(128) DEFAULT NULL,
    PRIMARY KEY (`id`),
    CONSTRAINT `fk_hm_type` FOREIGN KEY (type) REFERENCES enum_health_monitor_type(id)
) ENGINE=InnoDB;

DROP TABLE IF EXISTS `rule`;
CREATE TABLE `rule` (
    `id` int(32) NOT NULL,
    `type` varchar(32) DEFAULT NULL,
    `condition` varchar(128) DEFAULT NULL,
    PRIMARY KEY (`id`),
    CONSTRAINT `fk_r_type` FOREIGN KEY (type) REFERENCES `enum_rule_type`(name)
) ENGINE=InnoDB;

DROP TABLE IF EXISTS `ssl_decrypt`;
CREATE TABLE `ssl_decrypt` (
    `id` int(32) NOT NULL,
    `tenant_id` varchar(128) DEFAULT NULL
    `barbican_uuid` varchar(128) DEFAULT NULL,
    `enabled` int(1) DEFAULT 0,
    PRIMARY KEY (`id`),
) ENGINE=InnoDB;

DROP TABLE IF EXISTS `ssl_encrypt`;
CREATE TABLE `ssl_encrypt` (
    `id` int(32) NOT NULL,
    `barbican_uuid` varchar(128) DEFAULT NULL,
    `enabled` int(1) DEFAULT 0,
    PRIMARY KEY (`id`),
) ENGINE=InnoDB;

DROP TABLE IF EXISTS `tls_certificate`;
CREATE TABLE `ssl_encrypt` (
    `id` int(32) NOT NULL,
    `tenant_id` varchar(128) DEFAULT NULL
    `barbican_uuid` varchar(128) DEFAULT NULL,
    `simple_certificate_data` varchar(128) DEFAULT NULL,
    PRIMARY KEY (`id`),
) ENGINE=InnoDB;

DROP TABLE IF EXISTS `vip`;
CREATE TABLE `vip` (
    `id` int(32) NOT NULL,
    `tenant_id` varchar(128) DEFAULT NULL
    `subnet_id` varchar(32) DEFAULT NULL,
    `type` varchar(32) DEFAULT NULL,
    PRIMARY KEY (`id`),
    CONSTRAINT `fk_v_type` FOREIGN KEY (session_persistence) REFERENCES enum_vip_type(id)
) ENGINE=InnoDB;

DROP TABLE IF EXISTS `load_balancer`;
CREATE TABLE `load_balancer` (
    `id` int(32) NOT NULL AUTO_INCREMENT,
    `tenant_id` varchar(128) DEFAULT NULL
    `ssl_decrypt_id` int(32) DEFAULT NULL,
    `tls_certificate_id` int(32) DEFAULT NULL,
    `name` varchar(128) DEFAULT NULL,
    `content_switching` int(1) DEFAULT 0,
    `port` int(11) DEFAULT NULL,
    `protocol` varchar(32) DEFAULT NULL,
    `status` varchar(32) DEFAULT NULL,
    PRIMARY KEY (`id`),
    CONSTRAINT `fk_g_status` FOREIGN KEY (status) REFERENCES `enum_lbaas_status`(name),
    CONSTRAINT `fk_g_ut` FOREIGN KEY (update_type) REFERENCES `enum_update_type`(name),
    CONSTRAINT  `fk_g_algo` FOREIGN KEY (algorithm) REFERENCES `enum_glb_algorithm`(name),
    CONSTRAINT `fk_p_ssl_decrypt` FOREIGN KEY (ssl_decrypt_id) REFERENCES ssl_decrypt(id)
    CONSTRAINT `fk_p_tls_cert` FOREIGN KEY (tls_certificate_id) REFERENCES tls_certificate(id)
) ENGINE=InnoDB;

DROP TABLE IF EXISTS `lb_vip`;
CREATE TABLE `lb_vip` (
    `lb_id` int(32) NOT NULL,
    `vip_id` varchar(128) DEFAULT NULL,
    PRIMARY KEY (`lb_id`, `vip_id`),
    CONSTRAINT `fk_v_lb_id` FOREIGN KEY (lb_id) REFERENCES load_balancer(id),
    CONSTRAINT `fk_v_vip_id` FOREIGN KEY (vip_id) REFERENCES vip(id)
) ENGINE=InnoDB;

DROP TABLE IF EXISTS `lb_pool`;
CREATE TABLE `lb_pool` (
    `lb_id` int(32) NOT NULL,
    `pool_id` varchar(128) DEFAULT NULL,
    `default` int(1) DEFAULT 0,
    PRIMARY KEY (`lb_id`, `vip_id`),
    CONSTRAINT `fk_p_lb_id` FOREIGN KEY (lb_id) REFERENCES load_balancer(id),
    CONSTRAINT `fk_p_pool_id` FOREIGN KEY (pool_id) REFERENCES pool(id)
) ENGINE=InnoDB;

DROP TABLE IF EXISTS `lb_pool_rule`;
CREATE TABLE `lb_pool_rule` (
    `lb_id` int(32) NOT NULL,
    `pool_id` int(32) DEFAULT NULL,
    `rule_id` int(32) DEFAULT NULL,
    PRIMARY KEY (`lb_id`, `pool_id`, `rule_id`),
    CONSTRAINT `fk_lbpr_lb_id` FOREIGN KEY (lb_id) REFERENCES load_balancer(id),
    CONSTRAINT `fk_lbpr_pool_id` FOREIGN KEY (pool_id) REFERENCES pool(id),
    CONSTRAINT `fk_lbpr_rule_id` FOREIGN KEY (rule_id) REFERENCES rule(id)
) ENGINE=InnoDB;

DROP TABLE IF EXISTS `enum_lbaas_protocol`;
CREATE TABLE `enum_lbaas_protocol` (
    `name` varchar(32) DEFAULT NULL,
    `description` varchar(128) DEFAULT NULL,
    PRIMARY KEY (`name`)
) ENGINE=InnoDB;

DROP TABLE IF EXISTS `enum_lbaas_status`;
CREATE TABLE `enum_lbaas_status` (
    `name` varchar(32) DEFAULT NULL,
    `description` varchar(128) DEFAULT NULL,
    PRIMARY KEY (`name`)
) ENGINE=InnoDB;

DROP TABLE IF EXISTS `enum_member_status`;
CREATE TABLE `enum_member_status` (
    `name` varchar(32) DEFAULT NULL,
    `description` varchar(128) DEFAULT NULL,
    PRIMARY KEY (`name`)
) ENGINE=InnoDB;

DROP TABLE IF EXISTS `enum_member_condition`;
CREATE TABLE `enum_member_condition` (
    `name` varchar(32) DEFAULT NULL,
    `description` varchar(128) DEFAULT NULL,
    PRIMARY KEY (`name`)
) ENGINE=InnoDB;

DROP TABLE IF EXISTS `enum_vip_type`;
CREATE TABLE `enum_vip_type` (
    `name` varchar(32) DEFAULT NULL,
    `description` varchar(128) DEFAULT NULL,
    PRIMARY KEY (`name`)
) ENGINE=InnoDB;

DROP TABLE IF EXISTS `enum_rule_type`;
CREATE TABLE `enum_rule_type` (
    `name` varchar(32) DEFAULT NULL,
    `description` varchar(128) DEFAULT NULL,
    PRIMARY KEY (`name`)
) ENGINE=InnoDB;

DROP TABLE IF EXISTS `enum_health_monitor_type`;
CREATE TABLE `enum_health_monitor_type` (
    `name` varchar(32) DEFAULT NULL,
    `description` varchar(128) DEFAULT NULL,
    PRIMARY KEY (`name`)
) ENGINE=InnoDB;

DROP TABLE IF EXISTS `enum_pool_algorithm`;
CREATE TABLE `enum_pool_algorithm` (
    `name` varchar(32) DEFAULT NULL,
    `description` varchar(128) DEFAULT NULL,
    PRIMARY KEY (`name`)
) ENGINE=InnoDB;

INSERT INTO `enum_rule_type` VALUES('PATH', 'Path');

INSERT INTO `enum_health_monitor_type` VALUES('HTTP', 'Http');
INSERT INTO `enum_health_monitor_type` VALUES('HTTPS', 'Https');
INSERT INTO `enum_health_monitor_type` VALUES('CONNECT', 'Connect');

INSERT INTO `enum_lbaas_protocol` VALUES('HTTP', 'HTTP');
INSERT INTO `enum_lbaas_protocol` VALUES('HTTPS', 'HTTPS');
INSERT INTO `enum_lbaas_protocol` VALUES('TCP', 'TCP');

INSERT INTO `enum_lbaas_status` VALUES('ACTIVE', 'Active');
INSERT INTO `enum_lbaas_status` VALUES('BUILD', 'Build');
INSERT INTO `enum_lbaas_status` VALUES('DELETED', 'Deleted');
INSERT INTO `enum_lbaas_status` VALUES('PENDING_DELETE', 'Pending Delete');
INSERT INTO `enum_lbaas_status` VALUES('PENDING_UPDATE', 'Pending Update');
INSERT INTO `enum_lbaas_status` VALUES('QUEUED', 'Queue');
INSERT INTO `enum_lbaas_status` VALUES('NONE', 'Nada');

INSERT INTO `enum_member_status` VALUES('OFFLINE', 'Member is offline');
INSERT INTO `enum_member_status` VALUES('ONLINE', 'Member is online');
INSERT INTO `enum_member_status` VALUES('UNKNOWN', 'Member is in an unknown status');

INSERT INTO `enum_member_condition` VALUES('ENABLED', 'Enabled');
INSERT INTO `enum_member_condition` VALUES('DISABLED', 'Disabled');
INSERT INTO `enum_member_condition` VALUES('DRAINING', 'Draining');


INSERT INTO `enum_vip_type` VALUES('IPV4', 'IPv4');
INSERT INTO `enum_vip_type` VALUES('IPV6', 'IPv6');

INSERT INTO `enum_pool_algorithm` VALUES('ROUND_ROBIN', 'Round robin');
INSERT INTO `enum_pool_algorithm` VALUES('LEAST_CONNECTIONS', 'Least connections');


set unique_checks=1;
set foreign_key_checks=1;
COMMIT;
