-- init.sql
DROP USER IF EXISTS 'myuser'@'%';
CREATE USER 'myuser'@'%' IDENTIFIED BY 'password';
CREATE DATABASE IF NOT EXISTS universidad;
GRANT ALL PRIVILEGES ON universidad.* TO 'myuser'@'%';
FLUSH PRIVILEGES;
