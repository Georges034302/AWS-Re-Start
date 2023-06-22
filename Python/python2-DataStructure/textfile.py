# Open a text file with a r/w mode
# Read a string from STDIN and write the string to a text file
# Read the textfile data and display it to the STDOUT

data = input("String: ")
f = open("demo.txt","a")    # opens a file and create a handler object
f.write(data+"\n")          # w overwrites data, a appends data
f.close()                   # always close the stream when you finish working

f = open("demo.txt","r")
print(f.read())
f.close()