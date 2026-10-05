show databases;

create database online_exam;

use online_exam;

-- for users (student+admin)

create table users(
user_id int auto_increment primary key,
fname varchar(100) not null,
lname varchar(100) not null,
email varchar(255) not null unique,
password_hash varchar(255) not null,
role enum('student','admin') default 'student',
created_at datetime default current_timestamp
);


-- for subjects

create table subjects(
subject_id int auto_increment primary key,
subject_name varchar(200) not null unique,
description text
);


-- for exams

create table exams(
exam_id int auto_increment primary key,
subject_id int not null,
exam_name varchar(255) not null,
description text,
duration_minutes int not null,
total_marks int not null,
passing_marks int not null,
start_time datetime,
end_time datetime,
created_by int not null,

foreign key (subject_id) references subjects(subject_id),
foreign key (created_by) references users(user_id)
);

-- for questions

create table questions(
question_id int auto_increment primary key,
exam_id int not null,
question_text text not null,
marks int not null default 1,

foreign key (exam_id) references exams(exam_id) on delete cascade
);

# on delete cascade means : if a parent row is deleted, delete all related child rows too

-- options

create table options(
option_id int auto_increment primary key,
question_id int not null,
option_text text not null,
is_correct boolean default false,

foreign key(question_id) references questions(question_id) on delete cascade
);

-- exam attempts
create table exam_attempts(
attempt_id int auto_increment primary key,
user_id int not null,
exam_id int not null,
started_at datetime default current_timestamp,
submitted_at datetime,
status enum("in_progress","submitted") default "in_progress",

foreign key (user_id) references users(user_id),

foreign key (user_id) references exams(exam_id),

unique(user_id, exam_id)
);


-- answers

create table student_answers(
answer_id int auto_increment primary key,
attempt_id int not null,
question_id int not null,
selected_option_id int,
answered_at datetime default current_timestamp,

foreign key (attempt_id) references exam_attempts(attempt_id) on delete cascade,

foreign key (question_id) references questions(question_id),
foreign key (selected_option_id) references options(option_id),


unique (attempt_id,question_id)
);


-- results

create table results(
result_id int auto_increment primary key,
attempt_id int not null unique,
total_questions int not null,
correct_answers int not null default 0,
wrong_answers int not null default 0,
unanswered int not null default 0,
marks_obtained decimal(10,2) not null default 0,
percentage decimal(5,2) not null default 0,
results_status enum('pass','fail') not null,
generated_at datetime default current_timestamp,

foreign key (attempt_id) references exam_attempts(attempt_id) on delete cascade);



