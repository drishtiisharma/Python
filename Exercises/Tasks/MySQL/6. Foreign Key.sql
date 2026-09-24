-- use school_db;
-- desc students;
-- desc courses;
/*
create table enrollments(
id int primary key, 
student_id int, 
course_id varchar(10), 

foreign key (student_id) references students(id), 
foreign key (course_id) references courses(id)
);
*/
-- insert into courses values(101,'python',4);
-- insert into enrollments values(1,101,101)
-- insert into enrollments values(2,99,101)
/*
throws this error:

Error Code: 1452. Cannot add or update a child row: a foreign key constraint fails (`school_db`.`enrollments`, CONSTRAINT `enrollments_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `students` (`id`))	0.016 sec
*/

