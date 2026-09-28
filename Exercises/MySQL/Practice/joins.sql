/*
join clause is used to combine rows from two or more tables, based on a related column between them

types of joins:
inner: returns only rows that have matching values in BOTH tables
left : returns all rows from left, and matched rows from right table
right: returns all rows from right, and matched rows from left table
cross: returns cartesian product of two or more tables i.e every possible combination
*/

use practice;
show tables;

create table emp(
emp_id int primary key auto_increment,
ename varchar(50),
dept_id int);

insert into emp(ename,dept_id) values
('rahul', 10),
('rita', 20),
('aman', 10),
('neha', 30);

select * from emp;

create table dept(
dept_id int primary key,
dname varchar(20)
);

insert into dept values
(10, 'IT'),
(20, 'HR'),
(30, 'Finance'),
(40, 'Marketing');

select * from dept;

-- inner join (emp and their respective department ONLY matched in BOTH)
select emp.ename, dept.dname 
from emp
inner join dept
on emp.dept_id = dept.dept_id;

insert into emp(ename,dept_id) values('Alex',null);

-- left join (all emps and their dep; even if their dept doesnt exist)
select emp.ename, dept.dname 
from emp
left join dept
on emp.dept_id = dept.dept_id;

-- right join (all depts and their emps; even if their emp doesnt exist)
select emp.ename, dept.dname 
from emp
right join dept
on emp.dept_id = dept.dept_id;

-- cross join (pair every emp with every dept)
select emp.ename, dept.dname 
from emp
cross join dept
where ename = 'Alex';




