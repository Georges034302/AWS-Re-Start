/*
	Select names from students
	generate usernames formatted as: <Name initial>-<ID>
*/

select name,
concat(substring(name,1,1),'-',ID) 'Username'
from testdb.students;