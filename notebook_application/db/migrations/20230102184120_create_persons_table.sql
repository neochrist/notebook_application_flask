-- migrate:up

CREATE TABLE person (
	id INTEGER PRIMARY KEY NOT NULL COMMENT 'Unique person id',
	person_name VARCHAR(50) NOT NULL COMMENT 'Name of the person',
    person_surname VARCHAR(50) NOT NULL COMMENT 'Surname of the person',
    phone_number VARCHAR(16) NOT NULL COMMENT 'phone number of the person',
    description TEXT COMMENT 'Non-necessary description of the person'

    ENGINE=InnoDB
	DEFAULT CHARSET=utf8

);

-- migrate:down

