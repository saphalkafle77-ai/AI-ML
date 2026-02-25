use shopdb;
select * from customers;

-- views
create view view1 as 
select customer_id,name from customers;

select * from view1
where name = "Alice";

-- from multiple table(join)
create view view2 as
select c.customer_id , c.name, o.order_id from customers c
inner join orders o
on c.customer_id = o.customer_id;

select * from view2;

-- drop view is possible
drop view view1;

-- index 
create table accounts(
account_id int primary key,
name varchar(50),
balance decimal(10,2),
branch varchar(50) );

insert into accounts
values
(1,"adam",500.00,"ktm"),
(2,"bob",500.00,"dang"),
(3,"charlie",500.00,"pokhara"),
(4,"davis",500.00,"rautahat");

select * from accounts;

create index idx_branch on accounts(branch);
show index from accounts;

select * from accounts
where branch = "rautahat";

-- multiple column
create index idx2 on accounts(branch,balance);

drop index idx2 on accounts;

-- stored procedures
delimiter $$
create procedure check_blc(IN acc_id INT)

begin
select balance from accounts
where account_id = acc_id;
end $$
delimiter ;
call check_blc(1);

-- also include output

delimiter $$
create procedure check_blc(out bal decimal(10,2))

begin
select balance into bal from accounts
where account_id = acc_id;
end $$
delimiter ;
call check_blc(@balance);
select @balance;
 