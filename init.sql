-- init.sql
CREATE DATABASE IF NOT EXISTS universidad;
CREATE USER 'myuser'@'%' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON universidad.* TO 'myuser'@'%';
FLUSH PRIVILEGES;
