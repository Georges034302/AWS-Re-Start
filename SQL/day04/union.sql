/*
	Union joins 2 tables
    Union removes duplicate rows
    
    Syntax:
    select column(s) from table1
    union
    select column(s) from table2;
 */
select name, CountryCode, population from world.city
union
select name,Code, population from world.country
order by name; 
