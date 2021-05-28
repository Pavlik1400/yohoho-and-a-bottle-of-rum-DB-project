CREATE OR REPLACE FUNCTION insert_to_log()
  RETURNS trigger AS
$$
BEGIN
    DELETE FROM active_alcoholic
         where id_alc = cast (NEW.id_alc as int) ;
RETURN NEW;
END;
$$
LANGUAGE 'plpgsql';

-- drop trigger log_insert on log;

CREATE TRIGGER log_insert
  AFTER INSERT
  ON log
  FOR EACH ROW
  EXECUTE PROCEDURE insert_to_log();
 
 
CREATE OR REPLACE FUNCTION insert_to_escape()
  RETURNS trigger AS
$$
BEGIN
    DELETE FROM escape
         where id_alc = cast (NEW.id_alc as int) ;
RETURN NEW;
END;
$$
LANGUAGE 'plpgsql';

-- drop trigger escape_insert on escape;

CREATE TRIGGER escape_insert
  AFTER INSERT
  ON escape
  FOR EACH ROW
  EXECUTE PROCEDURE insert_to_escape();
