INSERT INTO alcoholic VALUES (1, 'John', 'Doe'), 
						(2,'Cameron', 'Grey'),
						(3, 'Brian', 'Somme'),
						(4, 'Drew', 'Johnson'),
						(5, 'Mandy', 'Scott'),
						(6, 'Reily', 'Markus'),
						(7, 'Thomas', 'Doris'),
						(8, 'Arthur', 'Lou'),
						(9, 'Mary', 'Veil'),
						(10, 'Jack', 'Swanson'),
						(11, 'Freddie', 'Ossie'),
						(12, 'Megan', 'Roffle'),
						(13, 'James', 'Birmin'),
						(14, 'Ronald', 'Bishop'),
						(15, 'Lorentz', 'Watts');


INSERT INTO inspector VALUES (1, 'Ben', 'Reilly'), 
						(2,'Thomas', 'Andersen'),
						(3, 'Bob', 'Stancy'),
						(4, 'Andrew', 'Likewick'),
						(5, 'Jim', 'Sober'),
						(6, 'Leslie', 'Hamilton'),
						(7, 'Thomas', 'Orlando'),
						(8, 'Aaron', 'Solomons'),
						(9, 'Mary', 'Jackson'),
						(10, 'Brad', 'Antler'),
						(11, 'Fred', 'Black');

INSERT INTO bed VALUES (1, 'ordinary'), 
						(2, 'without a mattress'),
						(3, 'ordinary'),
						(4, 'next to the toilet'),
						(5, 'ordinary'),
						(6, 'ordinary'),
						(7, 'with double mattress'),
						(8, 'ordinary'),
						(9, 'ordinary'),
						(10, 'ordinary'),
						(11, 'ordinary'),
						(12, 'ordinary');

INSERT INTO drink VALUES (1, 'Whisky', 400), 
						(2,'Vodka', 100),
						(3, 'Gin', 300),
						(4, 'Margarita', 500),
						(5, 'Beer', 50),
						(6, 'Brandy', 350),
						(7, 'Rum', 250),
						(8, 'Wine', 300),
						(9, 'Vermouth', 320),
						(10, 'Cognac', 280),
						(11, 'Cider', 260);

INSERT INTO group_info VALUES (1, 'whisky lovers'), 
						(2, 'celebrating people'),
						(3, NULL),
						(4, 'drinking gang'),
						(5, 'overachieving alcoholics'),
						(6, NULL),
						(7,  NULL),
						(8, NULL),
						(9, NULL),
						(10, NULL);

INSERT INTO group_check_in VALUES 
						(1, 1, ('2020-04-24 10:00:00+00'), 1, 1), 
						(2, 2, ('2020-04-29 12:00:00+00'), 2, 2),
						(3, 3, ('2020-04-30 00:00:00+00'), 4, 3),
						(4, 4, ('2020-05-01 00:00:00+00'), 3, 4),
						(5, 5, ('2020-05-05 00:00:00+00'), 5, 5),
						(6, 6, ('2020-05-06 00:00:00+00'), 6, 6),
						(7, 7, ('2020-05-08 00:00:00+00'), 8, 7),
						(8, 8, ('2020-05-09 00:00:00+00'), 7, 8),
						(9, 3, ('2020-05-09 19:00:00+00'), 9, 9),
						(10, 5, ('2021-04-24 10:00:00+00'), 10, 10),
						(11, 2, ('2021-04-28 10:00:00+00'), 11, 11),
						(12, 6, ('2021-04-28 20:00:00+00'), 1, 1),
						(13, 10, ('2021-04-29 20:00:00+00'), 2, 1);

INSERT INTO log VALUES (1, 1, 1, 1, 1, ('2020-04-28 10:00:00+00')), 
						(2, 2, NULL, 2, 1, ('2020-04-30 10:00:00+00')),
						(3, 3, NULL, 3, 1, ('2020-04-28 12:00:00+00')),
						(4, 4, 5, 3, 2, ('2020-04-30 10:00:00+00')),
						(5, 5, 5, 4, 2, ('2020-04-30 15:00:00+00')),
						(6, 6, NULL, 5, 3, ('2020-04-30 23:00:00+00')),
						(7, 7, NULL, 6, 4, ('2020-05-03 23:00:00+00')),
						(8, 8, NULL, 7, 4, ('2020-05-04 23:00:00+00')),
						(9, 9, 6, 8, 4, ('2020-05-05 23:00:00+00')),
						(10, 10, 10, 1, 5, ('2020-05-07 23:00:00+00')),
						(11, 11, NULL, 2, 5, ('2020-05-06 15:00:00+00')),
						(12, 12, 3, 3, 5, ('2020-05-06 23:00:00+00')),
						(13, 13, NULL, 4, 5, ('2020-05-06 23:00:00+00')),
						(14, 14, NULL, 5, 6, ('2020-05-07 23:00:00+00')),
						(15, 15, 6, 6, 6, ('2020-05-08 13:00:00+00')),							
						(16, 3, 6, 7, 6, ('2020-05-08 23:00:00+00')),
						(17, 5, 8, 8, 6, ('2020-05-08 23:30:00+00')),
						(18, 7, 9, 9, 7, ('2020-05-09 23:30:00+00')),
						(19, 2, NULL, 10, 7, ('2020-05-10 10:30+00')),
						(20, 1, NULL, 11, 7, ('2020-05-10 12:30:00+00')),
						(21, 4, NULL, 1, 8, ('2020-05-10 22:30:00+00')),
						(22, 6, 10, 3, 9, ('2020-05-11 22:30:00+00'));

INSERT INTO active_alcoholic VALUES (1, 10, 1, 10), 
						(2, 11, 2, 10), 
						(3, 12, 3, 10), 
						(4, 13, 4, 10), 
						(5, 4, 5, 11), 
						(6, 5, 6, 11), 
						(7, 14, 7, 12), 
						(8, 15, 8, 12), 
						(9, 3, 9, 12), 
						(10, 5, 10, 12), 
						(11, 9, 11, 13),
						(12, 8, 12, 13);

INSERT INTO unconsciousness VALUES (1, 1, ('2020-04-24 11:00:00+00'), 
											('2020-01-01 12:20:00+00')), 
									(2, 2, ('2020-04-24 10:05:00+00'), 
											('2020-04-24 10:20:00+00')),
									(3, 3, ('2020-04-24 11:00:00+00'), 
											('2020-04-25 10:00:00+00')), 
									(4, 4, ('2020-04-29 12:00:00+00'), 
											('2020-04-29 23:00:00+00')), 
									(5, 5, ('2020-04-29 12:20:00+00'), 
											('2020-04-29 22:00:00+00')),
									(6, 4, ('2020-04-29 23:30:00+00'), 
											('2020-04-29 23:50:00+00')),
									(7, 5, ('2020-04-29 22:20:00+00'), 
											('2020-04-30 10:00:00+00')), 
									(8, 6, ('2020-04-30 00:00:00+00'), 
											('2020-04-30 10:00:00+00')), 
									(9, 7, ('2020-05-01 10:00:00+00'), 
											('2020-05-01 11:00:00+00')), 
									(10, 8, ('2020-05-01 00:00:00+00'), 
											('2020-05-03 00:00:00+00')),
									(11, 8, ('2020-05-03 10:00:00+00'), 
											('2020-05-03 15:00:00+00')), 
									(12, 9, ('2020-05-01 00:00:00+00'), 
											('2020-05-02 00:00:00+00')), 
									(13, 12, ('2021-04-24 10:00:00+00'), 
											('2021-04-26 10:00:00+00')), 
									(14, 15, ('2021-04-28 20:00:00+00'), 
											('2021-04-29 20:00:00+00'));

INSERT INTO escape VALUES (1, 3, ('2020-04-28 12:00:00+00'), 1),
						(2, 2, ('2020-04-30 10:00:00+00'), 2),
						(3, 13, ('2020-05-06 23:00:00+00'), 3),
						(4, 14, ('2020-05-07 23:00:00+00'), NULL),
						(5, 2, ('2020-05-10 10:30:00+00'), 4),
						(6, 1, ('2020-05-10 12:30:00+00'), 5),
						(7, 6, ('2020-04-30 23:00:00+00'), 6),
						(8, 7, ('2020-05-03 23:00:00+00'), 7),
						(9, 8, ('2020-05-04 23:00:00+00'), 8),
						(10, 11, ('2020-05-06 15:00:00+00'), 9),
						(11, 4, ('2020-05-10 22:30:00+00'), 10);



INSERT INTO job VALUES (1, 11, 'cleaning the floor', ('2020-05-05 10:00:00+00'), ('2020-05-05 11:00:00+00')),
						(2, 11, 'sweeping the floor', ('2020-05-05 12:00:00+00'), ('2020-05-05 13:00:00+00')),
						(3, 11, 'making the beds', ('2020-05-05 15:00:00+00'), ('2020-05-05 17:00:00+00')),
						(4, 10, 'doing the dishes', ('2020-05-05 10:00:00+00'), ('2020-05-05 13:00:00+00')),
						(5, 10, 'cleaning the windows', ('2020-05-05 15:00:00+00'), ('2020-05-05 17:00:00+00')),
						(6, 10, 'painting the walls', ('2020-05-05 17:00:00+00'), ('2020-05-05 18:00:00+00')),
						(7, 12, 'gardening', ('2020-05-05 10:00:00+00'), ('2020-05-05 13:00:00+00')),
						(8, 12, 'cleaning the windows', ('2020-05-05 14:00:00+00'), ('2020-05-05 16:00:00+00')),
						(9, 15, 'cleaning the floor', ('2020-05-07 11:00:00+00'), ('2020-05-07 16:00:00+00')),
						(10, 15, 'cleaning the floor', ('2020-05-08 09:00:00+00'), ('2020-05-08 11:00:00+00'));						

INSERT INTO bribe VALUES (1, 1, 100),
						(2, 1, 200),
						(3, 1, 250),
						(4, 2, 300),
						(5, 2, 100),
						(6, 11, 100),
						(7, 7, 150),
						(8, 7, 200),
						(9, 4, 100),
						(10, 4, 100);


