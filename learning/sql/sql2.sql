CREATE DATABASE IF NOT EXISTS college;
USE  college;

CREATE TABLE teacher(
id INT PRIMARY KEY,
name varchar(20) NOT NULL,
subject varchar(20),
salary INT default 15000);

INSERT into teacher
(id,name,subject,salary)
VALUES
(23,"ajay","math",50000),
(47,"bharat","english",60000),
(18,"chetan","chemistry",45000),
(9,"divya","physics",75000);

alter table teacher
change column salary ctc INT default 20000;

update teacher
set ctc = ctc + (0.25)*ctc;
SET SQL_SAFE_UPDATES = 0;

ALTER TABLE teacher
ADD COLUMN city varchar(30) default  "gurgaun";

ALTER TABLE teacher
DROP COLUMN ctc;

SELECT * FROM teacher;
select * FROM teacher
where ctc > 4000;


CREATE TABLE student(
roll_no INT PRIMARY KEY,
name varchar(30),
city varchar(30) default "kathmandu",
marks INT default 0);


INSERT INTO student(
roll_no,name,city,marks)
values
(101,"adam","delhi",76),
(108,"bob","kathmandu",65),
(124,"casey","pokhara",94),
(112,"duke","pokhara",80);

select * from student
where marks > 75;

select DISTINCT city
from student;

select city from student
group by city;

select city,max(marks) from student
group by city
;

select avg(marks) from student;

ALTER TABLE student
ADD COLUMN grade VARCHAR(10);

update student
set grade = "0"
where marks >=80;

update student
set grade = "A"
where marks BETWEEN 70 AND 80;

update student
set grade = "B"
where marks BETWEEN 60 AND 70;

select * from student;

