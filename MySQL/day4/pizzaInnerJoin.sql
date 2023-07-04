/*
	Find the intersection between shop and pizza tables
*/

select type
from testdb.pizza as pizza
inner join testdb.shop as shop
on pizza.type = shop.item_type;