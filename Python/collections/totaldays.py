#Req: Create a list of 12 months [no leap year]
#   - Read a day and a month from STDIN
#   - Determine and show the total days from Jan 1 until that day

days = [31,28,31,30,31,30,31,31,30,31,30,31]

day = int(input('day = '))
month = int(input('month = '))

i = 0 # this is the month number (January)
total = 0

while i < month-1:
    total += days[i]
    i+=1
total += day 

print(f'Total days = {total}')