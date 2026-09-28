show databases;
use practice;
show tables;
/*
CREATE TABLE products (
    id INT,
    pname VARCHAR(50),
    price DECIMAL(10,2),
    stock INT
);

INSERT INTO products VALUES
(1, 'Keyboard', 45.75, 20),
(2, 'Mouse', 25.49, 15),
(3, 'Monitor', 199.99, 5),
(4, 'USB Cable', 10.25, 0),
(5, 'Headphones', 75.80, 8);


*/
select * from products;
-- round()
select pname,round(price) as 'rounded_price' from products;
select round(254.3651,2);

-- ceil and floor
select ceil(10.1);
select floor(10.1);

-- abs
select abs(-25);

-- mod - shows remainder
select mod(10,5);
select mod(22,3);

-- power()
select power(2,5);
-- sqrt
select '2400' as number, round(sqrt(2400),2) as sqrt;

-- random
select rand();

-- signs, returns 1 for positive, -1 for negative and 0 for 0
select sign(-10);
select sign(20);
select sign(0);



