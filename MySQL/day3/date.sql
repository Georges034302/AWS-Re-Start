/*
	Show current students' grades
*/

select name, grade, 
dayname(CURDATE()) 'Today', 
concat(day(curdate()),'rd') as 'Day',
monthname(curdate()) 'Month'
from testdb.students;