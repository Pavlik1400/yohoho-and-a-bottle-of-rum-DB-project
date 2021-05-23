
-- 13)
-- • За данний період часу скільки і (яку) роботу робив данний алколік

	SELECT job_name, COUNT(job_name)
	FROM job
	WHERE begin_time >= '2020-04-29 12:00:00' AND end_time <= '2021-05-10 22:30:00' AND id_alc = 10
	GROUP BY job_name


-- 14)
-- • Знайти алкоголіків які нічого не робили

	SELECT log.id_alc
	FROM log
	FULL JOIN job
	ON job.id_alc = log.id_alc
	WHERE id_job IS NULL

-- 15)
-- • Який алкоголік найпрацьовитіший

	SELECT id_alc, COUNT(id_alc)
	FROM job
	GROUP BY id_alc
	ORDER BY COUNT(id_alc) DESC
	LIMIT 1

-- 16)
-- • Найпопулярніша робота

	SELECT job_name, COUNT(job_name)
	FROM job
	GROUP BY job_name
	ORDER BY COUNT(job_name) DESC
	LIMIT 1

-- 17)
-- • Список алкоголіків які робили таку то роботу

	SELECT id_alc
	FROM job
	WHERE job_name = 'cleaning the floor'

-- 18)
-- • Топ найкорумпованіший інспекторів

	SELECT id_ins, COUNT(id_ins)
	FROM bribe
	GROUP BY id_ins
	ORDER BY COUNT(id_ins) DESC

-- 19)
-- • Хто найбільше взяток дає

	SELECT id_alc, COUNT(id_alc)
	FROM escape
	GROUP BY id_alc
	ORDER BY COUNT(id_alc) DESC


-- 20)
-- • Найбільша взятка

	SELECT price, id_ins, id_alc
	FROM bribe
	JOIN escape
	ON bribe.id_bribe = escape.bribe_id
	ORDER BY price DESC
	LIMIT 1


