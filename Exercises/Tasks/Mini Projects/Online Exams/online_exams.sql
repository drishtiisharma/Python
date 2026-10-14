-- =====================================================
-- ONLINE EXAMINATION SYSTEM
-- Complete Database Schema
-- =====================================================

SHOW DATABASES;

CREATE DATABASE online_exam;

USE online_exam;


-- =====================================================
-- 1. USERS (STUDENTS AND ADMINS)
-- =====================================================

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    fname VARCHAR(100) NOT NULL,
    lname VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    role ENUM('student', 'admin') NOT NULL DEFAULT 'student',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);


-- =====================================================
-- 2. SUBJECTS
-- =====================================================

CREATE TABLE subjects (
    subject_id INT AUTO_INCREMENT PRIMARY KEY,
    subject_name VARCHAR(200) NOT NULL UNIQUE,
    description TEXT
);


-- =====================================================
-- 3. EXAMS
-- =====================================================

CREATE TABLE exams (
    exam_id INT AUTO_INCREMENT PRIMARY KEY,
    subject_id INT NOT NULL,
    exam_name VARCHAR(255) NOT NULL,
    description TEXT,
    duration_minutes INT NOT NULL,
    total_marks INT NOT NULL,
    passing_marks INT NOT NULL,
    start_time DATETIME,
    end_time DATETIME,
    status ENUM('draft', 'published') NOT NULL DEFAULT 'draft',
    created_by INT NOT NULL,

    CONSTRAINT chk_exam_duration
        CHECK (duration_minutes > 0),

    CONSTRAINT chk_exam_total_marks
        CHECK (total_marks > 0),

    CONSTRAINT chk_exam_passing_marks
        CHECK (
            passing_marks >= 0
            AND passing_marks <= total_marks
        ),

    CONSTRAINT fk_exams_subject
        FOREIGN KEY (subject_id)
        REFERENCES subjects(subject_id),

    CONSTRAINT fk_exams_creator
        FOREIGN KEY (created_by)
        REFERENCES users(user_id)
);


-- =====================================================
-- 4. QUESTIONS
-- Deleting an exam deletes its questions.
-- =====================================================

CREATE TABLE questions (
    question_id INT AUTO_INCREMENT PRIMARY KEY,
    exam_id INT NOT NULL,
    question_text TEXT NOT NULL,
    marks INT NOT NULL DEFAULT 1,

    CONSTRAINT chk_question_marks
        CHECK (marks > 0),

    CONSTRAINT fk_questions_exam
        FOREIGN KEY (exam_id)
        REFERENCES exams(exam_id)
        ON DELETE CASCADE
);


-- =====================================================
-- 5. OPTIONS
-- Deleting a question deletes its options.
-- =====================================================

CREATE TABLE options (
    option_id INT AUTO_INCREMENT PRIMARY KEY,
    question_id INT NOT NULL,
    option_text TEXT NOT NULL,
    is_correct BOOLEAN NOT NULL DEFAULT FALSE,

    CONSTRAINT fk_options_question
        FOREIGN KEY (question_id)
        REFERENCES questions(question_id)
        ON DELETE CASCADE
);


-- =====================================================
-- 6. EXAM ATTEMPTS
-- An exam cannot be deleted while attempts reference it.
-- One attempt per student per exam.
-- =====================================================

CREATE TABLE exam_attempts (
    attempt_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    exam_id INT NOT NULL,
    started_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    submitted_at DATETIME,
    status ENUM('in_progress', 'submitted')
        NOT NULL DEFAULT 'in_progress',

    CONSTRAINT fk_attempts_user
        FOREIGN KEY (user_id)
        REFERENCES users(user_id),

    CONSTRAINT fk_attempts_exam
        FOREIGN KEY (exam_id)
        REFERENCES exams(exam_id),

    CONSTRAINT uq_student_exam
        UNIQUE (user_id, exam_id)
);


-- =====================================================
-- 7. STUDENT ANSWERS
-- Keep historical answers when managing questions.
-- =====================================================

CREATE TABLE student_answers (
    answer_id INT AUTO_INCREMENT PRIMARY KEY,
    attempt_id INT NOT NULL,
    question_id INT NOT NULL,
    selected_option_id INT,
    answered_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_answers_attempt
        FOREIGN KEY (attempt_id)
        REFERENCES exam_attempts(attempt_id)
        ON DELETE CASCADE,

    CONSTRAINT fk_answers_question
        FOREIGN KEY (question_id)
        REFERENCES questions(question_id),

    CONSTRAINT fk_answers_option
        FOREIGN KEY (selected_option_id)
        REFERENCES options(option_id),

    CONSTRAINT uq_attempt_question
        UNIQUE (attempt_id, question_id)
);


-- =====================================================
-- 8. RESULTS
-- Deleting an attempt deletes its result.
-- =====================================================

CREATE TABLE results (
    result_id INT AUTO_INCREMENT PRIMARY KEY,
    attempt_id INT NOT NULL UNIQUE,
    total_questions INT NOT NULL,
    correct_answers INT NOT NULL DEFAULT 0,
    wrong_answers INT NOT NULL DEFAULT 0,
    unanswered INT NOT NULL DEFAULT 0,
    marks_obtained DECIMAL(10,2) NOT NULL DEFAULT 0,
    percentage DECIMAL(5,2) NOT NULL DEFAULT 0,
    results_status ENUM('pass', 'fail') NOT NULL,
    is_published BOOLEAN NOT NULL DEFAULT FALSE,
    generated_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT chk_result_counts
        CHECK (
            total_questions >= 0
            AND correct_answers >= 0
            AND wrong_answers >= 0
            AND unanswered >= 0
        ),

    CONSTRAINT chk_result_percentage
        CHECK (percentage >= 0 AND percentage <= 100),

    CONSTRAINT fk_results_attempt
        FOREIGN KEY (attempt_id)
        REFERENCES exam_attempts(attempt_id)
        ON DELETE CASCADE
);


-- =====================================================
-- 9. VERIFY TABLES
-- =====================================================

SHOW TABLES;

DESCRIBE users;
DESCRIBE subjects;
DESCRIBE exams;
DESCRIBE questions;
DESCRIBE options;
DESCRIBE exam_attempts;
DESCRIBE student_answers;
DESCRIBE results;


-- =====================================================
-- 10. VIEW DATA
-- =====================================================

SELECT * FROM users;
SELECT * FROM subjects;
SELECT * FROM exams;
SELECT * FROM questions;
SELECT * FROM options;
SELECT * FROM exam_attempts;
SELECT * FROM student_answers;
SELECT * FROM results;

COMMIT;


insert into users (fname,lname,email,password_hash,role) 
values
('Issac', 'Newton', 'issac@gmail.com','inewton','admin');