drop table death;
drop table alive;

create table death
(
	death_id SERIAL PRIMARY KEY,
	
	fname int,
	lname int
);

create table alive
(
	id_al SERIAL PRIMARY KEY,
	fname int,
	lname int
);



CREATE OR REPLACE FUNCTION insert_to_death()
  RETURNS trigger AS
$$
BEGIN
    DELETE FROM alive
         where fname = cast (NEW.fname as int) ;
RETURN NEW;
END;
$$
LANGUAGE 'plpgsql';


drop trigger death_insert on death;

CREATE TRIGGER death_insert
  AFTER INSERT
  ON death
  FOR EACH ROW
  EXECUTE PROCEDURE insert_to_death();
	
INSERT INTO alive(fname, lname) VALUES (1, 1);

INSERT INTO alive(fname, lname) VALUES (2, 2);

INSERT INTO death(fname, lname) VALUES (2, 2);
INSERT INTO death(fname, lname) VALUES (1, 1);


select * from alive;
	
	
	
	
	
	

