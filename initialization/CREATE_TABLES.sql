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

CREATE TABLE drink (
	id_drink SERIAL PRIMARY KEY,
	drink_name varchar(100) not null,
	price integer
);

CREATE TABLE group_info (
	id_group SERIAL PRIMARY KEY,
	group_name varchar(100)
);

CREATE TABLE bribe (
	id_bribe SERIAL PRIMARY KEY,
	id_ins integer not null,
	CONSTRAINT fk_id_ins
		FOREIGN KEY(id_ins) 
			REFERENCES inspector(id_ins)
			ON DELETE CASCADE,

  	price integer not null
);

CREATE TABLE group_check_in (
	id_check_in SERIAL PRIMARY KEY,
	id_group integer,
	CONSTRAINT fk_id_group
		FOREIGN KEY(id_group) 
			REFERENCES group_info(id_group)
			ON DELETE CASCADE,
	
	time timestamp,
	id_drink integer,
	CONSTRAINT fk_id_drink
		FOREIGN KEY(id_drink) 
			REFERENCES drink(id_drink)
			ON DELETE CASCADE,
	
	inspector_in integer not null,
		CONSTRAINT fk_inspector_in
		FOREIGN KEY(inspector_in) 
			REFERENCES inspector(id_ins)
			ON DELETE CASCADE
);

CREATE TABLE escape (
	id_esc SERIAL PRIMARY KEY,
	id_alc INTEGER NOT NULL,
	escape_date TIMESTAMP NOT NULL,
	bribe_id INTEGER,
	
	CONSTRAINT fk_id_alc
		FOREIGN KEY(id_alc) 
			REFERENCES alcoholic(id_alc)
			ON DELETE CASCADE,
	
	CONSTRAINT fk_bribe_id
		FOREIGN KEY(bribe_id) 
			REFERENCES bribe(id_bribe)
			ON DELETE CASCADE
);

CREATE TABLE log (
	id_log SERIAL PRIMARY KEY,
	
	id_alc integer not null,
	CONSTRAINT fk_id_alc
		FOREIGN KEY(id_alc) 
			REFERENCES alcoholic(id_alc)
			ON DELETE CASCADE,
	
	id_insp_out integer,
	CONSTRAINT fk_id_insp_out
		FOREIGN KEY(id_insp_out) 
			REFERENCES inspector(id_ins)
			ON DELETE CASCADE,
	
	id_bed integer not null,
	CONSTRAINT fk_id_bed
		FOREIGN KEY(id_bed) 
			REFERENCES bed(id_bed)
			ON DELETE CASCADE,
	
	id_group_check_in integer not null,
	CONSTRAINT fk_id_group_check_in
		FOREIGN KEY(id_group_check_in) 
			REFERENCES group_check_in(id_check_in)
			ON DELETE CASCADE,
	
	end_date timestamp not null
);


CREATE TABLE active_alcoholic (
	id_act SERIAL PRIMARY KEY,
	
  	id_alc integer not null,
	CONSTRAINT fk_id_alc
		FOREIGN KEY(id_alc) 
			REFERENCES alcoholic(id_alc)
			ON DELETE CASCADE,
	
	id_bed integer not null,
	CONSTRAINT fk_id_bed
		FOREIGN KEY(id_bed) 
			REFERENCES bed(id_bed)
			ON DELETE CASCADE,
	
	id_group_check_in integer not null, 
	CONSTRAINT fk_id_group_check_in
		FOREIGN KEY(id_group_check_in) 
			REFERENCES group_check_in(id_check_in)
			ON DELETE CASCADE
);

CREATE TABLE unconsciousness(
	id_unc SERIAL not null PRIMARY KEY,
	id_alc integer not null,
	CONSTRAINT fk_id_alc
	FOREIGN KEY(id_alc) 
		REFERENCES alcoholic(id_alc)
		ON DELETE CASCADE,
	
	begin_time timestamp,
	end_time timestamp
);

CREATE TABLE job (
	id_job serial not null PRIMARY KEY,
	id_alc integer not null,
	CONSTRAINT fk_id_alc
	FOREIGN KEY(id_alc) 
		REFERENCES alcoholic(id_alc)
		ON DELETE CASCADE,
	job_name varchar(50),
	begin_time timestamp not null,
	end_time timestamp not null
);

-- Drop table alcoholic cascade;
-- Drop table inspector cascade;
-- Drop table bed cascade;
-- Drop table escape cascade;
-- Drop table log cascade;
-- Drop table group_info cascade;
-- Drop table active_alcoholic cascade;
-- Drop table bribe cascade;
-- Drop table group_check_in ;
-- Drop table drink;
-- Drop table unconsciousness;
-- Drop table job;
