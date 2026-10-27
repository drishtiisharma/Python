CREATE DATABASE online_orders;
USE online_orders;


CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(20) NOT NULL DEFAULT 'user',
    salary DECIMAL(10,2),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE orders (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    product VARCHAR(100) NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    status VARCHAR(20) NOT NULL,
    order_date DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES users(id)
);

INSERT INTO users
(username, email, password_hash, role, salary)
VALUES
('alice', 'alice@example.com', 'fake_hash_001', 'user', 45000),
('bob', 'bob@example.com', 'fake_hash_002', 'user', 52000),
('charlie', 'charlie@example.com', 'fake_hash_003', 'admin', 85000),
('david', 'david@example.com', 'fake_hash_004', 'user', 48000),
('emma', 'emma@example.com', 'fake_hash_005', 'user', 55000),
('frank', 'frank@example.com', 'fake_hash_006', 'admin', 90000),
('grace', 'grace@example.com', 'fake_hash_007', 'user', 47000),
('henry', 'henry@example.com', 'fake_hash_008', 'user', 51000),
('isla', 'isla@example.com', 'fake_hash_009', 'user', 60000),
('jack', 'jack@example.com', 'fake_hash_010', 'admin', 95000),
('kate', 'kate@example.com', 'fake_hash_011', 'user', 53000),
('leo', 'leo@example.com', 'fake_hash_012', 'user', 49000);

INSERT INTO orders
(user_id, product, amount, status, order_date)
VALUES
(1, 'Laptop', 65000, 'delivered', '2026-01-10'),
(1, 'Mouse', 1200, 'delivered', '2026-02-05'),
(1, 'Keyboard', 2500, 'cancelled', '2026-03-12'),

(2, 'Monitor', 18000, 'delivered', '2026-01-15'),
(2, 'Headphones', 3500, 'pending', '2026-02-20'),
(2, 'Webcam', 4200, 'cancelled', '2026-03-18'),

(3, 'Laptop', 72000, 'delivered', '2026-01-22'),
(3, 'SSD', 6500, 'delivered', '2026-02-11'),
(3, 'Keyboard', 3000, 'cancelled', '2026-03-05'),

(4, 'Mouse', 1500, 'delivered', '2026-01-30'),
(4, 'Monitor', 21000, 'pending', '2026-02-15'),
(4, 'USB Hub', 1800, 'cancelled', '2026-03-22'),

(5, 'Laptop', 68000, 'delivered', '2026-01-12'),
(5, 'Mouse', 1300, 'delivered', '2026-02-17'),
(5, 'Headphones', 4000, 'cancelled', '2026-03-25'),

(6, 'Monitor', 25000, 'delivered', '2026-01-18'),
(6, 'SSD', 7000, 'delivered', '2026-02-28'),
(6, 'Keyboard', 2800, 'pending', '2026-03-10'),

(7, 'Webcam', 4500, 'delivered', '2026-01-25'),
(7, 'Mouse', 1100, 'cancelled', '2026-02-12'),
(7, 'USB Hub', 1600, 'delivered', '2026-03-20'),

(8, 'Laptop', 75000, 'delivered', '2026-01-08'),
(8, 'Keyboard', 2700, 'pending', '2026-02-14'),
(8, 'Headphones', 3800, 'cancelled', '2026-03-16'),

(9, 'Monitor', 22000, 'delivered', '2026-01-19'),
(9, 'Mouse', 1400, 'delivered', '2026-02-21'),
(9, 'SSD', 6800, 'cancelled', '2026-03-28'),

(10, 'Laptop', 80000, 'delivered', '2026-01-28'),
(10, 'Monitor', 24000, 'pending', '2026-02-25'),
(10, 'Keyboard', 3200, 'delivered', '2026-03-14'),

(11, 'Mouse', 1250, 'delivered', '2026-01-17'),
(11, 'Headphones', 3600, 'cancelled', '2026-02-26'),
(11, 'Webcam', 4300, 'delivered', '2026-03-30'),

(12, 'SSD', 7200, 'delivered', '2026-01-29'),
(12, 'Keyboard', 2900, 'cancelled', '2026-02-27'),
(12, 'Monitor', 23000, 'pending', '2026-03-29');


select * from users;
select * from orders;

-- TASK 1 --
create view active_orders as
select * from orders where status = 'cancelled';
select * from active_orders;
-- TASK 1 --

-- TASK 2 --
INSERT INTO orders (user_id, product, amount, status) VALUES (1, 'External Hard Drive', 6000, 'cancelled');
select * from active_orders where user_id <> 1;
-- TASK 2 --


-- TASK 3 --
create view public_users as
select id, username, created_at from users;
-- TASK 3 --



-- TASK 4 --
create view hr_users as
select id, username,email, role, salary, created_at from users;
select * from hr_users;
-- TASK 4 --

-- TASK 5 --
create view user_order_summary as
select u.username, count(o.id) as total_order_count, sum(o.amount) as total_amount_spent 
from users u 
left join orders o
on u.id = o.user_id
group by u.id, u.username;
select * from user_order_summary;
-- TASK 5 --



-- TASK 6 --
create or replace view public_users as
select  id, username, email, created_at from users;
select * from public_users;
-- TASK 6 --


-- TASK 7 --
drop view hr_users;
-- show full tables // lists base + views
show full tables where table_type = 'VIEW';
-- TASK 7 --


-- TASK 8 --
CREATE USER 'report_user'@'localhost' 
IDENTIFIED BY '5gv4df5';

select User, Host from mysql.user;
-- TASK 8 --

-- TASK 9 --
select * from online_orders.public_users;

grant select on online_orders.public_users
to 'report_user'@'localhost';

show grants for 'report_user'@'localhost';

-- TASK 9 --


-- TASK 10 --
/* 
only this will run with report_user: 
select * from public_users; (works fine)

select * from users would throw error (access denied)
*/
-- TASK 10 --

-- TASK 11 --
/*
in python 'testing.py'

sql code and user input got mixed in the same string when tested.
so the input can become the part of the sql syntax instead of being treated only as data3
this is commonly known as sql injection
*/
-- TASK 11 --



-- TASK 12 --
/*


PART A
# QUERY BUILT USING CONCATENATION # 
username = input("Enter username: ")
query = "SELECT * FROM users WHERE username = '" + username + "'"
*NOTE* : user input is directly concatenated with the sql query so the input can affect the sql query structure


# QUERY BUILT USING ? PLACEHOLDER # 
username = input("Enter username: ") 
query = "select * from users where username = ?"
*NOTE* : user input is separated from the sql query so the input is passed as a parameter instead of being inserted into the sql string


# QUERY BUILT USING STRING FORMATTING # 
username = input("Enter username: ")
query = f"SELECT * FROM users WHERE username = '{username}'"
*NOTE* : user input is directly concatenated with the sql query using the f-string so the input can affect the sql query structure



PART B 
# QUERY BUILT USING USER INPUT FOR COLUMN NAME #

allowed_columns = ["username", "salary", "created_at"]
sort_column = input("Enter column to sort by: ")
if sort_column in allowed_columns:
    query = f"SELECT * FROM users ORDER BY {sort_column}"
    print(query)
else:
    print("Invalid column")

*NOTE* : user input is used as a column name in the sql query, so placeholders cannot normally be used here, an allowlist is used to allow only predefined column names and prevent unwanted input from becoming part of the sql query structure.

*/
-- TASK 12 --


-- TASK 13 --
/*
# DEFENSE IN DEPTH CHECKLIST #

least-privilege database accounts:
- give database usser only the required permissions
- limits unauthorized access or changes

no admin credentials in app code:
- do not store admin databasse credentials in application code
- limits access to full database privileges

hashed passwords:
- store passwords as hashes and never plain text
- limits password exposure if the database is accessed

input validation:
- check user input before processing it
- limits invalid or unexpected input

generic error messages:
- do not show raw sql or database errors to the users
- limits exposure of database information

logging:
- record important security related activities
- helps detect and investigate suspicious activity
*/
-- TASK 13 --













