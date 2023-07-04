/*
	inner join: returns the intersection of two tables
    
    Syntax:
    
    select column(s) from table1
    inner join table2
    on table1.cloumn = table2.cloumn;
*/

select city.CountryCode, city.name
from world.city
inner join
world.country on city.population = country.population;