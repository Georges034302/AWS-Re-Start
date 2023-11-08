select item_name from testdb.products
union
select item_type from testdb.shop;