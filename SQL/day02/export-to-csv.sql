select * from testdb.students
into outfile '[path-to-file]\\students.csv'
fields terminated by ',' enclosed by '"' lines terminated by '\n';