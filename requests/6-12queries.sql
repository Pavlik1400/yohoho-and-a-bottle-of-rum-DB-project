• знайти усiх алкоголiкiв, яких забирали у витверезник хоча б N разiв за вказаний перiод (з дати F по дату T);

	SELECT id_alc FROM log
	GROUP BY id_alc
	HAVING beg_date >= F AND end_date <= T AND COUNT(id_alc) >= N

	SELECT id_alc FROM active_alcoholic
	GROUP BY id_alc
	HAVING beg_date >= F AND COUNT(id_alc) >= N

• знайти усi спiльнi подiї для алкоголiка A та iнспектора I за вказаний перiод (з дати F по дату T);

	// Спільні події - це який інспектор випускав/забирав якого алкоголіка?
	// Тоді тут забирання
	SELECT id_alc, id_insp_in FROM log
	WHERE beg_date >= F AND end_date <= T AND id_insp_in == I

	SELECT id_alc, inspector_in
	FROM active_alcoholic
	JOIN group
	ON group.id_group = active_alcoholic.group_id
	WHERE beg_date >= F AND inspector_in == I


	// А тут випускання
	SELECT id_alc, id_insp_out FROM log
	WHERE beg_date >= F AND end_date <= T AND id_insp_out == I

	// Можна буде організувати табличку з історією алкоголіка і його перетин з інспекторами

• для алкоголiка A та кожного спиртого напою, що вiн вживав, знайти скiльки разiв за вказаний перiод (з дати F по дату T) вiн розпивав напiй у групi з щонайменше N алкоголiкiв; ??

	
	SELECT id_alc, id_drink, LENGTH (group_len)
	FROM log
	JOIN group
	ON log.group_id = group.group_id
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


• знайти сумарну кiлькiсть втеч з витверезника по мiсяцях;

	SELECT COUNT(id_alc), EXTRACT(MONTH FROM when)
	FROM escape
	GROUP BY EXTRACT(MONTH FROM when)


• вивести лiжка витверезника у порядку спадання середньої кiлькостi втрат свiдомостi для усiх алкоголiкiв, що були приведенi на лiжко iнспектором I за вказаний перiод (з дати F по дату T);


	SELECT id_bed, AVG(id_unc)
	FROM log
	JOIN unconsciousness
	ON log.id_alc = unconsciousness.id_alc
	WHERE id_insp_in == I AND beg_date >= F AND end_date <= T
	GROUP BY id_bed
	ORDER BY AVG(id_unc) DESC


• вивести алкогольнi напої у порядку спадання сумарної кiлькостi алкоголiкiв, що його розпивала разом з алкоголiком A за вказаний перiод (з дати F по дату T);

	
	SELECT id_drink
	FROM group
	JOIN log
	ON group.id_group = log.id_group
	WHERE id_alc == A
	ORDER BY AVG(LENGTH(
			 (
				SELECT COUNT(id_alc) FROM log
				GROUP BY id_group
				HAVING id_alc == A
			 ))) DESC








