-- use school_db;

-- create index idx_last_name on students(last_name);

/*
insert into students values(102,'janice','bells','alice@gmail.com','2026-08-24 11:45:58');
insert into students values(103,'gwen','stacy','stacygwen@gmail.com','2026-08-24 14:55:58');
insert into students values(104,'mary','jane','jane10mary@gmail.com','2026-08-24 11:45:58');
insert into students values(105,'harry','channing','hchanning@gmail.com','2026-08-24 11:45:58');
insert into students values(106,'brad','smith','smith.brad@gmail.com','2026-08-24 11:45:58');
select * from students;
*/

-- explain select * from students where last_name = 'smith';

/*
shows: 
1	SIMPLE	students		ref	idx_last_name	idx_last_name	82	const	1	100.00	
*/


show index from students;

/*
list:

students	0	PRIMARY	1	id	A	1				BTREE
students	0	email	1	email	A	1			YES	BTREE
students	0	unique_email	1	email	A	1			YES	BTREE
students	1	idx_last_name	1	last_name	A	0				BTREE

*/









