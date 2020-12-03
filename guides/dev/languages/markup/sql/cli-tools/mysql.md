//get a shell in db
mysql -u [username] -p -h [serverName] [dbName]
    mysql -u eh -p -h sqlserver.ac.uk ehDb 
//run sql script
source ./x.sql

# cmds
//Will show the names of all tables in your database.
SHOW TABLES;
//Will show the columns and types in the person table.
DESCRIBE person;
//Will show all the data in the doctor table.
SELECT * FROM doctor;


# select
## no tables
select sqrt(25);
select current_date, current_time, current_user;

select current_date as today, current_time as now,
current_user as me;


create table car(
    reg_no char(7) primary key,
    make varchar(20),
    model varchar(20),
    colour varchar(20),
    owner integer
);
insert into driver (driver_no, name) values (1, 'Bill Smith');
insert into car (reg_no, make, model, colour, owner)
values ('AA65ABC', 'Ford', 'Focus', 'green', 1);

select reg_no, make, model, colour, owner from car;
select * from car;
select * from car where make='Ford' and colour='green';
select * from car, driver;
select * from car join driver on owner = driver_no;
select * from car, driver where owner = driver_no;
