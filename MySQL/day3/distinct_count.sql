SELECT count(distinct Language) 'Distinct Languages',
count(Language) 'Available Languages'
FROM world.countrylanguage;