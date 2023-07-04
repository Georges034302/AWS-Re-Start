/*
	left join: returns all table 2 records (without the intersection)
    and leave out the rest of table 2
    
    Syntax:
    
    select column(s) from table1
    right join table2
    on table1.cloumn = table2.cloumn;
*/

select city.CountryCode, city.name
from world.city
right join
world.country on city.population = country.population;