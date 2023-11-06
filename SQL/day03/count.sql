/*
 * Determine the total of distinct languages in the  world countryLanguage table
 * 
 */
 
select count(distinct(Language)) as 'Language Count'
from world.countrylanguage;