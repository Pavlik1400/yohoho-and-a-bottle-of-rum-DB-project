-- для алкоголiка A знайти усiх iнспекторiв, якi забирали його у витверезник принаймнi N разiв за вказаний перiод (з дати F по дату T);

SELECT inspector_in FROM
log INNER JOIN group_check_in 
ON group_check_in.id_check_in = log.id_group_check_in
INNER JOIN alcoholic ON alcoholic.id_alc = log.id_alc
WHERE time >= '2020-01-29 12:00:00' AND end_date <= '2021-05-10 22:30:00'
AND (alcoholic.id_alc=5)  -- тут потрібно вказати id бажаного алкоголіка A
GROUP BY inspector_in HAVING COUNT(log.id_alc)>=1; -- тут потрібно вказати N

-- для алкоголiка A знайти усi лiжка витверезника, де вiн побував за вказаний перiод (з дати F по дату T);

SELECT id_bed FROM
log INNER JOIN group_check_in 
ON group_check_in.id_check_in = log.id_group_check_in
INNER JOIN alcoholic ON alcoholic.id_alc = log.id_alc
WHERE time >= '2020-01-29 12:00:00' AND end_date <= '2021-05-10 22:30:00'
AND (alcoholic.id_alc=5)  -- тут потрібно вказати id бажаного алкоголіка A
GROUP BY id_bed;

-- для iнспектора I знайти усiх алкоголiкiв, яких вiн забирав хоча б N разiв за вказаний перiод (з дати F по дату T);

SELECT id_alc FROM
log INNER JOIN group_check_in 
ON group_check_in.id_check_in = log.id_group_check_in
INNER JOIN inspector ON inspector.id_ins=group_check_in.inspector_in
WHERE time >= '2020-01-29 12:00:00' AND end_date <= '2021-05-10 22:30:00'
AND (inspector.id_ins=2) -- тут потрібно вказати id бажаного інспектора I
GROUP BY (id_alc) HAVING COUNT (id_alc)>=1; -- тут потрібно вказати N

-- для алкоголiка A знайти усi лiжка у витверезнику, з яких вiн тiкав за вказаний перiод (з дати F по дату T);

SELECT id_bed FROM
log INNER JOIN escape
ON log.id_alc=escape.id_alc
INNER JOIN alcoholic ON alcoholic.id_alc = log.id_alc
WHERE escape_date>='2020-01-29 12:00:00' AND escape_date<= '2021-05-10 22:30:00'
AND (alcoholic.id_alc=2) -- тут потрібно вказати id бажаного алкоголіка A
GROUP BY id_bed; 

-- для алкоголiка A знайти усiх iнспекторiв, якi забирали його меншу кiлькiсть разiв нiж випускали;

SELECT inspector_in FROM
log INNER JOIN group_check_in 
ON group_check_in.id_check_in = log.id_group_check_in
INNER JOIN alcoholic ON alcoholic.id_alc = log.id_alc
WHERE alcoholic.id_alc=5 -- тут потрібно вказати id бажаного алкоголіка A
GROUP BY inspector_in HAVING COUNT(id_insp_out)>COUNT(inspector_in); 

-- знайти усiх iнспекторiв, якi забирали щонайменше N рiзних алкоголiкiв за вказаний перiод (з дати F по дату T);

SELECT inspector_in FROM
log INNER JOIN group_check_in 
ON group_check_in.id_check_in = log.id_group_check_in
WHERE time >= '2020-01-29 12:00:00' AND end_date <= '2021-05-10 22:30:00'
GROUP BY inspector_in HAVING COUNT(DISTINCT id_alc)>=3; -- тут потрібно вказати N



