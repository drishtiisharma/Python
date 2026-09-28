use practice;

select count(*) as 'no. of rows' from products;
select sum(stock) as 'total stock' from products;
select round(avg(price),2) as 'avg price' from products;
select min(price) as 'min price' from products;
select max(price) as 'max price' from products;
