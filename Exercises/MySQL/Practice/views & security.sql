# Views

/*
------------ VIEWS ------------
view: is a saved select query, when we create a view, mysql saves that query. the view can then be used with select like a normal query

for example:
	create view student_details as 
	select s.id, first_name, e.no from students;

now a view with only these columns will exist like a table

so whenever we need this table(view), we can use it as:

	select * from student_details // where student_details is a view


IMP:
* VIEW != another copy of table's data
* if data in ORIGINAL table changes, VIEW also changes
* if data in VIEW changes, ORIGINAL data also changes


WHY USE IT?
* to save a frequently used query
* to simplify complex queries
* to hide underlying table structure

------------ VIEWS ------------
*/

show databases;
use school_db;
show tables;

select * from students;



-- creating a view: fetching data--
create view fetch_students as 
select first_name, last_name, email from students;

select * from fetch_students;
-- creating a view: fetching data--




-- updating a view --
update fetch_students
set last_name = 'pitt'
where first_name = 'brad';

select * from fetch_students;

select * from students;
-- updating a view --






-- showing existing views --
show full tables;
show create view fetch_students;
/*
returns this:

'CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `fetch_students` AS select `students`.`first_name` AS `first_name`,`students`.`last_name` AS `last_name`,`students`.`email` AS `email` from `students`'
*/
-- showing existing views --






-- modifying views --

/* existing view:
create view fetch_students as 
select first_name, last_name, email from students;
*/

create or replace view fetch_students as 
select id, email from students;


select * from fetch_students;
-- modifying views --











-- deleting a view --
drop view fetch_students;
show full tables;
-- deleting a view --




-- copying a view --
create view fetch_copy as
select * from fetch_students;

select * from fetch_copy;
-- copying a view --




# mysql injection
/*

WHAT IT IS?

mysql injection is a security vulnerability where the attackers insert malicious code into input fields to manipulate backend database queries



for example:


	txtUserId = getRequestString("UserId");
	txtSQL = "select * from users where UserId =" + txtUserId;

now, there's nothing to prevent a user from entering smart input like:
UserId : 105 or 1=1, the query will now become

	select * from users where UserId = 105 or 1=1;
    
where OR 1=1 will ALWAYS be true

the table might contain sensitive data like passwords, addresses etc.



HOW TO PREVENT IT?

sql parameters can be used to prvent this. 
parameterized query is a sql statement that uses placeholders instead of directly adding the input values into the query text.
placeholders get replaced with actual valuess when query executes

most databases support such queries but syntax varies:
- mysql uses ?
- sql server uses @ 
- postgresql usess $

for example

instead of this:
	txtUserId = getRequestString("UserId");
	txtSQL = "select * from users where UserId =" + txtUserId;
    
do this:
	txtUserId = getRequestString("UserId");
	txtSQL = "select * from users where UserId = ?";
    cursor.execute(txtSQL, (txtUserId,))
    
so the query becomes:
	select * from users where UserId = '105 or 1 = 1';
not
	select * from users where UserId = 105 or 1 = 1;
*/