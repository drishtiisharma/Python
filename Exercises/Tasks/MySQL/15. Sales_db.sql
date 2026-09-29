create database sales_db;
use sales_db;

create table online_orders(
id int primary key,
customer_name varchar(100),
amount decimal(10,2),
order_date date,
region varchar(100)
);


create table store_orders(
id int primary key,
customer_name varchar(100),
amount decimal(10,2),
order_date date,
region varchar(100)
);


create table customers(
id int primary key,
name varchar(100),
loyalty_tier varchar(50),
signup_date date
);

INSERT INTO customers
VALUES
(1, 'Rahul', 'Gold', '2023-02-10'),
(2, 'Aman', 'Silver', '2023-04-15'),
(3, 'Priya', 'Platinum', '2023-05-20'),
(4, 'Neha', 'Gold', '2023-07-12'),
(5, 'Rohit', 'Silver', '2023-08-25'),
(6, 'Ananya', 'Platinum', '2023-09-10'),
(7, 'Vikas', 'Silver', '2023-10-18'),
(8, 'Sneha', 'Gold', '2023-11-05'),
(9, 'Karan', 'Silver', '2024-01-14'),
(10, 'Pooja', 'Platinum', '2024-02-20'),
(11, 'Meera', 'Gold', '2024-03-11'),
(12, 'Arjun', 'Silver', '2024-04-16'),
(13, 'Riya', 'Gold', '2024-05-22'),
(14, 'Sahil', 'Silver', '2024-06-30'),
(15, 'Dev', 'Gold', '2024-07-15'),
(16, 'Nikhil', 'Silver', '2024-08-20'),
(17, 'Simran', 'Gold', '2024-09-12');


select * from customers;


INSERT INTO store_orders
VALUES
(1, 'Rahul', 1200.00, '2024-01-15', 'North'),
(2, 'Aman', 900.00, '2024-04-05', 'West'),
(3, 'Priya', 1800.00, '2024-06-12', 'South'),
(4, 'Neha', 1600.00, '2024-08-20', 'East'),
(5, 'Rohit', 750.00, '2024-10-10', 'North'),
(6, 'Vikas', 1100.00, '2024-12-15', 'South'),
(7, 'Sneha', 2000.00, '2025-01-30', 'East'),
(8, 'Karan', 950.00, '2025-03-11', 'North'),
(9, 'Pooja', 2400.00, '2025-05-22', 'West'),
(10, 'Meera', 1700.00, '2025-07-18', 'South'),
(11, 'Arjun', 1250.00, '2025-09-09', 'East'),
(12, 'Sahil', 800.00, '2025-11-21', 'West'),
(13, 'Rahul', 1000.00, '2026-01-05', 'North'),
(14, 'Neha', 1450.00, '2026-02-14', 'East'),
(15, 'Dev', 1300.00, '2026-03-25', 'North'),
(16, 'Tanya', 2100.00, '2026-04-17', 'East'),
(17, 'Aman', 850.00, '2026-05-01', 'West'),
(18, 'Priya', 1900.00, '2026-06-10', 'South'),
(19, 'Kabir', 1150.00, '2026-07-05', 'North'),
(20, 'Ishita', 2700.00, '2026-08-12', 'South'),
(21, 'Kabir', 1150.00, '2026-07-05', 'North');

select * from store_orders;

INSERT INTO online_orders
VALUES
(1, 'Rahul', 1200.00, '2024-01-15', 'North'),
(2, 'Aman', 850.00, '2024-03-20', 'West'),
(3, 'Priya', 2300.00, '2024-05-10', 'South'),
(4, 'Neha', 1500.00, '2024-07-12', 'East'),
(5, 'Rohit', 950.00, '2024-09-18', 'North'),
(6, 'Ananya', 3200.00, '2024-11-05', 'West'),
(7, 'Vikas', 700.00, '2025-01-22', 'South'),
(8, 'Sneha', 1800.00, '2025-02-14', 'East'),
(9, 'Karan', 1100.00, '2025-04-08', 'North'),
(10, 'Pooja', 2600.00, '2025-06-19', 'West'),
(11, 'Rahul', 900.00, '2025-08-25', 'North'),
(12, 'Aman', 1400.00, '2025-10-11', 'West'),
(13, 'Meera', 2100.00, '2025-12-03', 'South'),
(14, 'Arjun', 1750.00, '2026-01-17', 'East'),
(15, 'Neha', 1300.00, '2026-02-21', 'East'),
(16, 'Riya', 2800.00, '2026-03-15', 'North'),
(17, 'Sahil', 600.00, '2026-04-10', 'West'),
(18, 'Priya', 1900.00, '2026-05-05', 'South'),
(19, 'Dev', 1250.00, '2026-06-20', 'North'),
(20, 'Tanya', 2200.00, '2026-07-14', 'East'),
(21, 'Aman', 850.00, '2026-08-01', 'West');

select * from online_orders;

-- TASK 1 --
select amount, order_date from online_orders
union
select amount, order_date from store_orders;
-- TASK 1 --


-- TASK 2 --
select amount, order_date from online_orders
union all
select amount, order_date from store_orders;

-- comparison
select count(*) as union_count from
(
select amount, order_date from online_orders
union
select amount, order_date from store_orders
) as combined_union; -- returns 40

select count(*) as union_all_count from
(
select amount, order_date from online_orders
union all
select amount, order_date from store_orders
) as combined_union_all; -- returns 42
-- TASK 2 --

select * from online_orders;
select * from store_orders;

-- TASK 3 --
select region, count(*) as total_orders, sum(amount) as total_amount
from  (
select customer_name, amount, order_date, region
from online_orders
union
select customer_name, amount, order_date, region
from store_orders
) as all_orders 
group by region;
-- TASK 3 --





-- TASK 4 --
select customer_name,sum(amount) as total_spend
from(
select * from online_orders
union all
select * from store_orders
) as all_orders
group by customer_name
order by total_spend desc;
-- TASK 4 --


-- TASK 5 --
select region, year(order_date) as order_year, count(*) as total_orders, sum(amount) as total_amount
from(
select region, amount, order_date from online_orders
union all
select region, amount, order_date from store_orders
) as all_orders
group by region, year(order_date)
order by region, order_year;
-- TASK 5 --

-- TASK 6 --
select customer_name, count(*) as order_count from(
select customer_name from online_orders
union all
select customer_name from store_orders
) as all_orders
group by customer_name
having count(*)<3;
-- TASK 6 --


-- TASK 7 --
/*

where - filters individual rows before grouping
having - filters individual rows after grouping

where cannot directly use the aggregate functions like sum(), avg(), etc as these functions operate on multiple/group of rows while where needs a condition that can be evaluated for each row directly.
hence, aggregate values are calculated only after grouping required rows so sql uses having to apply conditions on those aggregated results.

*/
select customer_name, sum(amount) as total_spend, count(*) as order_count
from (
select customer_name, amount, order_date
from online_orders
union all
select customer_name, amount, order_date
from store_orders
) as all_orders
where order_date >= '2025-01-01'
group by customer_name
having sum(amount) > 3000;
-- TASK 7 --


-- TASK 8 --
select c.id,c.name, c.loyalty_tier, c.signup_date 
from customers c 
where exists(
select 1
from online_orders o 
where o.customer_name = c.name
) or exists(
select 1
from online_orders o 
where o.customer_name = c.name
);
-- TASK 8 --




-- TASK 9 --
select c.id, c.name, c.loyalty_tier, c.signup_date 
from customers c 
where not exists(
select 1
from online_orders o 
where o.customer_name = c.name
) and not exists(
select 1
from online_orders o 
where o.customer_name = c.name
);
-- TASK 9 --







