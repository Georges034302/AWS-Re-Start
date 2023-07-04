select ci.Name as 'City Name'
from world.city as ci
inner join
world.country as co
on ci.CountryCode = co.Code;