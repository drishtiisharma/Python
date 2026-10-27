-- use school_db;

-- desc enrollments;
-- alter table enrollments add column status varchar(20) default 'active';

insert into enrollments (id, student_id, course_id) values (2, 101, 101);
select * from enrollments;
-- shows active as default