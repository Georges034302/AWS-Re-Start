select trim(name), 
length(name) 'Length',
length(trim(name)) 'Actual Length'
from testdb.students;