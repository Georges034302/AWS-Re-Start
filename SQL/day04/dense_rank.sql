select name, mark, grade,
dense_rank() over(partition by grade order by mark) 'Dense Rank'
from testdb.students;
/*
	- dense_rank() gives each row a number
    - duplicate rows have the same rank-number
    - next rank is the next number (no skipping)
    - ranking is reset when partition category changes
 */