
-- subqueries
USE shopdb;

select * from customers;
select * from orders;

-- with where 
select * from orders
where amount > (
select avg(amount)
from orders
);

-- select
select name,
( select count(*)
from orders o
where c.customer_id = o.customer_id ) as order_count
from customers c; 

-- with from
select summary.customer_id,summary.avg_amount
from
(select customer_id,avg(amount) as avg_amount
from orders 
group by customer_id
) as summary;