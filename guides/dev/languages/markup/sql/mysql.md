https://www.cs.kent.ac.uk/systems/cgi-bin/mysql.pl

mysql -u [username] -p -h dragon.kent.ac.uk [tableName]

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
