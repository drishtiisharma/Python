use practice;
-- show tables;

/*
select * from students;
select * from subs;
select * from users;

select distinct age from students;
select name from users;
select count(distinct age) from users;

select * from users where name = 'USER';
select * from users where age>19 and age<24;
select * from users where name = 'USER' or age = 20;
select * from users where not name = 'USER';
select * from users order by age;
select * from users order by uid desc;
select * from users order by name desc, age;

show keys from users where key_name = 'PRIMARY';
insert into users(age,name) values(Null,'bernard')

select name from users where age is null;
select distinct age from users where age is not null;

update users set name = 'unidentified' where age is null;

delete from users where name = 'john';

delete from users; - > this will delete all records(sequentially, can also use a where clause) but not the table structure
truncate table users; -> this  will delete all records(all at once, cannot use a truncate clause) but not the table structure

select count(*) from users; - returns total no of rows
select * from users; - returns whole table(all records)
select * from users limit 3;  return 1st 3 records
select * from users limit 4 offset 3; skip 1st 3 records(offset) and return 4 records from the very next(limit)
*/
