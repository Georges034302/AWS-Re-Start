create table if not exists testdb.products(
	item_number integer primary key auto_increment,
    item_name varchar(100) unique not null,
    price integer not null
);

insert into testdb.products(item_name,price)
values
('Supreme',12),
('Vegeterian',11),
('Meat Lovers',13),
('Pepperoni',12),
('Hawaiin',11),
('Four Cheese',12),
('BBQ Chicken',13);

create table if not exists testdb.shop(
	order_number integer primary key auto_increment,
    item_type varchar(100) unique not null,
    total integer not null,
    quantity integer not null
);

insert into testdb.shop(item_type,total,quantity)
values
('supreme',24,2),
('Hawaiin',33,3),
('Pepperoni',12,1);





