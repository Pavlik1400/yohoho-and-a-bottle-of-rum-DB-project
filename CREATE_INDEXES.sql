CREATE INDEX Bribe_Price_Btree ON bribe(price);

CREATE INDEX Escape_EscapeDate_Btree ON escape(escape_date);

CREATE INDEX Log_EndDate_Btree ON log(end_date);

CREATE INDEX GroupCheckIn_Time_Btree ON group_check_in(time);

CREATE INDEX Drink_Price_Btree ON drink(price);

CREATE INDEX Unconsciousness_BeginTime_Btree ON unconsciousness(begin_time);
CREATE INDEX Unconsciousness_EndTime_Btree ON unconsciousness(end_time);

CREATE INDEX Job_BeginTime_Btree ON job(begin_time);
CREATE INDEX Job_EndTime_Btree ON job(end_time);
