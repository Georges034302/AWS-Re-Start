SELECT *
FROM university.students INTO OUTFILE '[path-to-file]\\students.csv' 
FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n';