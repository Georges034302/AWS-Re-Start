select name, mark, grade,
ntile(5) over(partition by grade order by mark) 'NTile'
from testdb.students;
/*
	- ntile(integer-value) gives each row a number with max rank = integer-value
    - rank value is spread over the category partition
    - rank value overlaps multiple times to the end of the category
    - ranking is reset when partition category changes
 */