select name, mark, grade,
rank() over(partition by grade order by mark) 'Rank',
dense_rank() over(partition by grade order by mark) 'Dense Rank',
row_number() over(partition by grade order by mark) 'Row Number',
ntile(5) over(partition by grade order by mark) 'NTile'
from testdb.students;