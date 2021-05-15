-- • знайти усiх алкоголiкiв, яких забирали у витверезник хоча б N разiв за вказаний перiод (з дати F по дату T);


	SELECT id_alc FROM 
	log JOIN group_check_in 
		ON group_check_in.id_check_in = log.id_group_check_in
	WHERE time >= '2020-04-29 12:00:00' AND end_date <= '2021-05-10 22:30:00' -- input date
	
	UNION
	
	SELECT id_alc FROM 
	active_alcoholic JOIN group_check_in 
		ON group_check_in.id_check_in = active_alcoholic.id_group_check_in
	WHERE time >= '2020-04-29 12:00:00' -- input date
	
	GROUP BY id_alc
	HAVING COUNT(id_alc) >= 1 -- N

-- • знайти усi спiльнi подiї для алкоголiка A та iнспектора I за вказаний перiод (з дати F по дату T);


	SELECT id_alc, inspector_in FROM 
	log JOIN group_check_in 
		ON group_check_in.id_check_in = log.id_group_check_in
	WHERE time >= '2020-04-29 12:00:00' AND end_date <= '2021-05-10 22:30:00' -- input date
		  AND (inspector_in = 4 or id_insp_out = 4) AND id_alc = 7 -- input inspectors and alcoholics
		 
	UNION
	
	SELECT id_alc, inspector_in FROM 
	active_alcoholic JOIN group_check_in 
		ON group_check_in.id_check_in = active_alcoholic.id_group_check_in
	WHERE time >= '2020-04-29 12:00:00' AND (inspector_in = 4) AND id_alc = 7 -- input date, inspectors and alcoholics



-- • для алкоголiка A та кожного спиртого напою, що вiн вживав, знайти скiльки разiв за вказаний 
--   перiод (з дати F по дату T) вiн розпивав напiй у групi з щонайменше N алкоголiкiв; ??

	
	SELECT id_drink, COUNT(id_drink)
	FROM log
	JOIN group_check_in
	ON log.id_group_check_in = group_check_in.id_check_in
	WHERE time >= '2020-04-29 12:00:00' AND end_date <= '2021-05-10 22:30:00' AND id_alc = 4 -- input date, inspectors and alcoholics
	GROUP BY id_drink, id_group_check_in
	HAVING COUNT(id_group_check_in) > 0 -- N
	
	UNION
	
	SELECT id_drink, COUNT(id_drink)
	FROM active_alcoholic
	JOIN group_check_in
	ON active_alcoholic.id_group_check_in = group_check_in.id_check_in
	WHERE time >= '2020-04-29 12:00:00' AND id_alc = 4 -- input date and alcoholic
	GROUP BY id_drink, id_group_check_in
	HAVING COUNT(id_group_check_in) > 0 -- N


-- • знайти сумарну кiлькiсть втеч з витверезника по мiсяцях;

	SELECT COUNT(id_alc), EXTRACT(MONTH FROM escape_date)
	FROM escape
	GROUP BY EXTRACT(MONTH FROM escape_date)


-- • вивести лiжка витверезника у порядку спадання середньої кiлькостi втрат свiдомостi для усiх 
--   алкоголiкiв, що були приведенi на лiжко iнспектором I за вказаний перiод (з дати F по дату T);


	SELECT id_bed, ROUND(COUNT(id_unc)/COUNT(id_bed), 2)
	FROM (log
	JOIN unconsciousness
		ON log.id_alc = unconsciousness.id_alc) as log_unc
	JOIN group_check_in
		ON group_check_in.id_check_in = log_unc.id_group_check_in
	WHERE inspector_in = 8 AND time >= '2020-04-29 12:00:00' AND end_date <= '2021-05-10 22:30:00' -- input dates and inspector
	GROUP BY id_bed
	ORDER BY ROUND(COUNT(id_unc)/COUNT(id_bed), 2) DESC


-- • вивести алкогольнi напої у порядку спадання сумарної кiлькостi алкоголiкiв, що його розпивала 
--   разом з алкоголiком A за вказаний перiод (з дати F по дату T);

	
	SELECT id_drink, COUNT(id_group_check_in)
	FROM log
	JOIN group_check_in
	ON log.id_group_check_in = group_check_in.id_check_in
	WHERE time >= '2020-04-29 12:00:00' AND end_date <= '2021-05-10 22:30:00' AND id_alc = 4  -- input dates and alcoholics
	GROUP BY id_drink, id_group_check_in
	ORDER BY COUNT(id_group_check_in)
	
	UNION
	
	SELECT id_drink, COUNT(id_group_check_in)
	FROM active_alcoholic
	JOIN group_check_in
	ON active_alcoholic.id_group_check_in = group_check_in.id_check_in
	WHERE time >= '2020-04-29 12:00:00' AND id_alc = 4  -- input dates and alcoholics
	GROUP BY id_drink, id_group_check_in
 	ORDER BY COUNT(id_group_check_in)

