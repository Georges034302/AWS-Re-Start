select name, mark, grade,
rank() over(partition by grade order by mark) 'Rank'
from testdb.students;
-- rank() gives each row a number
-- duplicates have same rank number
-- next rank is skipped for as many duplicates
-- ranking is reset when category changes