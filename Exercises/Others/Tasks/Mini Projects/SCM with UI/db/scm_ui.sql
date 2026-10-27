show databases;

create database scm_ui;

use scm_ui;


create table users(
user_id int primary key auto_increment,
email varchar(100) not null unique,
password_hash varchar(255) not null,
role enum("admin","student") not null
);

INSERT INTO users (email, password_hash, role)
VALUES ('admin@gmail.com', 'admin123', 'admin');

create table students(
student_id int auto_increment primary key,
user_id int not null unique,
fname varchar(100) not null,
lname varchar(100) not null,
age int,
gender varchar(20),
email_id varchar(100) not null unique,

foreign key (user_id) references users(user_id)
);

create table courses (
course_id int primary key auto_increment,
course_name varchar(500) not null,
credits int not null,

check (credits between 1 and 6)
);


INSERT INTO courses (course_name, credits)
VALUES
('Python Programming', 4),
('Database Management', 4),
('Machine Learning', 4),
('Data Structures', 3),
('Web Development', 3);


create table enrollments(
enrollment_id int primary key auto_increment,
student_id int not null,
course_id int not null,
enrolled_on datetime default current_timestamp,

foreign key (student_id) references students(student_id),
foreign key (course_id) references courses(course_id),

unique(student_id, course_id)

);

select * from students;

