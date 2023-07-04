/*
	Create a table 'pizza'. pizza has
    item_number (autoincrement)
    type
    price
    
    create a table 'order'. shop has
    order_number (autoincrement)
    total
    item_type
    item_quantity    
*/
create table if not exists testdb.pizza(
	item_number integer primary key auto_increment,
	type varchar(50) unique not null,
	price integer not null
);

insert into testdb.pizza(type,price)
values
('supreme',12),
('hawaiin',12),
('soujuk',12),
('vegeterian',12),
('peperoni',12),
('bbq chicken',12);

create table if not exists testdb.shop(
	order_number integer primary key auto_increment,
	item_type varchar(50) unique not null,
    total decimal not null,
	item_quantity integer not null
);

insert into testdb.shop(item_type,total,item_quantity)
values
('supreme',26.5,2),
('bbq chicken',28.5,2),
('hawaiin',28.5,2);


