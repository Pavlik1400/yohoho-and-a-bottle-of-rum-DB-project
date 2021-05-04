

CREATE TABLE alcoholic (
	id_alc SERIAL PRIMARY KEY,
	fname varchar(30),
	lname varchar(30)
);

CREATE TABLE inspector (
	id_ins SERIAL PRIMARY KEY,
	fname varchar(30),
	lname varchar(30)
);

CREATE TABLE bed (
	id_bed SERIAL PRIMARY KEY,
	description varchar(200)
);

CREATE TABLE escape (
	id_esc SERIAL PRIMARY KEY,
	id_alc INTEGER NOT NULL,
	escape_date TIMESTAMP NOT NULL,
	bribe_id INTEGER
);

CREATE TABLE log (
	id_log SERIAL PRIMARY KEY,
	id_alc integer not null,
	id_insp_out integer,
	id_bed integer not null,
	id_group_check_in integer not null, 
	end_date timestamp not null
);

CREATE TABLE group_info (
	id_group SERIAL PRIMARY KEY,
	group_name varchar(100)
);

CREATE TABLE active_alcoholic (
	id_act SERIAL PRIMARY KEY,
  	id_alc integer not null,
	id_bed integer not null,
	id_group_check_in integer not null  	
);

CREATE TABLE bribe (
	id_bribe SERIAL PRIMARY KEY,
	id_ins integer not null,
  price integer not null
);

CREATE TABLE group_check_in (
	id_check_in SERIAL PRIMARY KEY,
	id_group integer, 
	time timestamp,
	id_drink integer,
	inspector_in integer not null
);

CREATE TABLE drink (
	id_drink SERIAL PRIMARY KEY,
	drink_name varchar(100) not null,
	price integer
);

CREATE TABLE unconsciousness(
	id_unc SERIAL not null PRIMARY KEY,
	id_alc integer not null,
	begin_time timestamp,
	end_time timestamp
);

CREATE TABLE job (
	id_job serial not null PRIMARY KEY,
	id_alc integer not null,
	job_name varchar(50),
	begin_time timestamp not null,
	end_time timestamp not null
);
