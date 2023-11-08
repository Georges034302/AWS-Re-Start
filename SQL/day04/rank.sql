select name, mark, grade,
rank() over(partition by grade order by mark) 'Rank'
from testdb.students;
/*
	- rank() gives each row a number
    - duplicate rows have the same rank-number
    - next rank is skipped for as many previous duplicate rows
    - ranking is reset when partition category changes
 */