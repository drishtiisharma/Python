-- use school_db;
-- alter table courses modify column credits int;
-- alter table courses add constraint chk_credits check (credits between 1 and 6);

-- select * from courses;
insert into courses values (102,'java',10);

/*
throws error:

Error Code: 3819. Check constraint 'chk_credits' is violated.	0.000 sec
*/