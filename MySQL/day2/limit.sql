/*
	select students name and mark for students with grades C or D 
    Only show the top 5
*/

select name, mark
from testdb.students
where grade = 'D' or grade = 'C' -- where grade in ('C','D')
order by mark desc limit 5;