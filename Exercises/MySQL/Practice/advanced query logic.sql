show databases;
use school_db;
show tables;

select * from students;
select * from enrollments;
select * from courses;

-- EXISTS --
select s.first_name, s.last_name
from students s
where exists (
select 1
from enrollments e
where e.student_id = s.id
);
-- ------ --


-- ANY --
use shop_db;
select * from products;

select name, category from products
where price > any(
select category
from products
where stock > 20
);
-- ----- --


show databases;
use practice;
show tables;


/* 
-- ALL --

create table prod(
pid int primary key auto_increment,
pname varchar(100),
price decimal(10,2)
);

insert into prod(pname, price) values
('chairs',180.00),
('tables',190.00),
('fan',918.00),
('cupboard',800.00);

create table ord_det(
oid int primary key auto_increment,
pid int,
quant int
);

insert into ord_det(pid, quant) values
(1,12),
(2,10),
(3,8),
(4,15);
select * from ord_det;
*/

select pid, pname 
from prod
where price > ALL(
select price
from prod
where pid < 2);
-- -- --


show tables;
select * from prod;



-- INSERT INTO --
create table prod_cop(
pid int primary key auto_increment,
pname varchar(100),
price decimal(10,2)
);

select * from prod;

insert into prod_cop
select pid,pname,price
from prod
where price>190;

select * from prod_cop;
-- ---------------- --




-- CASE --
use company_db;
show tables;
select * from employees;

select name, salary,
case
when salary >= 60000 then 'high'
when salary >= 40000 then 'medium'
else 'low'
end 
as salary_level
from employees;
-- ------------- --



-- IFNULL --
use shop_db;
show tables;
select * from products;

select name, ifnull(rating, "Not Available") as rating
from products;
-- this replaces null with something
-- -------- --



-- ISNULL --
select * from products;

select name, isnull(rating) as "rating missing" from products; 
-- 0: not null
-- 1: null
-- this only checks if null exists
-- -------- --


-- STORED PROCEDURES --
use company_db;
select * from employees;


select * from employees
where department_id = 4;

delimiter //
create procedure get_dept_4_emp()
begin
select * from employees
where department_id = 4;
end //

delimiter ;

delimiter @
create procedure get_dept_3_emp()
begin
select * from employees
where department_id = 3;
end @

delimiter ;

call get_dept_3_emp();

call get_dept_4_emp();
-- ----------------- --



/* multi line comment 
single line comments:
# 
--
*/


select name,
salary + 5000 as inc_salary,
salary - 5000 as dec_salary,
salary * 2 as double_salary,
salary / 2 as half_salary
from employees;

/*

-- REGULAR OPERATORS --
+    addition
-    subtraction
*    multiplication
/    division
%    remainder
-- ----------------- -- 


-- COMPARISON OPERATORS --
=
<>
!=
>
<
>=
<=
-- -------------------- -- 

-- LOGICAL OPERATORS --
AND
OR
NOT
-- -------------------- -- 


-- SPECIAL OPERATORS --
BETWEEN
IN
LIKE
-- ----------------- -- 


*/


/* 
-- DATA TYPES --

-- NUMERIC --
tinyint - 1 byte
smallint - 2 bytes
int - 4 bytes
bigint - 8 bytes
decimal(m,d) - variable
float - 4 bytes
double - 8 bytes
-- ------- -- 

-- STRING --
char(size) - upto 255
varchar(size) - upto 65,535
text - includes tinytext, text, mediumtext, longtext (no need to specify max length)
blobs - binary large objects; used to store binary files like images, audios or encrypted data
enum('v1','v2',...)
for example: 
	CREATE TABLE tasks (
		task_id INT PRIMARY KEY AUTO_INCREMENT,
		task_name VARCHAR(100) NOT NULL,
		-- The priority column will only accept 'Low', 'Medium', or 'High'
		priority ENUM('Low', 'Medium', 'High') DEFAULT 'Medium'
	);
-- ------- -- 

-- DATE AND TIME --
date - yyyy-mm-dd
time - hh:mm:ss
datetime - stores combined date and time string
timestamp - timezone aware
year - 4 digit format
-- ------- -- 

diff between datetime and timestamp

- DATETIME captures exactly what the clock says at that moment. If the photo says 12:00, it will always say 12:00, no matter who looks at it or what city they are standing in.

- TIMESTAMP If we schedule a meeting for 12:00 PM in New York, a coworker logging in from London doesn't see 12:00 PM on their calendar, they see 5:00 PM. 

*/ 






