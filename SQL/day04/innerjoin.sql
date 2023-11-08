select city.CountryCode, city.name
from world.city
inner join world.country
on city.CountryCode = country.Code;
