use practice;
show tables;

CREATE TABLE orders (
    id INT,
    customer VARCHAR(50),
    order_date DATE,
    order_time DATETIME
);

INSERT INTO orders VALUES
(1, 'Alice', '2026-09-20', '2026-09-20 10:30:00'),
(2, 'Bob', '2026-09-22', '2026-09-22 14:45:00'),
(3, 'Charlie', '2026-09-25', '2026-09-25 18:20:00');

select * from orders;


select curdate(); -- current date
select curtime(); -- current time
select now(); -- current date + time

select year('2026-03-24') as 'year', month('2026-03-24') as 'month', day('2026-03-24') as 'date';

select monthname('2026-03-24') as 'month_name', dayname('2026-03-24') as 'day_name';

select date(order_time) from orders;
select time(order_time) from orders;

select '2004-06-11' as bday1,
dayname('2004-06-11') as day,
date_add('2004-06-11', interval 286 day) as bday2,dayname('2005-03-24') as day;

select '2005-03-24' as bday1,
dayname('2005-03-24') as day,
date_sub('2005-03-24', interval 286 day) as bday2,dayname('2004-06-11') as day;

select datediff('2004-06-11','2005,03-24') as date_diff;

select date_format('2026-09-20',
'%d-%m-%Y') as 'mm-dd-yyyy';

/*
%Y	4-digit year
%y	2-digit year

%m	Month number
%M	Month name

%d	Day
%H	Hour
%i	Minutes
%s	Seconds
*/


