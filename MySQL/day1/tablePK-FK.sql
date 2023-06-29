/*
	This is multi-line comment
    Create a table with PK user ID autoincremented size 3
    User has a name (not null) and a unique lastname (not null)
    User has DOB (date)
*/
create table if not exists testdb.users(
	userid integer primary key auto_increment,
	first_name varchar(255) not null,
	last_name varchar(255) unique not null,
	dob date
)auto_increment=100;

/*
	Create a table associated with users called 'blogs'
	the user id is the FK for the blogs table
    blog id is autoincremented primary key
    text (size 255) is the blog text
*/

set foreign_key_checks=0;			-- enable tables association
set global foreign_key_checks=0;	-- enable tables association (globally)

create table testdb.blogs(
	blogid integer primary key auto_increment,
    userid integer,
	text varchar(255) NOT NULL,    
	foreign key (userid) references testdb.users(userid)
);
