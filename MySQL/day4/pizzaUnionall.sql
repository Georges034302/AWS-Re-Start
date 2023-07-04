/*
	Show the union between tables including duplicates by item type
*/

select type
from testdb.pizza
union all
select item_type
from testdb.shop
order by type;