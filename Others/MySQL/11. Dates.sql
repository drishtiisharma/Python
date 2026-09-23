-- use school_db;
-- desc students;

-- alter table students modify column enrolled_on date;
/*
insert into students(first_name,last_name,email,enrolled_on) values
('sherlock','holmes','sherlock@gmail.com','2023-07-12'),
('shinnosuke','nohara','shin.chan@gmail.com','2020-08-01'),
('gintoki','sakata','g.sakata@gmail.com','2022-06-07');
*/
-- alter table students add column created_at timestamp default current_timestamp();
-- insert into students(first_name,last_name,email,enrolled_on) values ('mike','tyson','t.mike@gmail.com','2023-07-12');

-- alter table students add column updated_at datetime default current_timestamp() on update current_timestamp;

-- select id, first_name, last_name, created_at, updated_at from students where email = 't.mike@gmail.com'

-- select * from students;

-- update students set last_name='anderson' where email = 't.mike@gmail.com';

select id, first_name, last_name, created_at, updated_at from students where email = 't.mike@gmail.com'