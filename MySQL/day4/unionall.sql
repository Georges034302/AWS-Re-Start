/*
	union all: joins two tables (allowing dupplicate rows)
    
    Syntax:
    
    select column(s) from table1
    union all
    select columns(s) from table2;
*/

select name, CountryCode, population from  world.city
union all
select name, Code, population from world.country;