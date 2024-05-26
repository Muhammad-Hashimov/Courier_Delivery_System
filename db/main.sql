CREATE TABLE courier.client (
	id BIGINT UNSIGNED auto_increment NOT NULL,
	Name varchar(100) NOT NULL,
	Surename varchar(100) NOT NULL,
	Age BIGINT UNSIGNED NOT NULL,
	`Number` varchar(100) NOT NULL,
	CONSTRAINT client_pk PRIMARY KEY (id)
)


CREATE TABLE courier.courier (
	Id BIGINT UNSIGNED auto_increment NOT NULL,
	Name varchar(100) NOT NULL,
	Surname varchar(100) NOT NULL,
	`Number` varchar(100) NOT NULL,
	CONSTRAINT courier_pk PRIMARY KEY (Id)
)