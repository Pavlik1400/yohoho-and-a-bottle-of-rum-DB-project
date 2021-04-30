-- • знайти усiх алкоголiкiв, яких забирали у витверезник хоча б N разiв за вказаний перiод (з дати F по дату T);
select * from group_check_in
select * from log

	SELECT id_alc FROM 
	log JOIN group_check_in 
		ON group_check_in.id_check_in = log.id_group_check_in
	WHERE time >= '2020-04-29 12:00:00' AND end_date <= '2021-05-10 22:30:00'
	
	UNION
	
	SELECT id_alc FROM 
	active_alcoholic JOIN group_check_in 
		ON group_check_in.id_check_in = active_alcoholic.id_group_check_in
	WHERE time >= '2020-04-29 12:00:00'
	
	GROUP BY id_alc
	HAVING COUNT(id_alc) >= 1

-- • знайти усi спiльнi подiї для алкоголiка A та iнспектора I за вказаний перiод (з дати F по дату T);

-- 	// Спільні події - це який інспектор випускав/забирав якого алкоголіка?
-- 	// Тоді тут забирання
-- select * from group_check_in where inspector_in = 4
-- select * from log where id_group_check_in = 4

	SELECT id_alc, inspector_in FROM 
	log JOIN group_check_in 
		ON group_check_in.id_check_in = log.id_group_check_in
	WHERE time >= '2020-04-29 12:00:00' AND end_date <= '2021-05-10 22:30:00' 
		  AND (inspector_in = 4 or id_insp_out = 4) AND id_alc = 7
		 
	UNION
	
	SELECT id_alc, inspector_in FROM 
	active_alcoholic JOIN group_check_in 
		ON group_check_in.id_check_in = active_alcoholic.id_group_check_in
	WHERE time >= '2020-04-29 12:00:00' AND (inspector_in = 4) AND id_alc = 7


-- 	// Можна буде організувати табличку з історією алкоголіка і його перетин з інспекторами

-- • для алкоголiка A та кожного спиртого напою, що вiн вживав, знайти скiльки разiв за вказаний 
--   перiод (з дати F по дату T) вiн розпивав напiй у групi з щонайменше N алкоголiкiв; ??

	
	SELECT id_alc, id_drink, LENGTH (group_len)
	FROM log
	JOIN group_check_in
	ON log.group_id = group_check_in.group_id
	GROUP BY id_drink
	HAVING beg_date >= F AND end_date <= T AND id_drink==input_drink AND 
		LENGTH 
		(
			SELECT id_alc
			FROM log
			JOIN log AS l
			ON l.id_group = log.id_group


			SELECT COUNT(id_alc) FROM log
			GROUP BY id_group
			HAVING COUNT(id_alc) > N

		) > 0


-- • знайти сумарну кiлькiсть втеч з витверезника по мiсяцях;

	SELECT COUNT(id_alc), EXTRACT(MONTH FROM escape_date)
	FROM escape
	GROUP BY EXTRACT(MONTH FROM escape_date)


-- • вивести лiжка витверезника у порядку спадання середньої кiлькостi втрат свiдомостi для усiх 
--   алкоголiкiв, що були приведенi на лiжко iнспектором I за вказаний перiод (з дати F по дату T);


	SELECT id_bed, ROUND(COUNT(id_unc)/COUNT(id_bed), 2)
	FROM (log
	JOIN unconsciousness
		ON log.id_alc = unconsciousness.id_alc) as log_unc
	JOIN group_check_in
		ON group_check_in.id_check_in = log_unc.id_group_check_in
	WHERE inspector_in = 8 AND time >= '2020-04-29 12:00:00' AND end_date <= '2021-05-10 22:30:00' 
	GROUP BY id_bed
	ORDER BY ROUND(COUNT(id_unc)/COUNT(id_bed), 2) DESC


-- • вивести алкогольнi напої у порядку спадання сумарної кiлькостi алкоголiкiв, що його розпивала 
--   разом з алкоголiком A за вказаний перiод (з дати F по дату T);

	
	SELECT id_drink
	FROM group_check_in
	JOIN log
	ON group_check_in.id_check_in = log.id_group_check_in
	
	WHERE id_alc = 4
	ORDER BY (
				SELECT COUNT(*) FROM log
				GROUP BY id_group_check_in
			 ) DESC