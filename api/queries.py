QUERIES_REQUIRED_ARGS = {
    1: ['id_alc', 'N', 'from_date', 'to_date'],
    2: ['id_alc', 'from_date', 'to_date'],
    3: ['id_ins', 'N', 'from_date', 'to_date'],
    4: ['id_alc', 'from_date', 'to_date'],
    5: ['id_alc'],
    6: ['N', 'from_date', 'to_date', 'from_date'],
    7: ['N', 'from_date', 'to_date', 'from_date'],
    8: ['id_alc', 'id_ins', 'from_date', 'to_date'],
    9: ['id_alc', 'N', 'from_date', 'to_date'],
    10: [],
    11: ['id_ins', 'from_date', 'to_date'],
    12: ['id_alc', 'from_date', 'to_date'],
    13: ['id_alc', 'from_date', 'to_date'],
    14: [],
    15: [],
    16: [],
    17: ['job_name'],
    18: [],
    19: [],
    20: [],
    21: ['fname', 'lname'],
    22: ['fname', 'lname']

}


def q1(args, session):
    q_res = session.execute(f"""
SELECT inspector_in FROM
log INNER JOIN group_check_in 
ON group_check_in.id_check_in = log.id_group_check_in
INNER JOIN alcoholic ON alcoholic.id_alc = log.id_alc
WHERE time >= '{args['from_date']}' AND end_date <= '{args['to_date']}'
AND (alcoholic.id_alc={args['id_alc']})
GROUP BY inspector_in HAVING COUNT(log.id_alc)>={args['N']};
""")
    return {'reponse': [{'inspector_in': row[0]} for row in q_res]}


def q2(args, session):
    q_res = session.execute(f"""
SELECT id_bed FROM
log INNER JOIN group_check_in 
ON group_check_in.id_check_in = log.id_group_check_in
INNER JOIN alcoholic ON alcoholic.id_alc = log.id_alc
WHERE time >= '{args['from_date']}' AND end_date <= '{args['to_date']}'
AND (alcoholic.id_alc={args['id_alc']})
GROUP BY id_bed;
""")
    return {'reponse': [{'id_bed': row[0]} for row in q_res]}


def q3(args, session):
    q_res = session.execute(f"""
SELECT id_alc FROM
log INNER JOIN group_check_in 
ON group_check_in.id_check_in = log.id_group_check_in
INNER JOIN inspector ON inspector.id_ins=group_check_in.inspector_in
WHERE time >= '{args['from_date']}' AND end_date <= '{args['to_date']}'
AND (inspector.id_ins={args['id_ins']})
GROUP BY (id_alc) HAVING COUNT (id_alc)>={args['N']};
""")
    return {'reponse': [{'id_alc': row[0]} for row in q_res]}


def q4(args, session):
    q_res = session.execute(f"""
SELECT id_bed FROM
log INNER JOIN escape
ON log.id_alc=escape.id_alc
INNER JOIN alcoholic ON alcoholic.id_alc = log.id_alc
WHERE escape_date>='{args['from_date']}' AND escape_date<= '{args['to_date']}'
AND (alcoholic.id_alc={args['id_alc']})
GROUP BY id_bed; 
""")
    return {'reponse': [{'id_bed': row[0]} for row in q_res]}


def q5(args, session):
    q_res = session.execute(f"""
SELECT inspector_in FROM
log INNER JOIN group_check_in 
ON group_check_in.id_check_in = log.id_group_check_in
INNER JOIN alcoholic ON alcoholic.id_alc = log.id_alc
WHERE alcoholic.id_alc={args['id_alc']}
GROUP BY inspector_in HAVING COUNT(id_insp_out)>COUNT(inspector_in); 
""")
    return {'reponse': [{'inspector_in': row[0]} for row in q_res]}


def q6(args, session):
    q_res = session.execute(f"""
SELECT inspector_in FROM
log INNER JOIN group_check_in 
ON group_check_in.id_check_in = log.id_group_check_in
WHERE time >= '{args['from_date']}' AND end_date <= '{args['to_date']}'
GROUP BY inspector_in HAVING COUNT(DISTINCT id_alc)>={args['N']};
""")
    return {'reponse': [{'inspector_in': row[0]} for row in q_res]}


def q7(args, session):
    q_res = session.execute(f"""
SELECT id_alc FROM 
log JOIN group_check_in 
    ON group_check_in.id_check_in = log.id_group_check_in
WHERE time >= '{args['from_date']}' AND end_date <= '{args['to_date']}'

UNION

SELECT id_alc FROM 
active_alcoholic JOIN group_check_in 
    ON group_check_in.id_check_in = active_alcoholic.id_group_check_in
WHERE time >= '{args['from_date']}'

GROUP BY id_alc
HAVING COUNT(id_alc) >= {args['N']}
""")
    return {'reponse': [{'id_alc': row[0]} for row in q_res]}


def q8(args, session):
    q_res = session.execute(f"""
SELECT id_alc, inspector_in FROM 
log JOIN group_check_in 
    ON group_check_in.id_check_in = log.id_group_check_in
WHERE time >= '{args['from_date']}' AND end_date <= '{args['to_date']}' 
      AND (inspector_in = {args['id_ins']} or id_insp_out = {args['id_ins']}) AND id_alc = {args['id_alc']}
     
UNION

SELECT id_alc, inspector_in FROM 
active_alcoholic JOIN group_check_in 
    ON group_check_in.id_check_in = active_alcoholic.id_group_check_in
WHERE time >= '{args['from_date']}' AND (inspector_in = {args['id_ins']}) AND id_alc = {args['id_alc']}
""")
    return {'reponse': [{'id_alc': row[0], 'inspector_in': row[1]} for row in q_res]}


def q9(args, session):
    q_res = session.execute(f"""
SELECT id_drink, COUNT(id_drink)
FROM log
JOIN group_check_in
ON log.id_group_check_in = group_check_in.id_check_in
WHERE time >= '{args['from_date']}' AND end_date <= '{args['to_date']}' AND id_alc = {args['id_alc']}
GROUP BY id_drink, id_group_check_in
HAVING COUNT(id_group_check_in) > {args['N']}

UNION

SELECT id_drink, COUNT(id_drink)
FROM active_alcoholic
JOIN group_check_in
ON active_alcoholic.id_group_check_in = group_check_in.id_check_in
WHERE time >= '{args['from_date']}' AND id_alc = {args['id_alc']}
GROUP BY id_drink, id_group_check_in
HAVING COUNT(id_group_check_in) > {args['N']}
""")
    return {'reponse': [{'id_drink': row[0], 'count': row[1]} for row in q_res]}


def q10(args, session):
    q_res = session.execute(f"""
SELECT COUNT(id_alc), EXTRACT(MONTH FROM escape_date)
FROM escape
GROUP BY EXTRACT(MONTH FROM escape_date)
""")
    return {'reponse': [{'count': row[0], 'date_part': row[1]} for row in q_res]}


def q11(args, session):
    q_res = session.execute(f"""
SELECT id_bed, ROUND(COUNT(id_unc)/COUNT(id_bed), 2)
FROM (log
JOIN unconsciousness
    ON log.id_alc = unconsciousness.id_alc) as log_unc
JOIN group_check_in
    ON group_check_in.id_check_in = log_unc.id_group_check_in
WHERE inspector_in = {args['id_ins']} AND time >= '{args['from_date']}' AND end_date <= '{args['to_date']}' -- input dates and inspector
GROUP BY id_bed
ORDER BY ROUND(COUNT(id_unc)/COUNT(id_bed), 2) DESC
""")
    return {'reponse': [{'id_bed': row[0], 'round': float(row[1])} for row in q_res]}


def q12(args, session):
    q_res = session.execute(f"""
SELECT id_drink, COUNT(id_group_check_in)
FROM log
JOIN group_check_in
ON log.id_group_check_in = group_check_in.id_check_in
WHERE time >= '{args['from_date']}' AND end_date <= '{args['to_date']}' AND id_alc = {args['id_alc']}  -- input dates and alcoholic
GROUP BY id_drink, id_group_check_in
ORDER BY COUNT(id_group_check_in)

UNION

SELECT id_drink, COUNT(id_group_check_in)
FROM active_alcoholic
JOIN group_check_in
ON active_alcoholic.id_group_check_in = group_check_in.id_check_in
WHERE time >= '{args['from_date']}' AND id_alc = {args['id_alc']}  -- input begin date and alcoholic
GROUP BY id_drink, id_group_check_in
ORDER BY COUNT(id_group_check_in)
""")
    return {'reponse': [{'id_drink': row[0], 'count': int(row[1])} for row in q_res]}


def q13(args, session):
    q_res = session.execute(f"""
SELECT job_name, COUNT(job_name)
FROM job
WHERE begin_time >= '{args['from_date']}' AND end_time <= '{args['to_date']}' AND id_alc = {args['id_alc']}
GROUP BY job_name
""")
    return {'reponse': [{'job_name': row[0], 'count': int(row[1])} for row in q_res]}


def q14(args, session):
    q_res = session.execute(f"""
SELECT log.id_alc
FROM log
FULL JOIN job
ON job.id_alc = log.id_alc
WHERE id_job IS NULL
""")
    return {'reponse': [{'id_alc': row[0]} for row in q_res]}


def q15(args, session):
    q_res = session.execute(f"""
SELECT id_alc, COUNT(id_alc)
FROM job
GROUP BY id_alc
ORDER BY COUNT(id_alc) DESC
LIMIT 1
""")
    return {'reponse': [{'id_alc': row[0], 'count': int(row[1])} for row in q_res]}


def q16(args, session):
    q_res = session.execute(f"""
SELECT job_name, COUNT(job_name)
FROM job
GROUP BY job_name
ORDER BY COUNT(job_name) DESC
LIMIT 1
""")
    return {'reponse': [{'job_name': row[0], 'count': int(row[1])} for row in q_res]}


def q17(args, session):
    q_res = session.execute(f"""
SELECT id_alc
FROM job
WHERE job_name = '{args['job_name']}'
""")
    return {'reponse': [{'id_alc': row[0]} for row in q_res]}


def q18(args, session):
    q_res = session.execute(f"""
SELECT id_ins, COUNT(id_ins)
FROM bribe
GROUP BY id_ins
ORDER BY COUNT(id_ins) DESC
""")
    return {'reponse': [{'id_ins': row[0], 'count': int(row[1])} for row in q_res]}


def q19(args, session):
    q_res = session.execute(f"""
SELECT id_alc, COUNT(id_alc)
FROM escape
GROUP BY id_alc
ORDER BY COUNT(id_alc) DESC
""")
    return {'reponse': [{'id_alc': row[0], 'count': int(row[1])} for row in q_res]}


def q20(args, session):
    q_res = session.execute(f"""
SELECT price, id_ins, id_alc
FROM bribe
JOIN escape
ON bribe.id_bribe = escape.bribe_id
ORDER BY price DESC
LIMIT 1
""")
    return {'reponse': [{'price': row[0], 'id_ins': row(1), 'id_alc': row[2]} for row in q_res]}

def q21(args, session):
    q_res = session.execute(f"""
SELECT fname, lname, COUNT(id_bribe)
FROM inspector AS inspector INNER JOIN bribe ON bribe.id_ins = inspector.id_ins
WHERE fname = '{args['fname']}' AND lname = '{args['lname']}' 
GROUP BY fname, lname
ORDER BY COUNT(fname) DESC
""")
    return {'reponse': [{'Name': [row[0], row[1]], 'Number of bribes': int(row[2])} for row in q_res]}

def q22(args, session):
    q_res = session.execute(f"""
SELECT COUNT(id_alc)
FROM inspector AS inspector INNER JOIN log ON log.id_insp_out = inspector.id_ins
WHERE fname = '{args['fname']}' AND lname = '{args['lname']}'
""")
    return {'reponse': [{'Number of alcoholics': int(row[0])} for row in q_res]}

QUERY_FUNCS = {
    1: q1,
    2: q2,
    3: q3,
    4: q4,
    5: q5,
    6: q6,
    7: q7,
    8: q8,
    9: q9,
    10: q10,
    11: q11,
    12: q12,
    13: q13,
    14: q14,
    15: q15,
    16: q16,
    17: q17,
    18: q18,
    19: q19,
    20: q20,
    21: q21,
    22: q22

}



