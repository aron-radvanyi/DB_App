-- script to create database 

CREATE DATABASE database_db_App;
CREATE USER 'your_user'@'localhost' IDENTIFIED BY '12345';
GRANT ALL PRIVILEGES ON your_database_name.* TO 'your_user'@'localhost';
FLUSH PRIVILEGES;
