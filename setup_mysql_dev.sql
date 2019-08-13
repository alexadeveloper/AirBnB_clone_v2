-- Create database user and grant permisisons
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
USE hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
USE performance_schema;
GRANT SELECT ON * TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
