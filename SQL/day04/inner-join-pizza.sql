select item_name from testdb.products as products
inner join 
testdb.shop as shop
on products.item_name = shop.item_type;