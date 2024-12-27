-- Create Users table
create table sdev_users (
	user_id   integer primary key,
	email     varchar(75) not null unique,
	firstname varchar(50) not null,
	lastname  varchar(75) not null,
	city      varchar(75),
	state     char(2),
	zip       varchar(10)
);

-- Create Roles table
create table roles (
	role_id integer primary key,
	role    varchar(20) not null unique
);

-- Create user-info table
create table user_info (
	user_id  integer primary key,
	password varchar(40) not null,
	constraint fk_wu2 foreign key ( user_id )
		references sdev_users ( user_id )
			on delete cascade
);

-- Create User roles table
create table user_roles (
	user_id integer not null,
	role_id integer not null,
	constraint pkur primary key ( user_id,
	                              role_id ),
	constraint fk_ur1 foreign key ( user_id )
		references sdev_users ( user_id )
			on delete cascade,
	constraint fk_ur2 foreign key ( role_id )
		references roles ( role_id )
			on delete cascade
);

-- Create Account data table
create table customeraccount (
	account_id     integer primary key,
	user_id        integer not null
		references sdev_users ( user_id ),
	cardholdername varchar(75) not null,
	cardtype       varchar(20) not null,
	servicecode    varchar(20) not null,
	cardnumber     varchar(30) not null,
	cav_ccv2       integer not null,
	expiredate     date not null,
	fulltrackdata  varchar(75) not null,
	pin            varchar(10) not null
);

-- Insert records into sdev_users
insert into sdev_users (
	user_id,
	email,
	firstname,
	lastname,
	city,
	state,
	zip
) values ( 1,
           'james.robertson@umgc.edu',
           'Jim',
           'Robertson',
           'Adelphi',
           'MD',
           '20706' );

-- Create a Fake Admin account for testing
insert into sdev_users (
	user_id,
	email,
	firstname,
	lastname,
	city,
	state,
	zip
) values ( 2,
           'test.admin@umgc.edu',
           'Test',
           'Admin',
           'Adelphi',
           'MD',
           '20706' );

-- Create a Fake Customer account for testing
insert into sdev_users (
	user_id,
	email,
	firstname,
	lastname,
	city,
	state,
	zip
) values ( 3,
           'test.customer@umgc.edu',
           'Test',
           'Customer',
           'Adelphi',
           'MD',
           '20706' );

-- Insert records into user_info
insert into user_info (
	user_id,
	password
) values ( 1,
           'mypassword' );

insert into user_info (
	user_id,
	password
) values ( 2,
           'adminpasstest' );

insert into user_info (
	user_id,
	password
) values ( 3,
           'customerpasstest' );

-- Insert records into roles
insert into roles (
	role_id,
	role
) values ( 1,
           'Customer' );

insert into roles (
	role_id,
	role
) values ( 2,
           'Admin' );

-- Insert records into user_roles
insert into user_roles (
	user_id,
	role_id
) values ( 1,
           1 );

insert into user_roles (
	user_id,
	role_id
) values ( 1,
           2 );

insert into user_roles (
	user_id,
	role_id
) values ( 2,
           2 );

insert into user_roles (
	user_id,
	role_id
) values ( 3,
           1 );

-- Insert records into CustomerAccount
insert into customeraccount (
	account_id,
	user_id,
	cardtype,
	servicecode,
	cardnumber,
	cav_ccv2,
	cardholdername,
	expiredate,
	fulltrackdata,
	pin
) values ( 1,
           1,
           'MasterCard',
           '27aD',
           '1111111111111',
           321,
           'James Robertson',
           '2016-02-23',
           '3323344ASDfc23442',
           '3Ds2q' );

insert into customeraccount (
	account_id,
	user_id,
	cardtype,
	servicecode,
	cardnumber,
	cav_ccv2,
	cardholdername,
	expiredate,
	fulltrackdata,
	pin
) values ( 2,
           2,
           'Visa',
           '34q4',
           '222222222222',
           365,
           'Test Administrator',
           '2018-09-16',
           '9852QDFXu43678',
           '9w21Q' );

insert into customeraccount (
	account_id,
	user_id,
	cardtype,
	servicecode,
	cardnumber,
	cav_ccv2,
	cardholdername,
	expiredate,
	fulltrackdata,
	pin
) values ( 3,
           3,
           'AMEX',
           '48w5',
           '333333333333',
           439,
           'Test Customer',
           '2019-05-30',
           '65234qwpH39302',
           '92ERS2' );

-- cd "C:\Users\brian\3. Programs\DB_Derby\bin"
-- ./ij
-- ij statements to create database and exicute .sql files
-- connect 'jdbc:derby:C:\Users\brian\2. Code\School Code\1. Java\School Code\SDEV 425\SDEV425_HW4\SDEV425_HW4\SDEV425;create=true;user=sdev425;password=sdev425';
-- RUN 'C:\Users\brian\2. Code\School Code\4. SQL\School Code\SDEV425\createHW4Tables.sql';
-- RUN 'C:\Users\brian\2. Code\School Code\4. SQL\School Code\SDEV425\selectAllTables.sql';