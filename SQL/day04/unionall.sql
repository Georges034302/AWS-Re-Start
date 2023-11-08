/*
	Union all joins 2 tables
    Union all allows duplicate rows
    
    Syntax:
    select column(s) from table1
    union all
    select column(s) from table2;
 */
select name, CountryCode, population from world.city
union all
select name,Code, population from world.country
order by CountryCode; 