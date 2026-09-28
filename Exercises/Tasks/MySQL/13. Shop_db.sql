create database shop_db;
use shop_db;

create table products(
id int primary key auto_increment,
name varchar(100),
category varchar(100),
brand varchar(50),
price decimal(10,2),
stock int,
rating decimal(3,1),
launch_date date
);

insert into products(name,category,brand,price,stock,rating,launch_date)
values
('iPhone 15 Pro', 'Electronics', 'Apple', 999.00, 25, 4.8, '2024-09-20'),
('Galaxy S24', 'Electronics', 'Samsung', 899.00, 40, 4.6, '2024-01-31'),
('Pixel 9 Pro', 'Electronics', 'Google', 899.00, 30, 4.5, '2024-08-22'),
('OnePlus 12', 'Electronics', 'OnePlus', 799.00, 35, 4.4, '2024-01-23'),
('iPhone 16', 'Electronics', 'Apple', 899.00, 45, NULL, '2024-09-20'),

('MacBook Air', 'Computers', 'Apple', 1099.00, 15, 4.7, '2024-03-04'),
('ThinkPad X1', 'Computers', 'Lenovo', 1299.00, 20, 4.6, '2025-01-15'),
('MacBook Pro', 'Computers', 'Apple', 1599.00, 10, 4.9, '2024-11-08'),
('Dell XPS 15', 'Computers', 'Dell', 1399.00, 18, 4.5, '2023-10-10'),
('HP Pavilion', 'Computers', 'HP', 799.00, 25, NULL, '2025-06-12'),

('AirPods Pro', 'Accessories', 'Apple', 249.00, 50, 4.7, '2024-09-20'),
('Galaxy Buds', 'Accessories', 'Samsung', 149.00, 60, 4.3, '2025-02-10'),
('Sony WH-1000XM5', 'Accessories', 'Sony', 399.00, 30, 4.8, '2023-05-20'),
('Pixel Buds', 'Accessories', 'Google', 179.00, 45, NULL, '2024-10-15'),
('OnePlus Buds Pro', 'Accessories', 'OnePlus', 199.00, 55, 4.4, '2024-07-25'),

('iPad Mini', 'Tablets', 'Apple', 499.00, 35, 4.6, '2024-10-23'),
('Galaxy Tab S9', 'Tablets', 'Samsung', 699.00, 25, 4.5, '2023-08-11'),
('iPad Pro', 'Tablets', 'Apple', 999.00, 20, 4.8, '2024-05-15'),
('Lenovo Tab M10', 'Tablets', 'Lenovo', 249.00, 40, NULL, '2025-03-18'),
('Pixel Tablet', 'Tablets', 'Google', 499.00, 30, 4.2, '2024-06-20'),

('Nike Air Max', 'Footwear', 'Nike', 180.00, 40, 4.7, '2024-03-15'),
('Adidas Ultraboost', 'Footwear', 'Adidas', 160.00, 50, 4.6, '2025-01-20'),
('Puma Pro Runner', 'Footwear', 'Puma', 120.00, 60, 4.3, '2024-08-05'),
('Nike Mini Runner', 'Footwear', 'Nike', 100.00, 45, NULL, '2025-05-10'),
('Reebok Classic', 'Footwear', 'Reebok', 90.00, 55, 4.1, '2023-11-12'),
('Adidas Max Cushion', 'Footwear', 'Adidas', 140.00, 35, 4.4, '2024-09-01'),
('Puma Street Pro', 'Footwear', 'Puma', 110.00, 40, 4.2, '2025-07-15');

select * from products;


select 
category,
count(*) as product_count,
round(avg(price),2) as avg_price,
sum(stock) as total_stock,
min(rating) as min_rating,
max(rating) as max_rating
from products
where 
launch_date >= current_date()- interval 2 year and name not like '%pro%'
group by category
order by sum(stock*price) desc;



