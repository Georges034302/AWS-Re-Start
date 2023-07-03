select name, mark, grade,
dense_rank() over(partition by grade order by mark) 'Dense Rank'
from testdb.students;
-- dense_rank() gives each row a number
-- duplicates have same rank number
-- next rank is the next value (no skipping)
-- ranking is reset when category changes