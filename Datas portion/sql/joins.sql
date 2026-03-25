CREATE DATABASE shopdb;
USE shopdb;

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(50),
    city VARCHAR(50)
);

INSERT INTO customers (customer_id, name, city) VALUES
(1, 'Alice', 'Mumbai'),
(2, 'Bob', 'Delhi'),
(3, 'Charlie', 'Bangalore'),
(4, 'David', 'Mumbai');

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    amount INT
);


INSERT INTO orders (order_id, customer_id, amount) VALUES
(101, 1, 500),
(102, 1, 900),
(103, 2, 300),
(104, 5, 700);


-- inner joins
select *
from customers c
inner join orders o
on c.customer_id = o.customer_id;

-- left joins
select *
from customers c
left join orders o
on c.customer_id = o.customer_id;

-- outer joins
select * from customers c
left join orders o
on c.customer_id = o.customer_id
union 
select * from customers  c
right join orders  o
on c.customer_id = o.customer_id;

-- cross join
select * from customers
cross join orders;


-- self join
select * from customers as A
join customers as B
ON A.customer_id = B.customer_id;



-- exclusive join
select * from customers c 
left join orders o
on c.customer_id = o.customer_id
where o.customer_id is NULL;

select * from customers c
right join orders o
on c.customer_id = o.customer_id
where c.customer_id is NULL;