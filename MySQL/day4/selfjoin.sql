select A.Name as 'Not Equal Names'
from world.city as A, world.city as B
where A.Name <> B.Name
order by A.CountryCode;
