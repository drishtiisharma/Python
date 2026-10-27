use practice;
show databases;
show tables;
/*
create table emp1(
id int primary key auto_increment,
name varchar(10)
);

insert into emp1(name) values
('rahul'),
('aman'),
('geeta');

select * from emp1;


create table mang1(
id int primary key auto_increment,
name varchar(10)
);

insert into mang1(name) values
('khushi'),
('neha'),
('raj');

select * from mang1;
*/

update emp1 set id = 4 where name ='aman';

-- union: combines + removes duplicates
select * from emp1 
union
select * from mang1;

-- union all: combines + keeps duplicates
select * from emp1 
union all
select * from mang1;

-- group by
use company_db;
show tables;
select * from employees;
select * from departments;

select e.department_id,d.name, count(*) as emp_count
from employees e
left join departments d
on e.department_id = d.id
group by department_id;

select e.department_id,d.name, count(*) as emp_count
from employees e
left join departments d
on e.department_id = d.id
group by department_id
having count(*)>4;


select d.name, round(avg(salary),2) as avg_salary
from employees e
left join departments d
on e.department_id = d.id
where e.salary > 75000
group by e.department_id
having avg(e.salary) > 50000;



