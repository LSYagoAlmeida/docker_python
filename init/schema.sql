CREATE DATABASE teste;

CREATE TABLE IF NOT EXISTS `teste`.`users`(
  id int AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(255) NOT NULL
) ENGINE=INNODB;