create database store_db;
use store_db;

create table products(
id int primary key auto_increment,
pname varchar(50),
category varchar(50) default 'misc',
price float default 0.00,
stock int,
discontinued boolean,
supplier varchar(50)
);

insert into products values
(1, 'Keyboard', 'Electronics', 45.00, 20, FALSE, 'TechSupply'),
(2, 'Mouse', 'Electronics', 25.00, 50, FALSE, 'TechSupply'),
(3, 'Monitor', 'Electronics', 180.00, 10, FALSE, 'DisplayWorld'),
(4, 'USB Cable', 'Electronics', 15.00, 0, TRUE, 'TechSupply'),
(5, 'Headphones', 'Electronics', 75.00, 15, FALSE, NULL),

(6, 'Office Chair', 'Furniture', 120.00, 5, FALSE, 'FurniCo'),
(7, 'Desk', 'Furniture', 250.00, 3, FALSE, 'FurniCo'),
(8, 'Bookshelf', 'Furniture', 150.00, 0, TRUE, NULL),
(9, 'Lamp', 'Furniture', 40.00, 12, FALSE, 'LightHouse'),

(10, 'Notebook', 'Stationery', 5.00, 100, FALSE, 'PaperWorld'),
(11, 'Pen', 'Stationery', 2.00, 200, FALSE, 'PaperWorld'),
(12, 'Marker', 'Stationery', 8.00, 80, FALSE, 'PaperWorld'),
(13, 'Stapler', 'Stationery', 12.00, 30, FALSE, NULL),

(14, 'Calculator', 'Stationery', 35.00, 25, FALSE, 'OfficeGoods'),
(15, 'Webcam', 'Electronics', 90.00, 7, FALSE, 'DisplayWorld');

INSERT INTO products (id, pname, category, price, stock, discontinued, supplier)
VALUES
(16, 'Tablet', 'Electronics', 300.00, 8, FALSE, 'TechSupply'),
(17, 'Sofa', 'Furniture', 500.00, 2, FALSE, 'FurniCo'),
(18, 'Eraser', 'Stationery', 3.00, 150, FALSE, 'PaperWorld');

select * from products order by category;

update products set price = price +(0.10 *price) where category ='Furniture';


select * from products;
select pname, price from products;

select distinct category from products;
select distinct supplier from products;
select count(distinct category) from products;

select * from products order by price;
select * from products order by category asc, price desc;
select * from products order by price limit 5;


select * from products where category = 'Electronics' and price<100;
select * from products where category in ('Electronics','Stationery');

select * from products where price > 50;
select * from products where category = 'Electronics';
select * from products where stock = 0;


delete from products where stock = 0 and discontinued = true;
select * from products;
select * from products limit 5 offset 5;































































































