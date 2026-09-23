-- use school_db;

-- desc students;

-- alter table students add constraint unique_email unique (email); {already added while creating table}

-- insert into students values(101,'alex','graham','alex123@gmail.com', '2026-09-23 12:00:10');

 -- select * from students;

-- insert into students values(102,'alex','johnson','alex123@gmail.com', '2026-09-24 13:30:12');

 -- Throws Error Code: 1062. Duplicate entry 'alex123@gmail.com' for key 'students.email'	0.016 sec
 
select * from students; -- displays only 1st record


