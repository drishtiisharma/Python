use practice;
select * from orders;
select if(id>1, 'yes', 'no') from orders;
select pname,stock, if(stock>0,'available','out of stock') as status from products;

select pname,
price,
case
when price<50 then 'cheap'
when price<100 then 'medium'
else 'expensive'
end as price_category from products;

CREATE TABLE customers (
    id INT,
    name VARCHAR(50),
    phone VARCHAR(20)
);

INSERT INTO customers VALUES
(1, 'Alice', '9876543210'),
(2, 'Bob', NULL),
(3, 'Charlie', '9123456780');

select name, ifnull(phone,'not available') as phone from customers;

select coalesce(null,null,'hello',null,'world') as first_non_null;


select nullif(10,10.0);

