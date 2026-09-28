use practice;
show tables;
/*
CREATE TABLE students (
    id INT,
    name VARCHAR(50),
    age INT,
    city VARCHAR(50),
    email VARCHAR(100)
);

INSERT INTO students VALUES
(1, 'Alice', 22, 'Indore', 'alice@gmail.com'),
(2, 'Bob', 25, 'Bhopal', 'bob@yahoo.com'),
(3, 'Charlie', 19, 'Indore', 'charlie@gmail.com'),
(4, 'David', 30, 'Mumbai', 'david@outlook.com'),
(5, 'Daniel', 27, 'Delhi', 'daniel@gmail.com'),
(6, 'Ananya', 21, 'Indore', 'ananya@yahoo.com');

select * from students;

*/

select * from students where name like "d%";
select * from students where email like '%gmail%';
select * from students where name like '__n%';

select * from students;

select * from students where city in ('indore','bhopal');
select * from students where city not in ('indore','bhopal');

select * from students where age between 19 and 22;



