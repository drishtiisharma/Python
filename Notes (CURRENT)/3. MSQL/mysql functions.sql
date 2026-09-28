show databases;
create database practice;
use practice;

/*
create table users(
id int,
name varchar(20),
email varchar(100)
);
alter table users modify id int primary key auto_increment, auto_increment = 100;

insert into users(name, email) values
('alice', 'alice12@gmail.com'),
('janice', 'janice.alb@gmail.com'),
('charlie', 'charlie24@gmail.com');

alter table users add column age int;
update users set age = 20 where name like 'A%';
update users set age = 19 where name like 'J%';
update users set age = 21 where name like 'C%';

*/

select upper(name) from users;
-- similarly lower()

-- length & char_length

-- same for both
select 'hello' as text, length('hello') as bytes, char_length('hello') as characters;

-- different for both
select '💀' as text, length('💀') as bytes, char_length('💀') as characters;

-- concat
select concat('hello','','world');
select concat(name,' - ', email) as "name-email" from users;
select concat_ws('-',2026,'09','26') as date;

-- substring: substring(string,start,length)
select substring('helloworld',1,6) as substring;
select substring(name,1,3) as subname from users;

-- left and right
select left(email,5) from users;
select right(email,5) from users;

-- trim()
SELECT 
    '    hello   ' AS original_text, 
    LENGTH('    hello   ') AS original_length,
    TRIM('  hello   ') AS trimmed_text, 
    LENGTH(TRIM('  hello   ')) AS trimmed_length;
    
    
-- replace()
select replace(name,'charlie','zuri') from users;
select * from users; -- will display the original, not the replaced


-- instr()
select email,instr(email,'@') as 'position_of_@' from users;

-- reverse()
select name as 'original_name',reverse(name) as 'reversed_name' from users;





