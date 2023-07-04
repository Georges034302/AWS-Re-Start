/*
	left join: returns all table 1 records (with the intersection)
    and leave out the rest of table 2
    
    Syntax:
    
    select column(s) from table1
    inner join table2
    on table1.cloumn = table2.cloumn;
*/

select city.CountryCode, city.name
from world.city
left join
world.country on city.population = country.population;