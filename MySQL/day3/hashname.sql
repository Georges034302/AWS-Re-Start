/*
	select all names and grades
    but only show the initial (first letter) of the name
    rest of of the name replace by hash
*/
select name, 
insert(name,2,length(name),'#') as 'Hash-Name' 
from testdb.students;