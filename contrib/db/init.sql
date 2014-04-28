CREATE DATABASE lbaas;
GRANT USAGE ON *.* TO 'lbaas'@'%' IDENTIFIED BY 'pass1234';
GRANT ALL PRIVILEGES ON lbaas.* TO 'lbaas'@'%';
GRANT USAGE ON *.* TO 'lbaas'@'localhost' IDENTIFIED BY 'pass1234';
GRANT ALL PRIVILEGES ON lbaas.* TO 'lbaas'@'localhost';
FLUSH PRIVILEGES;
