CREATE 	DATABASE IF NOT EXISTS instagram;
USE instagram;

CREATE TABLE user(
id INT PRIMARY KEY,
age INT,
name VARCHAR(30) NOT NULL,
username VARCHAR(40) UNIQUE,
followers INT DEFAULT 0,
following INT,
CONSTRAINT CHECK (age>=18)
);

CREATE TABLE post(
id INT PRIMARY KEY,
content VARCHAR(1000),
user_id INT,
FOREIGN KEY (user_id) REFERENCES user(id)
);

-- alter
alter table post
add column bio varchar(10000);

-- drop
alter table post
drop column bio;

-- rename table
alter table post
rename to details;

-- rename column
alter table details
change column content bio varchar(3000);

select * from details;

INSERT INTO user
(id,age,name,username,followers,following)
VALUES
(1,21,"adam","adam_hero",123,145),
(2,20,"ram","ramyan",200,200),
(3,23,"hari","hari_don",300,400),
(4,22,"sita","cutie_sita",100,20);

SELECT name,followers FROM user
WHERE followers>=200;

-- use age + 1 = 18 arithmetic operator

-- frequently used operators
-- and(both true) ,or(atleast one),between(select for given range) 
select name,age
from user
where age>15 or followers >200;

select name,age
from user
where age BETWEEN 15 and 20 ;

-- in(matches any values in list)
SELECT name,followers,username
from user
where username IN("donald_123","adam_hero","rambhatta");

-- limit by clause
SELECT name 
from user
where age >15 
limit 3;

-- order by clause
select age,name,followers
from user
order by followers asc;

-- aggregrate function
select count(followers)
from user
where age =20;

-- group by clause
select name,max(followers)
from user
GROUP by name;

-- having clause
select name,max(followers)
from user
GROUP by name
having max(followers) > 200;

UPDATE user
SET followers = 400
where age = 20;
SET SQL_SAFE_UPDATEs = 0;

SELECT * FROM user;



INSERT INTO post
(id,content,user_id)
VALUES
(101,"i am a youtuber",2),
(102,"i love food",4),
(103,"programming is easy",2);


SELECT * FROM post;
