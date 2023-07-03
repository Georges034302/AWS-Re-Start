select name, mark, grade,
ntile(4) over(partition by grade order by mark) 'NTile'
from testdb.students;
-- ntile(value) decides the size of the ranks from 1 to value
-- spreads the rank values for all the category
-- if the category rows are bigger than rank value
-- ntile overlaps with as many duplicates (categorSize - ntileSize)