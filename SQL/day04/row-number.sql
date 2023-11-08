select name, mark, grade,
row_number() over(partition by grade order by mark) 'Row Number'
from testdb.students;
/*
	- row_number() gives each row a number
    - duplicate rows have unique rank-number (no duplicate ranks)
    - next rank is the next number (no skipping)
    - ranking is reset when partition category changes
 */