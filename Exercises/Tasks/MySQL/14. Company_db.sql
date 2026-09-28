create database company_db;
use company_db;

create table departments(
id int primary key,
name varchar(20)
);

create table employees(
id int primary key,
name varchar(20),
department_id int,
manager_id int,
salary decimal(10,2),
foreign key (department_id) references departments(id),
foreign key (manager_id) references employees(id)
);

create table projects(
id int primary key,
title varchar(100),
department_id int
);


insert into departments (id, name) values
(1, 'Engineering'),
(2, 'HR'),
(3, 'Finance'),
(4, 'Marketing'),
(5, 'Sales'),
(6, 'Legal');

insert into employees (id, name, department_id, manager_id, salary) values
(1, 'Rahul', 1, NULL, 90000),
(2, 'Aman', 1, 1, 70000),
(3, 'Priya', 1, 1, 75000),
(4, 'Neha', 1, 2, 65000),

(5, 'Rohan', 3, NULL, 85000),
(6, 'Simran', 3, 5, 65000),
(7, 'Karan', 3, 5, 68000),

(8, 'Anjali', 4, NULL, 80000),
(9, 'Vikas', 4, 8, 60000),
(10, 'Pooja', 4, 8, 62000),

(11, 'Arjun', 5, NULL, 82000),
(12, 'Meera', 5, 11, 58000),
(13, 'Nikhil', 5, 11, 61000),

(14, 'Isha', NULL, NULL, 50000),
(15, 'Dev', NULL, 1, 55000),

(16, 'Kavya', 1, 2, 66000),
(17, 'Aditya', 3, 5, 64000),
(18, 'Sneha', 4, 8, 59000),
(19, 'Varun', 5, 11, 57000),
(20, 'Tanya', 1, 3, 70000),
(21, 'Mohit', NULL, 5, 52000);

select * from employees;


insert into projects (id, title, department_id) values
(1, 'Website Redesign', 1),
(2, 'Mobile App', 1),
(3, 'Cloud Migration', 1),

(4, 'Recruitment Drive', 2),

(5, 'Financial Audit', 3),
(6, 'Budget Planning', 3),

(7, 'Ad Campaign', 4),
(8, 'Social Media Strategy', 4),

(9, 'Sales Expansion', 5),
(10, 'CRM Upgrade', 5),

(11, 'Market Research', 5),

(12, 'Unknown Project', 99);

select * from projects;


-- TASK 1 --
select e.id, e.name, d.name
from employees e
inner join departments d
on e.department_id = d.id;

-- TASK 2 --
select count(*) from employees; -- 21

select count(*) as emp_with_null_dept from employees where department_id is null; -- 3

select count(*) as emp_after_join
from employees e
inner join departments d
on e.department_id = d.id; -- 18 (verified)


-- TASK 3 --
select e.name, d.name, p.title
from employees e
inner join departments d
on e.department_id = d.id
inner join projects p 
on d.id = p.department_id;

-- TASK 4 --
select e.name, d.name
from employees e
left join departments d
on e.department_id = d.id;

-- TASK 5 --
select d.name , e.name
from departments d
left join employees e
on d.id = e.department_id;

-- TASK 6 --
select d.name, p.title
from departments d
left join projects p
on d.id = p.department_id;

-- TASK 7 --
-- returns entire left table with matched rows from right table
select d.name , e.name
from departments d
left join employees e
on d.id = e.department_id;
-- left table : departments
-- right table : employees

-- returns entire right table with matched rows from left table
select e.name , d.name
from employees e
right join departments d
on e.department_id = d.id;
-- right table : departments
-- left table : employees

-- hence both had identical results


-- TASK 8 --
select d.id as department_id, d.name as department_name, e.name as employee_name
from employees e
right join departments d
on e.department_id = d.id;

-- TASK 9 --
select e.name as employee_name, m.name as manager_name
from employees e
join employees m
on e.manager_id = m.id;

-- TASK 10 --
select e.name as employee_name, m.name as manager_name
from employees e
left join employees m
on e.manager_id = m.id;

-- TASK 11 --
select e1.name as employee1, e2.name as employee2, e1.department_id, e1.salary as salary1, e2.salary as salary2
from employees e1
join employees e2
on e1.department_id = e2.department_id
and e1.id < e2.id
and e1.salary <> e2.salary;

-- TASK 12 --
select e.name as employee_name, m.name as manager_name, d.name as department_name
from employees e
left join employees m
on e.manager_id = m.id
left join departments d
on e.department_id = d.id;

-- TASK 13 --
select d.name as department_name, count(e.id) as emp_count, count(p.id) as project_count
from departments d
left join employees e
on d.id = e.department_id
left join projects p
on d.id = p.department_id
where e.id is null and p.id is null
group by d.name;


-- TASK 14 --
-- inner join across all 3 tables
select e.name as emp_name, d.name as dept_name, p.title as project_name
from employees e
inner join departments d
on e.department_id = d.id
inner join projects p
on d.id = p.department_id;

-- left join across all 3 tables
select e.name as emp_name, d.name as dept_name, p.title as project_name
from employees e
left join departments d
on e.department_id = d.id
left join projects p
on d.id = p.department_id;

-- comparison
select
(
select count(*) as inner_join_count
from employees e
inner join departments d
on e.department_id = d.id
inner join projects p
on d.id = p.department_id
) as inner_join_row_count, -- 46

(select count(*) as inner_join_count
from employees e
left join departments d
on e.department_id = d.id
left join projects p
on d.id = p.department_id) as left_join_row_count; -- 49