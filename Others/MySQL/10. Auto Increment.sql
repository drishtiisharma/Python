-- use school_db;

-- desc students;
-- desc courses;

-- show create table students;
/* result
CREATE TABLE `students` (
   `id` int NOT NULL,
   `first_name` varchar(20) NOT NULL,
   `last_name` varchar(20) NOT NULL,
   `email` varchar(100) DEFAULT NULL,
   `enrolled_on` datetime DEFAULT NULL,
   PRIMARY KEY (`id`),
   UNIQUE KEY `email` (`email`),
   UNIQUE KEY `unique_email` (`email`),
   KEY `idx_last_name` (`last_name`)
 ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
*/
 
-- show create table courses;
/*
result:
CREATE TABLE `courses` (
   `id` varchar(10) NOT NULL,
   `title` varchar(100) DEFAULT NULL,
   `credits` int DEFAULT NULL,
   PRIMARY KEY (`id`),
   CONSTRAINT `chk_credits` CHECK ((`credits` between 1 and 6))
 ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
*/


/* 
dropping foreign keys
-- alter table enrollments drop foreign key enrollments_ibfk_1;
-- alter table enrollments drop foreign key enrollments_ibfk_2;
*/

-- alter table students modify column id int not null auto_increment;
-- alter table courses modify column id int not null auto_increment;


/* 
-- desc students; {shows auto_increment in extras}

insert into students(first_name,last_name,email) values
('emma','brown','bemma@gmail.com'),
('millie','grey','mgrey@gmail.com'),
('chris','presky','pre.chris@gmail.com');

-- delete from students where id = 107;

insert into students(first_name,last_name,email) values
('ninja','hattori','hattori.ninja@gmail.com');

-- select * from students; {doesnt continue from the deleted id}
*/

/*
-- desc courses; {shows auto_increment in extras}

insert into courses (title,credits) values
('java',3),
('dbms',5),
('os',5);

-- delete from courses where id = 116;

insert into courses (title,credits) values
('cn',3),
('dsa',5);

-- select * from courses; {doesnt continue from the deleted id}
*/


-- show table status like 'courses';
-- show table status like 'students';