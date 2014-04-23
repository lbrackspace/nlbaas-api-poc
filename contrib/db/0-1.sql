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
    `id` varchar(128) NOT NULL,
    `name` varchar(128) DEFAULT NULL,
    `subnet_id` varchar(128) DEFAULT NULL,
    `session_persistence` varchar(32) DEFAULT NULL,
    `status` varchar(32) DEFAULT NULL,
    PRIMARY KEY (`id`),
    CONSTRAINT `fk_p_sp` FOREIGN KEY (session_persistence) REFERENCES enum_pool_session_persistence(id)
) ENGINE=InnoDB;


DROP TABLE IF EXISTS `load_balancer`;
CREATE TABLE `load_balancer` (
    `id` varchar(128) NOT NULL AUTO_INCREMENT,
    `tenant_id` int(11) NOT NULL,
    `name` varchar(128) DEFAULT NULL,
    `port` int(11) DEFAULT NULL,
    `protocol` varchar(32) DEFAULT NULL,
    `status` varchar(32) DEFAULT NULL,
    `create_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
    `update_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
    `update_type` varchar(32) DEFAULT NULL,
    PRIMARY KEY (`id`),
    CONSTRAINT `fk_g_status` FOREIGN KEY (status) REFERENCES `enum_lbaas_status`(name),
    CONSTRAINT `fk_g_ut` FOREIGN KEY (update_type) REFERENCES `enum_update_type`(name),
    CONSTRAINT  `fk_g_algo` FOREIGN KEY (algorithm) REFERENCES `enum_glb_algorithm`(name)
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


set unique_checks=1;
set foreign_key_checks=1;
COMMIT;
