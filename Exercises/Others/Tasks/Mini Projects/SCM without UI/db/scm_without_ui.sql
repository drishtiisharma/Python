show databases;
create database scm;

use scm;

create table students(
student_id int primary key auto_increment,
name varchar(100) not null,
email varchar(100) unique not null,
password_hash varchar(255) not null
);

create table courses(
course_id int primary key auto_increment,
course_name varchar(100) not null,
credits int check (credits between 1 and 6)
);

create table enrollments(
enrollment_id int primary key auto_increment,
student_id int not null,
course_id int not null,
enrolled_on datetime default current_timestamp,

foreign key(student_id) references students(student_id),
foreign key(course_id) references courses(course_id),
unique (student_id, course_id)
);

insert into courses (course_name, credits) values
("DBMS",6),
("OS",5),
("CN",4),
("ML",6);






