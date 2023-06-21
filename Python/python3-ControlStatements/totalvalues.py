# Read values from STDIN until -1
# Calculate and show the total and average at 3-decimal points

n = int(input("n = "))

total = 0
count = 0
while n != -1:
    total += n
    n = int(input("n = "))
    count+=1

print(f'Total = {total}')
print(f'Average = {total/count:.3f}')

