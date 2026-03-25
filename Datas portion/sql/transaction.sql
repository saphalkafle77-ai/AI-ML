CREATE DATABASE prime;

USE prime;

create table accounts(
   id int primary key auto_increment,
   name varchar(50),
   balance decimal(10, 2)
   );
   
insert into accounts
(name,balance)
values
("adam",500.00),
("bob",300.00),
("charlie",1000.00);



-- transaction
START TRANSACTION;

UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;

COMMIT;
SELECT * FROM accounts;

-- rollback

START TRANSACTION;

UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 3;

rollback;


-- savepoint
 start transaction;
 update accounts set balance = balance + 1000 where id = 1;
 savepoint after_wallet_topup;
 
 update accounts set balance = balance + 10 where id = 1;
 -- error
 rollback to after_wallet_topup;
 commit;
 
 select * from accounts;