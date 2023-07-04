/*
	Returns all records from both tables
*/

select ci.Name as 'City Name'
from world.city as ci
cross join
world.country as co
on ci.CountryCode = co.Code;