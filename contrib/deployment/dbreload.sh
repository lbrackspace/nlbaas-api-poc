#!/bin/bash
SQL_FILE=$1
CONFIG_FILE=/etc/openstack/nlbaas/config.cfg

pw=$(awk -F'db_password=' '{print $2}' $CONFIG_FILE)
un=glb

echo "Recreating database and user privileges"
mysql -uroot -e"drop database if exists lbaas; create database lbaas; GRANT ALL PRIVILEGES ON lbaas.* TO $un@localhost IDENTIFIED BY '$pw'"

echo "Importing the sql file"
mysql -ulbaas -p$pw -Dlbaas <$SQL_FILE

echo "Displaying the created tables..."
echo | mysql -ulbaas -p$pw -e"use lbaas; show tables;"
